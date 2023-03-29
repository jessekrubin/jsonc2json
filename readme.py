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
