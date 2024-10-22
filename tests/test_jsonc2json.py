from pathlib import Path
import json
import jsonc2json as jsonc2json
import pytest

REPO_ROOT = Path.cwd()

JSONC_STRING = """
{
    "name": /* full */ "John Doe",
    "age": 43,
    "phones": [
        "+44 1234567", // work phone
        "+44 2345678"  // home phone
    ]  # hash comment
}
""".strip()

EXPECTED_JSON_DATA = {
    "name": "John Doe",
    "age": 43,
    "phones": ["+44 1234567", "+44 2345678"],
}


def test_version():
    assert jsonc2json.__version__ is not None
    import tomli

    Path("Cargo.toml").read_text()
    pyproject_toml = tomli.loads(Path("Cargo.toml").read_text())
    cargo_version = pyproject_toml["package"]["version"]
    assert jsonc2json.__version__ == cargo_version
    # pyproject_version = tomli.loads(Path("pyproject.toml").read_text())["project"][
    #     "version"
    # ]
    # assert jsonc2json.__version__ == pyproject_version


def test_jsonc2json_string():
    data = REPO_ROOT.joinpath("_data", "sample.json").read_text()
    stripped = jsonc2json.jsonc2json(data)

    loaded = json.loads(stripped)
    assert loaded
    assert isinstance(loaded, dict)


def test_jsonc2json_bytes():
    # with open("sample.json", "rb") as f:
    # data = f.read()
    data = REPO_ROOT.joinpath("_data", "sample.json").read_bytes()
    stripped = jsonc2json.jsonc2json_bin(data)
    assert isinstance(stripped, bytes)
    string = stripped.decode("utf-8")
    assert isinstance(string, str)
    loaded = json.loads(stripped)
    assert loaded
    assert isinstance(loaded, dict)


def test_jsonc2json_simple() -> None:
    jsonstr = jsonc2json.jsonc2json(JSONC_STRING)
    assert json.loads(jsonstr) == EXPECTED_JSON_DATA


def test_invalid_json():
    jsonstr = "/* foo "
    with pytest.raises(ValueError):
        _stripped = jsonc2json.jsonc2json(jsonstr)
    with pytest.raises(ValueError):
        _stripped = jsonc2json.jsonc2json(jsonstr.encode("utf-8"))


@pytest.mark.skip("TODO")
def test_strip_whitespace():
    raise NotImplementedError("TODO")


def test_dev():
    pass
