from dashboards.interfaces.sds.dataset_repository_interface import DatasetRepositoryInterface
from dashboards.interfaces.service import Service
from dashboards.models.sds.dataset import Dataset


class DatasetService(Service):
    """
    Service class for interacting with datasets
    """

    def __init__(self, repository: DatasetRepositoryInterface):
        self.repository = repository

    def get_dataset(self, dataset_id: str):
        """
        Get a sds by its ID.
        :param dataset_id:
        :return: Dataset object.
        """
        return self.repository.get_by_id(dataset_id)

    def get_all_datasets(self) -> list[Dataset]:
        """
        Get all datasets.
        :return: A list of Dataset objects.
        """
        return self.repository.get_all()
