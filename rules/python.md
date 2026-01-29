# Python Rules

This document outlines the rules and configurations for Python-based projects generated with this template.

This rules inspired from OCA, PEP8, and Odoo best practices.

## Versioning
The project uses a configurable Python version (defaulting to 3.12). The project must have a `.python-version` file with format `major.minor`, for example:
```
3.12
```

## Dependencies
Core dependencies for development and tooling are defined in `requirements.txt`.

### Tooling
- [**pre-commit**](https://pre-commit.com/#installation): Used for managing and reviewing git hooks.
- [**ruff**](https://docs.astral.sh/ruff/installation/): Used for formatting and lint checking.
- [**pylint**](https://pylint.readthedocs.io/en/latest/user_guide/installation/index.html): Used for static code analysis.

## Linting & Formatting
The following tools are used to ensure code quality.

### Ruff
An extremely fast Python linter and code formatter. All of configuration is in the `.ruff.toml` file.

#### `B` (flake8-bugbear)
Detects likely bugs and design problems.
```python
# Bad: Mutable default argument
def add_to(x, list_=[]):
    list_.append(x)
    return list_
```

#### `C90` (mccabe)
Checks code complexity.
```python
# Bad: Function with too high cyclomatic complexity (too many branches)
def complex_function(x):
    if x > 0:
        if x < 10:
            print("x is between 0 and 10")
        else:
            print("x is greater than 10")
    # ... (lots of nested ifs)
```

#### `I` (isort)
Sorts imports.
```python
# Bad
import sys
import os
from my_lib import a
import json

# Good
import json
import os
import sys
from my_lib import a
```

#### `UP` (pyupgrade)
Upgrades syntax to newer Python versions.
```python
# Bad (Python 2 style)
print "Hello"

# Good (Python 3)
print("Hello")
```

#### `W291`
Trailing whitespace.
```python
x = 1 # There is an extra space at the end of this line
```

### Pylint
A static code analyser. All of configuration is in the `.pylintrc` file.

#### Plugins
- `pylint.extensions.docstyle`
- `pylint.extensions.mccabe`
- `pylint-odoo` (with `odoo` stack)

#### `anomalous-backslash-in-string`
Backslash in string that isn't a valid escape.
```python
# Bad
print("C:\Program Files")

# Good
print(r"C:\Program Files")
```

#### `assignment-from-none`
Assigning result of function that returns None.
```python
def my_func():
    print("Hello")

# Bad
x = my_func()
```

#### `dangerous-default-value`
Mutable object as default argument.
```python
# Bad
def fn(arg=[]):
    pass
```

#### `duplicate-key`
Duplicate key in dictionary.
```python
# Bad
my_dict = {"a": 1, "a": 2}
```

#### `eval-used`
Usage of `eval()`.
```python
# Bad (Security risk)
eval("1 + 1")
```

#### `pointless-statement`
Statement that has no effect.
```python
# Bad
1 + 1
```

#### `pointless-string-statement`
String statement that has no effect (and isn't a docstring).
```python
def my_func():
    "This string does nothing"
    return True
```

#### `redundant-keyword-arg`
Passing a keyword argument that is already passed by position.
```python
def func(a): pass
# Bad if called incorrectly showing redundancy (though usually a TypeError)
# Pylint catches specific redundant cases in complex calls.
```

#### `reimported`
Importing a module that is already imported.
```python
import os
# ...
import os # Bad
```

#### `return-in-init`
Returning a value in `__init__`.
```python
class MyClass:
    def __init__(self):
        return 1 # Bad
```

#### `too-few-format-args`
String format called with too few arguments.
```python
# Bad
"{} {}".format(1)
```

#### `unreachable`
Code that cannot be reached.
```python
def my_func():
    return
    print("Unreachable") # Bad
```

#### `trailing-whitespace`
Whitespace at the end of a line.
```python
x = 1 # There is an extra space at the end of this line
```

#### `deprecated-module`
Usage of deprecated modules.
```python
import optparse # Bad (deprecated, use argparse)
```

#### `redefined-builtin`
Redefining a built-in function.
```python
def list(): # Bad
    pass
```

#### `too-complex`
Code complexity check (McCabe).
```python
# Bad: Function with too high cyclomatic complexity (too many branches)
def complex_function(x):
    if x > 0:
        if x < 10:
            print("x is between 0 and 10")
        else:
            print("x is greater than 10")
    # ... (lots of nested ifs)
```

