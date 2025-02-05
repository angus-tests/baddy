from dashboards.interfaces.dataset_repository_interface import DatasetRepositoryInterface
from dashboards.models.dataset import Dataset


class DatasetDatabaseRepository(DatasetRepositoryInterface):
    """
    A concrete implementation of the DatasetRepositoryInterface
    that will use the database to store and retrieve datasets
    """

    def get_by_id(self, dataset_id):
        return Dataset.objects.filter(dataset_id=dataset_id).first()

    def get_all(self):
        return Dataset.objects.all()
