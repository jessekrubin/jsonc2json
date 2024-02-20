from __future__ import annotations
from typing import List, Optional
import sys
from ._jsonc2json import __version_lib__, jsonc2json_bin


def main(args: Optional[List[str]] = None) -> int:
    argv = args or sys.argv[1:]
    if argv:
        last_arg_lower = argv[-1].lower()
        if last_arg_lower == "-h" or last_arg_lower == "--help":
            sys.stdout.write(
                f"jsonc2json-v{__version_lib__}\nUsage: python -m jsonc2json < input.json(c) > output.json"
            )
            return 0
        if last_arg_lower == "-v" or last_arg_lower == "--version":
            sys.stdout.write(__version_lib__)
            return 0

    stdin_bytes = sys.stdin.buffer.read()
    sys.stdout.buffer.write(jsonc2json_bin(stdin_bytes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
