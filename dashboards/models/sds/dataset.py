from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List


@dataclass
class Dataset:
    """
    A class that represents a sds
    """
    dataset_id: str
    period: date
    survey_id: str
    schema_version: str
    published_at: Optional[date] = None

    def __str__(self):
        return self.dataset_id

    def get_search_string(self):
        return ' '.join([str(val) for val in self.__dict__.values() if val is not None])
