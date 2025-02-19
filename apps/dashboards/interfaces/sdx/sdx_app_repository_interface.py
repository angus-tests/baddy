from abc import ABC, abstractmethod

from apps.dashboards.dto.sdx.sdx_app import SDXApp


class SDXAppRepositoryInterface(ABC):
    """
    Interface that defines the methods that must be implemented
    for an SDX App repository.
    """

    @abstractmethod
    def get_by_slug(self, slug: str) -> SDXApp:
        """
        Get a sds by its ID.
        :param slug: A unique identifier for the app.
        :return: The SDXApp object.
        """
        pass

    @abstractmethod
    def get_all(self) -> list[SDXApp]:
        """
        Get all SDX apps.
        :return: list of SDXApp objects.
        """
        pass
