"""Package metadata/info"""

from jsonc2json._jsonc2json import __build_profile__, __version_lib__

__all__ = (
    "__build_profile__",
    "__description__",
    "__title__",
    "__version__",
    "__version_lib__",
)
__title__ = "jsonc2json"
__description__ = "strip comments from JSONC (JSON with comments)"
__version__ = __version_lib__
