from typing import Any

from apps.dashboards.dto.sdx.sdx_app import SDXApp


class SDXAppFactory:
    """
    Factory class for creating SDX App Objects
    """

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SDXApp:
        """Creates a SDXApp from a dictionary."""
        return SDXApp(
            slug=data["slug"],
            name=data["name"],
            version=data["version"],
            status=data["status"],
            description=data.get("description", None),
        )
