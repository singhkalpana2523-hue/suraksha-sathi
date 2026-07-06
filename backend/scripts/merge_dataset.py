from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple


@dataclass
class MergeConfig:
    input_dir: str
    output_dir: str
    output_filename: str = "scam_dataset.json"

    # expected input filenames
    rbi_filename: str = "rbi.json"
    npci_filename: str = "npci.json"
    certin_filename: str = "certin.json"
    generated_filename: str = "generated_examples.json"


def _load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _normalize_records(data: Any) -> List[Dict[str, Any]]:
    # Accept either: {"records": [...]} or [...] or single record.
    if data is None:
        return []

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        if "records" in data and isinstance(data["records"], list):
            return data["records"]

        # If dict looks like a single record
        if all(
            k in data
            for k in ["id", "title", "category", "subcategory", "severity"]
        ):
            return [data]

    raise ValueError("Unsupported JSON format for records")


def _normalize_text(s: Any) -> str:
    if s is None:
        return ""

    if not isinstance(s, str):
        s = str(s)

    return " ".join(s.lower().split())


def _jaccard_similarity(a: str, b: str) -> float:
    ta = set(_normalize_text(a).split())
    tb = set(_normalize_text(b).split())

    if not ta and not tb:
        return 1.0

    if not ta or not tb:
        return 0.0

    inter = len(ta & tb)
    union = len(ta | tb)

    return inter / union if union else 0.0


def _looks_like_duplicate(
    r1: Dict[str, Any],
    r2: Dict[str, Any],
    *,
    threshold: float,
) -> bool:

    t1 = _normalize_text(r1.get("title", ""))
    t2 = _normalize_text(r2.get("title", ""))

    text1 = r1.get("text", "")
    text2 = r2.get("text", "")

    if (
        t1
        and t1 == t2
        and _normalize_text(text1)
        == _normalize_text(text2)
    ):
        return True

    sim_text = _jaccard_similarity(str(text1 or ""), str(text2 or ""))

    if sim_text >= threshold:
        return True

    summary1 = r1.get("summary", "")
    summary2 = r2.get("summary", "")

    if (
        (text1 is None or str(text1).strip() == "")
        and (text2 is None or str(text2).strip() == "")
    ):
        sim_title = _jaccard_similarity(t1, t2)
        sim_summary = _jaccard_similarity(summary1, summary2)

        return max(sim_title, sim_summary) >= max(
            0.75,
            threshold - 0.1,
        )

    return False


def _dedupe(
    records: List[Dict[str, Any]],
    *,
    similarity_threshold: float = 0.9,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:

    exact_seen = set()
    deduped: List[Dict[str, Any]] = []
    duplicates: List[Dict[str, Any]] = []

    for r in records:

        source = r.get("source", "")
        title_norm = _normalize_text(r.get("title", ""))
        text_norm = _normalize_text(r.get("text", ""))

        exact_key = (
            source,
            title_norm,
            text_norm,
        )

        if exact_key in exact_seen:
            duplicates.append(r)
            continue

        exact_seen.add(exact_key)

        is_dup = False

        for kept in deduped:
            if _looks_like_duplicate(
                r,
                kept,
                threshold=similarity_threshold,
            ):
                is_dup = True
                break

        if is_dup:
            duplicates.append(r)
        else:
            deduped.append(r)

    return deduped, duplicates


def merge_dataset(cfg: MergeConfig) -> Dict[str, Any]:
    os.makedirs(cfg.output_dir, exist_ok=True)

    inputs = [
        (
            cfg.rbi_filename,
            _load_json(os.path.join(cfg.input_dir, cfg.rbi_filename)),
        ),
        (
            cfg.npci_filename,
            _load_json(os.path.join(cfg.input_dir, cfg.npci_filename)),
        ),
        (
            cfg.certin_filename,
            _load_json(os.path.join(cfg.input_dir, cfg.certin_filename)),
        ),
        (
            cfg.generated_filename,
            _load_json(os.path.join(cfg.input_dir, cfg.generated_filename)),
        ),
    ]

    merged_records: List[Dict[str, Any]] = []

    for filename, data in inputs:
        records = _normalize_records(data)

        for r in records:
            r.setdefault("source", filename.replace(".json", ""))

        merged_records.extend(records)

    deduped, duplicates = _dedupe(merged_records)

    out_path = os.path.join(
        cfg.output_dir,
        cfg.output_filename,
    )

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(
            deduped,
            f,
            ensure_ascii=False,
            indent=2,
        )

    return {
        "input_count": len(merged_records),
        "output_count": len(deduped),
        "duplicate_count": len(duplicates),
        "output_file": out_path,
    }


if __name__ == "__main__":

    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    dataset_dir = os.path.join(
        base_dir,
        "app",
        "dataset",
        "processed",
    )

    cfg = MergeConfig(
        input_dir=dataset_dir,
        output_dir=dataset_dir,
        output_filename="scam_dataset.json",
    )

    result = merge_dataset(cfg)

    print(json.dumps(result, ensure_ascii=False, indent=2))