from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Dataset:
    """
    A class that represents a dataset
    """
    dataset_id: str
    filename: str
    period: date
    survey_id: str
    schema_version: str
    published_at: Optional[date] = None

    def __str__(self):
        return self.dataset_id
