import os
import json
from datetime import datetime


class DatasetService:

    def __init__(self):

        self.dataset_dir = "app/dataset/processed"

        os.makedirs(self.dataset_dir, exist_ok=True)

    def save_record(self, record):

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"

        path = os.path.join(
            self.dataset_dir,
            filename
        )

        with open(path, "w", encoding="utf-8") as f:

            json.dump(
                record,
                f,
                indent=4,
                ensure_ascii=False
            )

        return filename