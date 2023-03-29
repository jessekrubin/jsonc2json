from pathlib import Path
import json
import jsonc2json as jsonc2json
import pytest

PWD = Path(__file__).parent
REPO_ROOT = PWD.parent


def test_version():
    assert jsonc2json.__version__ is not None
    import tomli

    Path("Cargo.toml").read_text()
    cargo_version = tomli.loads(Path("Cargo.toml").read_text())["package"]["version"]
    assert jsonc2json.__version__ == cargo_version
    pyproject_version = tomli.loads(Path("pyproject.toml").read_text())["project"][
        "version"
    ]
    assert jsonc2json.__version__ == pyproject_version


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


def test_invalid_json():
    jsonstr = "/* foo "
    with pytest.raises(ValueError):
        _stripped = jsonc2json.jsonc2json(jsonstr)
    with pytest.raises(ValueError):
        _stripped = jsonc2json.jsonc2json(jsonstr.encode("utf-8"))


def test_dev():
    pass
