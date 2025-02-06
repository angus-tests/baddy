from datetime import date, datetime
from typing import Any, Optional

from dashboards.models.dataset import Dataset


class DatasetFactory:
    """
    A factory used to create Dataset instances.
    """

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Dataset:
        """Creates a Dataset from a dictionary."""
        return Dataset(
            dataset_id=data["dataset_id"],
            filename=data["filename"],
            period=DatasetFactory.parse_date(data["period"]),
            survey_id=data["survey_id"],
            created_at=DatasetFactory.parse_datetime(data.get("created_at")),
        )

    @staticmethod
    def from_kwargs(**kwargs) -> Dataset:
        """Creates a Dataset from keyword arguments."""
        return DatasetFactory.from_dict(kwargs)

    @staticmethod
    def parse_date(value: Any) -> date:
        """Parses a date string or object into a `date` instance."""
        if isinstance(value, date):
            return value
        return datetime.strptime(value, "%Y-%m-%d").date()

    @staticmethod
    def parse_datetime(value: Optional[Any]) -> Optional[datetime]:
        """Parses a datetime string or object into a `datetime` instance."""
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
