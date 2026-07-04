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
        if all(k in data for k in ["id", "title", "category", "subcategory", "severity"]):
            return [data]
    raise ValueError("Unsupported JSON format for records")


def _dedupe(records: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    # Primary dedupe: by (source, title, text) if possible; else fallback to repr.
    seen = set()
    deduped = []

    duplicates = []
    for r in records:
        source = r.get("source", "")
        title = r.get("title", "")
        text = r.get("text", "")
        key = (source, title, text)
        if key in seen:
            duplicates.append(r)
            continue
        seen.add(key)
        deduped.append(r)

    return deduped, duplicates


def merge_dataset(cfg: MergeConfig) -> Dict[str, Any]:
    os.makedirs(cfg.output_dir, exist_ok=True)

    inputs = [
        (cfg.rbi_filename, _load_json(os.path.join(cfg.input_dir, cfg.rbi_filename))),
        (cfg.npci_filename, _load_json(os.path.join(cfg.input_dir, cfg.npci_filename))),
        (cfg.certin_filename, _load_json(os.path.join(cfg.input_dir, cfg.certin_filename))),
        (
            cfg.generated_filename,
            _load_json(os.path.join(cfg.input_dir, cfg.generated_filename)),
        ),
    ]

    merged_records: List[Dict[str, Any]] = []
    for filename, data in inputs:
        records = _normalize_records(data)
        # Track provenance via source if missing
        for r in records:
            r.setdefault("source", filename.replace(".json", ""))
        merged_records.extend(records)

    deduped, duplicates = _dedupe(merged_records)

    out_path = os.path.join(cfg.output_dir, cfg.output_filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(deduped, f, ensure_ascii=False, indent=2)

    return {
        "input_count": len(merged_records),
        "output_count": len(deduped),
        "duplicate_count": len(duplicates),
        "output_file": out_path,
    }


if __name__ == "__main__":
    # Default paths:
    # - input: backend/app/dataset/processed/
    # - output: backend/app/dataset/processed/
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_dir = os.path.join(base_dir, "app", "dataset", "processed")

    cfg = MergeConfig(
        input_dir=dataset_dir,
        output_dir=dataset_dir,
        output_filename="scam_dataset.json",
    )

    result = merge_dataset(cfg)
    print(json.dumps(result, ensure_ascii=False, indent=2))

