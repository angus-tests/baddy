from datetime import date, datetime
from typing import Any, Optional


from dashboards.models.sds.dataset import Dataset


class DatasetFactory:
    """
    A factory used to create Dataset instances.
    """

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Dataset:
        """Creates a Dataset from a dictionary."""
        return Dataset(
            dataset_id=data["dataset_id"],
            period=data["period"],
            survey_id=str(data["survey_id"]),
            schema_version=data["schema_version"],
            published_at=DatasetFactory._parse_date(data.get("published_at")),
        )

    @staticmethod
    def from_list_of_dicts(data: list[dict[str, Any]]) -> list[Dataset]:
        """Creates a list of Datasets from a list of dictionaries."""
        return [DatasetFactory.from_dict(item) for item in data]

    @staticmethod
    def from_kwargs(**kwargs) -> Dataset:
        """Creates a Dataset from keyword arguments."""
        return DatasetFactory.from_dict(kwargs)

    @classmethod
    def _parse_date(cls, value: Any) -> Optional[date]:
        """
        Ensure that the date is in the correct format.
        """
        if isinstance(value, date):
            return value
        elif isinstance(value, datetime):
            return value.date()
        elif isinstance(value, str):
            return datetime.fromisoformat(value).date()
