from dashboards.interfaces.sds.dataset_repository_interface import DatasetRepositoryInterface
from dashboards.interfaces.service import Service
from dashboards.models.sds.dataset import Dataset

import logging

logger = logging.getLogger(__name__)


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
        return sorted(self.dataset_repository.get_all(), key=lambda x: x.dataset_id)

    def search_datasets(self, datasets: list[Dataset], search_query: str) -> list[Dataset]:
        """
        Search datasets by name.
        :param datasets: A list of Dataset objects.
        :param search_query: The search query.
        :return: A list of Dataset objects where the query is contained within the id.
        """
        logger.info(f"Starting search for {search_query}")
        matches = []
        # Go through the datasets
        for dataset in datasets:
            did = dataset.dataset_id.lower()
            # Check if the search query is in the dataset id
            if search_query.lower() in did:
                matches.append(dataset)
            else:
                print(f"{search_query.lower()} not in {did}")


        return matches
