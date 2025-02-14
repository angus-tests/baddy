from dashboards.factories.sds.dataset_factory import DatasetFactory
from dashboards.interfaces.sds.dataset_repository_interface import DatasetRepositoryInterface


class FakeDatasetRepository(DatasetRepositoryInterface):
    """
    A repository that will generate fake datasets with consistent data.
    """

    def __init__(self):
        self.datasets = [
            {
                "dataset_id": "0a4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220101",
                "schema_version": "v1",
                "survey_id": 1234,
                "published_at": "2022-01-01T00:00:00",
            },
            {
                "dataset_id": "1b4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220201",
                "schema_version": "v2",
                "survey_id": 5678,
                "published_at": "2022-02-01T00:00:00",
            },
            {
                "dataset_id": "2c4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220301",
                "schema_version": "v1",
                "survey_id": 9012,
                "published_at": "2022-03-01T00:00:00",
            },
            {
                "dataset_id": "3d4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220401",
                "schema_version": "v2",
                "survey_id": 3456,
                "published_at": "2022-04-01T00:00:00",
            },
            {
                "dataset_id": "4e4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220501",
                "schema_version": "v1",
                "survey_id": 7890,
                "published_at": "2022-05-01T00:00:00",
            },
            {
                "dataset_id": "5f4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220601",
                "schema_version": "v2",
                "survey_id": 1234,
                "published_at": "2022-06-01T00:00:00",
            },
            {
                "dataset_id": "6g4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220701",
                "schema_version": "v1",
                "survey_id": 5678,
                "published_at": "2022-07-01T00:00:00",
            },
            {
                "dataset_id": "7h4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220801",
                "schema_version": "v2",
                "survey_id": 9012,
                "published_at": "2022-08-01T00:00:00",
            },
            {
                "dataset_id": "8i4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20220901",
                "schema_version": "v1",
                "survey_id": 3456,
                "published_at": "2022-09-01T00:00:00",
            },
            {
                "dataset_id": "9j4e5b70-a6d9-44a3-b510-ab53c7fee39f",
                "period": "20221001",
                "schema_version": "v2",
                "survey_id": 7890,
                "published_at": "2022-10-01T00:00:00",
            }
        ]

    def get_by_id(self, dataset_id):
        # Find the dataset with the given ID
        for dataset in self.datasets:
            if dataset["dataset_id"] == dataset_id:
                return DatasetFactory.from_dict(dataset)

    def get_all(self):
        return [DatasetFactory.from_dict(dataset) for dataset in self.datasets]

