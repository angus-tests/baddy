from dashboards.meta.singleton_meta import SingletonMeta


class Service(metaclass=SingletonMeta):
    """
    Base class for services

    Services are responsible for implementing the business logic of the application
    and are singletons
    """

    pass
