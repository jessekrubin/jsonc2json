# globsters

python & rust globsters

glob + lobster + rs (rs) = globsters

```python
from globsters import globster

# single
matcher_1 = globster("**/*.py")

assert matcher_1("foo/bar/baz.py")  # True
assert not matcher_1("foo/bar/baz.pyc")  # False

# single case insensitive
matcher_2 = globster("**/*.py", case_insensitive=True)
assert matcher_2("foo/bar/baz.PY")  # True

# multi (also works with negation)
matcher_3 = globster(["*.py", "*.txt"])
assert matcher_3("foo/bar/baz.py")  # True
assert matcher_3("foo/bar/baz.txt")  # True
assert not matcher_3("foo/bar/baz.pyc")  # False

# multi negation (also works with case insensitive)
matcher_4 = globster(["*.py", "!*.pyc"])
assert matcher_4("foo/bar/baz.py")  # True
assert not matcher_4("foo/bar/baz.pyc")  # False

```
"# jsonc2json-dev" 
"# jsonc2json-dev" 
