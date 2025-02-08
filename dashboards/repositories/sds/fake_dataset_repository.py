from dashboards.factories.sds.dataset_factory import DatasetFactory
from dashboards.interfaces.sds.dataset_repository_interface import DatasetRepositoryInterface
from dashboards.models.sds.dataset import Dataset
from faker import Faker


class FakeDatasetRepository(DatasetRepositoryInterface):
    """
    A repository that will generate fake datasets.
    """

    def __init__(self):
        self.fake = Faker()
        self.number_of_datasets = 20

    def get_by_id(self, dataset_id):
        return self._make_fake_dataset()

    def get_all(self):
        return [self._make_fake_dataset() for _ in range(self.number_of_datasets)]

    def _make_fake_dataset(self) -> Dataset:
        return DatasetFactory.from_dict({
            "dataset_id": self.fake.uuid4(),
            "filename": f"{self.fake.word()}.csv",
            "period": self.fake.date_this_decade().isoformat(),
            "schema_version": self.fake.random_element(elements=("v1", "v2")),
            "survey_id": self.fake.random_int(min=1000, max=9999),
            "published_at": self.fake.date_time_this_year().isoformat(),
        })
