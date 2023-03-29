from __future__ import annotations

from typing import AnyStr
from .libjsonc2json import jsonc2json_bin, jsonc2json_str, __version_lib__

__version__ = __version_lib__
__all__ = (
    "__version__",
    "jsonc2json",
    "jsonc2json_bin",
    "jsonc2json_str",
)


def jsonc2json(jsonc: AnyStr) -> AnyStr:
    """Convert JSONC string/bytes to JSON string/bytes

    Args:
        jsonc (AnyStr): JSONC string/bytes

    Returns:
        AnyStr: JSON string/bytes

    Examples:
        >>> jsonc2json('{"foo": "bar"}')
        '{"foo": "bar"}'
        >>> jsonc2json(b'{"foo": "bar"}')
        '{"foo": "bar"}'

    """
    if isinstance(jsonc, bytes):
        return jsonc2json_bin(jsonc)
    return jsonc2json_str(jsonc)
