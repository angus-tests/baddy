from django.core.cache import cache


class CacheService:
    """
    This class is a service class that handles all the caching operations.
    """

    @staticmethod
    def get(key: str):
        """
        Fetch an item from the cache
        """
        return cache.get(key)

    @staticmethod
    def set(key: str, value, timeout=300):
        """
        Set an item in the cache
        :param key: The key to assign to the value
        :param value: data to be stored in the cache
        :param timeout: The time in seconds to store the value in the cache
        """
        cache.set(key, value, timeout)

    @staticmethod
    def delete(key: str):
        """
        Delete an item from the cache
        """
        cache.delete(key)
