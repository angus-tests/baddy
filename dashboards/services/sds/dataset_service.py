from dashboards.interfaces.sds.dataset_repository_interface import DatasetRepositoryInterface
from dashboards.interfaces.service import Service
from dashboards.models.sds.dataset import Dataset


class DatasetService(Service):
    """
    Service class for interacting with datasets
    """

    def __init__(self, dataset_repository: DatasetRepositoryInterface):
        self.dataset_repository = dataset_repository

    def get_dataset(self, dataset_id: str):
        """
        Get a sds by its ID.
        :param dataset_id:
        :return: Dataset object.
        """
        return self.dataset_repository.get_by_id(dataset_id)

    def get_all_datasets(self) -> list[Dataset]:
        """
        Get all datasets.
        :return: A list of Dataset objects.
        """
        return self.dataset_repository.get_all()

    def search_datasets(self, datasets: list[Dataset], search_query: str) -> list[Dataset]:
        """
        Search datasets by name.
        :param datasets: A list of Dataset objects.
        :param search_query: The search query.
        :return: A list of Dataset objects where the query is contained within the id.
        """

        # Go through each dataset and check if the search query is in the name
        return [dataset for dataset in datasets if search_query.lower() in dataset.dataset_id.lower()]
