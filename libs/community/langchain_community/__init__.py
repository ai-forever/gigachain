"""Main entrypoint into package."""
<<<<<<< HEAD

from importlib import metadata

# Check that we have gigachain_core package instead of langchain_core
from langchain_core.__gigachain_core import _check_gigachain_core_version

# Проверяем, что мы используем именно gigachain_core
_check_gigachain_core_version()

=======
from importlib import metadata

>>>>>>> langchan/master
try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)
