r"""jsonc2json ~ convert JSONC strings/bytes to JSON strings/bytes

Examples:
    Here is a jsonc string with block comments, line comments, and hash comments:
    >>> JSONC_STRING = '''
    ... {
    ...     "name": /* full */ "John Doe",
    ...     "age": 43,
    ...     "phones": [
    ...         "+44 1234567", // work phone
    ...         "+44 2345678"  // home phone
    ...     ]  # hash comment
    ... }
    ... '''.strip()
    >>> print(JSONC_STRING)
    {
        "name": /* full */ "John Doe",
        "age": 43,
        "phones": [
            "+44 1234567", // work phone
            "+44 2345678"  // home phone
        ]  # hash comment
    }

    jsonc2json defaults to stripping all comments

    >>> from jsonc2json import jsonc2json
    >>> json_string = jsonc2json(JSONC_STRING)
    >>> json_string_lines = json_string.splitlines(keepends=True)
    >>> from pprint import pprint
    >>> pprint(json_string_lines)
    ['{\n',
     '    "name":            "John Doe",\n',
     '    "age": 43,\n',
     '    "phones": [\n',
     '        "+44 1234567",              \n',
     '        "+44 2345678"               \n',
     '    ]                \n',
     '}']

    Now the json string is parseable

    >>> from json import loads
    >>> loads(json_string)
    {'name': 'John Doe', 'age': 43, 'phones': ['+44 1234567', '+44 2345678']}

    if we give jsonc2json a bytes object, it will return a bytes object (typing.AnyStr)
    >>> json_bytes = jsonc2json(JSONC_STRING.encode())
    >>> isinstance(json_bytes, bytes)
    True

"""

from __future__ import annotations

from typing import AnyStr
from ._jsonc2json import jsonc2json_bin, jsonc2json_str, __version_lib__

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

    """
    if isinstance(jsonc, bytes):
        return jsonc2json_bin(jsonc)
    return jsonc2json_str(jsonc)
