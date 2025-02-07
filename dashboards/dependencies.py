"""
Construct all the concrete dependencies for the dashboards module.

i.e instantiate all the classes and services that are required for the dashboards module to function.
"""
from dashboards.repositories.dataset.fake_dataset_repository import FakeDatasetRepository
from dashboards.services.dataset.dataset_service import DatasetService


def get_dataset_service() -> DatasetService:
    """
    Get the dataset service.
    """

    # For now we are using fake data, but in the future we could replace this with a real repository.
    return DatasetService(
        FakeDatasetRepository()
    )
