from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List


@dataclass
class Dataset:
    """
    A class that represents a sds
    """
    dataset_id: str
    period: str
    survey_id: str
    schema_version: str
    published_at: Optional[date] = None

    def __str__(self):
        return self.dataset_id

    def _get_date_string(self):
        """
        Get a string representation of the date.
        """
        if self.published_at:
            # Format into long date
            return self.published_at.strftime("%B %d, %Y")
        return ""

    def get_search_string(self):
        """
        Get a string representation of the dataset for searching purposes.
        """

        # Store the fields that are dates
        date_values = [self.published_at] if self.published_at else []

        # Create a string representation of the dataset
        return (" ".join(
            [
                str(val).lower() for val in self.__dict__.values() if val and val not in date_values
            ]
        ) + self._get_date_string()).lower()
