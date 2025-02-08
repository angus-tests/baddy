from dataclasses import dataclass
from typing import Optional


class AppStatus:
    """
    A class that represents the status
    of an app in the SDX system
    """
    HEALTHY = "healthy"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "unknown"


@dataclass
class SDXApp:
    """
    A class that represents an app
    in the SDX system
    """
    slug: str
    app_name: str
    version: str
    status: AppStatus
    description: Optional[str] = None

    def __str__(self):
        return self.app_name
