from abc import ABC, abstractmethod

from apps.dashboards.dto.sds.dataset import Dataset


class DatasetRepositoryInterface(ABC):
    """
    Interface that defines the methods that must be implemented
    by the sds repository.
    """

    @abstractmethod
    def get_by_id(self, dataset_id: str) -> Dataset:
        """
        Get a sds by its ID.
        :param dataset_id:
        :return: The Dataset object.
        """

    @abstractmethod
    def get_all(self) -> list[Dataset]:
        """
        Get all datasets.
        :return: list of Dataset objects.
        """
