from dashboards.interfaces.sdx.sdx_app_repository_interface import (
    SDXAppRepositoryInterface,
)
from dashboards.interfaces.service import Service


class HealthService(Service):
    """
    Service class for fetching health information for SDX
    """

    def __init__(self, sdx_app_repository: SDXAppRepositoryInterface):
        self.sdx_app_repository = sdx_app_repository

    def get_all_apps(self):
        """
        Get all apps.
        :return: A list of SDXApp objects.
        """
        return self.sdx_app_repository.get_all()
