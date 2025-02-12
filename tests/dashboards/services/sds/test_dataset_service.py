from unittest.mock import MagicMock

from django.test import TestCase

from dashboards.factories.sds.dataset_factory import DatasetFactory
from dashboards.interfaces.sds.dataset_repository_interface import DatasetRepositoryInterface
from dashboards.services.sds.dataset_service import DatasetService


class TestDatasetService(TestCase):

    def setUp(self):
        self.fake_dataset_repository = MagicMock(spec=DatasetRepositoryInterface)
        self.dataset_service = DatasetService(
            self.fake_dataset_repository
        )

    def test_basic_search(self):
        datasets = [
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
            }
        ]

        # Create a list of Dataset objects from the dictionaries
        datasets = DatasetFactory.from_list_of_dicts(datasets)

        # Mock the return value of get_all_datasets
        self.fake_dataset_repository.get_all.return_value = datasets

        # Search for the dataset with the ID "0a4e5b70-a6d9-44a3-b510-ab53c7fee39f"
        search_query = "0a4e5b70-a6d9-44a3-b510-ab53c7fee39f"
        result = self.dataset_service.search_datasets(search_query)

        # Assert that the result is a list containing the first dataset
        self.assertEqual(result, [datasets[0]])

    def test_multi_field_search(self):
        datasets = [
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
                "period": "20240203",
                "schema_version": "v2",
                "survey_id": 5678,
                "published_at": "2022-02-01T00:00:00",
            }
        ]

        # Create a list of Dataset objects from the dictionaries
        datasets = DatasetFactory.from_list_of_dicts(datasets)

        # Search with multiple fields
        search_query = "20220201 5678"
        result = self.dataset_service.search_datasets(search_query)

        # Assert that the result is a list containing the first dataset
        self.assertEqual(result, [datasets[1]])

