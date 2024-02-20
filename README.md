# jsonc2json

python & rust package to strip comments from jsonc strings/bytes

uses: https://docs.rs/json_comments/latest/json_comments/

## Install:

```bash
pip install jsonc2json
```

## Usage:

```python
from jsonc2json import jsonc2json

jsonc_string = """
{
    "name": /* full */ "John Doe",
    "age": 43,
    "phones": [
        "+44 1234567", // work phone
        "+44 2345678"  // home phone
    ]  # hash comment
}
""".strip()

json_string = jsonc2json(jsonc_string)

print(json_string)
# PRINTS:
# {
#     "name":            "John Doe",
#     "age": 43,
#     "phones": [
#         "+44 1234567",
#         "+44 2345678"
#     ]
# }

assert isinstance(json_string, str)
assert isinstance(jsonc2json(jsonc_string.encode()), bytes)
```

## CLI

```bash
# stdin
$ echo '{"a": 1 /* comment */, "b": 2}' | python -m jsonc2json
'{"a": 1              , "b": 2}'
# file (still stdin!)
$ python -m jsonc2json < has-comments.jsonc > no-comments.json
```


## TODO:

- [ ] Add options present in the rust package
- [ ] Clap CLI?
- [ ] build confit
