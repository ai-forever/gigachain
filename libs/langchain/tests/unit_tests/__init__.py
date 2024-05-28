"""All unit tests (lightweight tests)."""
<<<<<<< HEAD

=======
>>>>>>> langchan/master
from typing import Any


def assert_all_importable(module: Any) -> None:
    for attr in module.__all__:
        getattr(module, attr)
