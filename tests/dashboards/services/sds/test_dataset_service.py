from unittest.mock import MagicMock
from django.test import TestCase

from apps.dashboards.factories.sds.dataset_factory import DatasetFactory
from apps.dashboards.interfaces.sds.dataset_repository_interface import (
    DatasetRepositoryInterface,
)
from apps.dashboards import DatasetService


class TestDatasetService(TestCase):
    def setUp(self):
        """Set up test data once for all test cases."""
        self.fake_dataset_repository = MagicMock(spec=DatasetRepositoryInterface)
        self.dataset_service = DatasetService(self.fake_dataset_repository)

        # Common dataset mock
        dataset_dicts = [
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
            },
        ]
        self.datasets = DatasetFactory.from_list_of_dicts(dataset_dicts)
        self.fake_dataset_repository.get_all.return_value = self.datasets

    def test_basic_search(self):
        """Test search by dataset ID."""
        result = self.dataset_service.search_datasets(
            search_query="0a4e5b70-a6d9-44a3-b510-ab53c7fee39f"
        )
        self.assertEqual(result, [self.datasets[0]])

    def test_multi_field_search(self):
        """Test search across multiple fields."""
        result = self.dataset_service.search_datasets(search_query="20220201 5678")
        self.assertEqual(result, [self.datasets[1]])

    def test_search_version(self):
        """Test search by schema version."""
        result = self.dataset_service.search_datasets(search_query="v2")
        self.assertEqual(result, [self.datasets[1], self.datasets[2]])
