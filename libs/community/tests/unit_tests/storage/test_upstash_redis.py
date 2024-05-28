<<<<<<< HEAD
"""Light weight unit test that attempts to import UpstashRedisStore."""

=======
"""Light weight unit test that attempts to import UpstashRedisStore.
"""
>>>>>>> langchan/master
import pytest


@pytest.mark.requires("upstash_redis")
def test_import_storage() -> None:
    from langchain_community.storage.upstash_redis import UpstashRedisStore  # noqa
