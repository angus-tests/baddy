from dataclasses import dataclass
from datetime import date
from typing import Optional


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

    def _get_date_string(self, date_object: date = None):
        """
        Get a string representation of the date.
        """
        if date_object:
            # Create multiple date formats to search
            date_formats = [
                "%Y-%m-%",
                "%y-%m-%d",
                "%Y/%m/%",
                "%y/%m/%d",
            ]
            date_string = ""
            for date_format in date_formats:
                date_string += f"{date_object.strftime(date_format)} "
            return date_string
        return ""

    def get_search_string(self):
        """
        Get a string representation of the dataset for searching purposes.
        """

        # Store the fields that are dates
        date_values = [self.published_at] if self.published_at else []

        # Create a string representation of the dataset
        main_string = " ".join(
            [
                str(val).lower()
                for val in self.__dict__.values()
                if val and val not in date_values
            ]
        )

        # Add the date values
        date_strings = [self._get_date_string(date_val) for date_val in date_values]

        # Add the date strings to the main string
        return main_string + " ".join(date_strings)
