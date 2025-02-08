from faker import Faker

from dashboards.factories.sdx.sdx_app_factory import SDXAppFactory
from dashboards.interfaces.sdx.sdx_app_repository_interface import SDXAppRepositoryInterface
from dashboards.models.sdx.sdx_app import SDXApp, AppStatus


class FakeSDXAppRepository(SDXAppRepositoryInterface):
    """
    A repository that will generate fake sdx apps.
    """

    def __init__(self):
        self.fake = Faker()
        self.number_of_apps = 5

        self.app_data = [
            {
                "slug": "sdx-testy",
                "app_name": "SDX-Testy",
                "version": "0.3.2",
                "status": "healthy",
                "description": "A test app for the SDX system"
            },
            {
                "slug": "sdx-paul",
                "app_name": "SDX-Paul",
                "version": "6.6.6",
                "status": "unhealthy",
                "description": "A performance testing app for the SDX system"
            },
            {
                "slug": "sdx-survey",
                "app_name": "SDX-Survey",
                "version": "0.9.10",
                "status": "healthy",
                "description": "App for controlling surveys in the SDX system"
            },

        ]

    def get_by_slug(self, slug: str) -> SDXApp:
        """
        Get an SDX app by its slug.
        :param slug:
        :return:
        """
        for app in self.app_data:
            if app["slug"] == slug:
                return SDXAppFactory.from_dict(app)
        raise ValueError(f"App with slug {slug} not found")

    def get_all(self) -> list[SDXApp]:
        """
        Get all SDX apps.
        :return:
        """
        return [SDXAppFactory.from_dict(app) for app in self.app_data]


