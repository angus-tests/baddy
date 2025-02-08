"""
Construct all the concrete dependencies for the dashboards module.

i.e instantiate all the classes and services that are required for the dashboards module to function.
"""
from dashboards.repositories.sds.fake_dataset_repository import FakeDatasetRepository
from dashboards.repositories.sdx.fake_sdx_app_repository import FakeSDXAppRepository
from dashboards.services.sds.dataset_service import DatasetService
from dashboards.services.sdx.health_service import HealthService


def get_dataset_service() -> DatasetService:
    """
    Get the sds service.
    """

    # For now we are using fake data, but in the future we could replace this with a real repository.
    return DatasetService(
        FakeDatasetRepository()
    )


def get_health_service() -> HealthService:
    """
    Get the health service.
    """

    # For now we are using fake data, but in the future we could replace this with a real repository.
    return HealthService(
        FakeSDXAppRepository()
    )
