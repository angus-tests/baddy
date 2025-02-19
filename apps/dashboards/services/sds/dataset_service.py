from apps.dashboards.interfaces.sds.dataset_repository_interface import (
    DatasetRepositoryInterface,
)
from apps.dashboards.interfaces.service import Service
from apps.dashboards.dto.sds.dataset import Dataset

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

    def search_datasets(self, search_query: str) -> list[Dataset]:
        """
        Search datasets using a specific strategy.

        :param search_query: The search query.
        :return: A list of matching Dataset objects.
        """
        # Fetch all datasets
        datasets = self.get_all_datasets()

        # Normalize search query
        search_terms = search_query.lower().split()

        # Filter datasets based on the search query
        return [
            dataset
            for dataset in datasets
            if all(term in dataset.get_search_string() for term in search_terms)
        ]
