# Odoo Rules

This document outlines the rules and configurations for Odoo-based projects generated with this template.

This rules inspired from OCA, PEP8, and Odoo best practices.

> [!NOTE]
> Since Odoo is built on Python, this document serves as an extension of the [Python Rules](./python.md). All rules defined there also apply to Odoo projects unless explicitly overridden.

## Versioning
The project uses a configurable Python version (defaulting to 3.12). The project must have a `.python-version` file with format `major.minor`, for example:
```
3.12
```

## Dependencies
Core dependencies for development and tooling are defined in `requirements.txt`.

### Tooling
- [**pre-commit**](https://pre-commit.com/#installation): Used for managing and reviewing git hooks.
- [**ruff**](https://docs.astral.sh/ruff/installation/): Used for formatting and lint checking (Python).
- [**pylint**](https://pylint.readthedocs.io/en/latest/user_guide/installation/index.html): Used for static code analysis (Python & Odoo).
- [**biome**](https://biomejs.dev/guides/manual-installation/): Used for formatting and lint checking (JavaScript).

## Linting & Formatting
The following tools are used to ensure code quality.

### Ruff
An extremely fast Python linter and code formatter. All of configuration is in the `.ruff.toml` file.

#### `I` (isort)
Sorts imports with specific sections for Odoo.
```python
# Order: future, standard-library, third-party, odoo, odoo-addons, first-party, local-folder
import os # standard-library
import pandas # third-party
import odoo # odoo
from odoo.addons import base # odoo-addons
from . import models # local-folder
```

### Pylint
A static code analyser. All of configuration is in the `.pylintrc` file.

#### `manifest-required-keys`
Ensures the manifest contains all required keys.
```python
# Bad (__manifest__.py)
{
    "name": "My Module",
}

# Good
{
    "name": "My Module",
    "version": "17.0.1.0.0",
    "license": "LGPL-3",
    "summary": "My Summary",
    "depends": ["base"],
}
```

#### `manifest-author-string`
Ensures author is a string.

#### `manifest-deprecated-key`
Checks for usage of deprecated keys in manifest.

#### `manifest-version-format`
Checks if version format is valid.

#### `manifest-maintainers-list`
Checks if maintainers key is a list.

#### `manifest-data-duplicated`
Checks for duplicate data entries in manifest.

#### `manifest-behind-migrations`
Checks if manifest version is behind migrations.

#### `manifest-external-assets`
Checks for external assets in manifest.

#### `resource-not-exist`
Checks if files defined in manifest exist.

#### `missing-readme`
Checks if README.rst or README.md exists.

#### `missing-odoo-file`
Checks if Odoo file (openerp or odoo) exists.

#### `license-allowed`
Checks if license is allowed.

#### `development-status-allowed`
Checks if development status is allowed.

#### `odoo-addons-relative-import`
Checks relative imports.

#### `sql-injection`
Checks for potential SQL injections.
```python
# Bad
self.env.cr.execute("SELECT * FROM table WHERE name = '" + name + "'")

# Good
self.env.cr.execute("SELECT * FROM table WHERE name = %s", (name,))
```

#### `print-used`
Checks for usage of `print` statement (use logging instead).
```python
# Bad
print("Error occurred")

# Good
_logger.error("Error occurred")
```

#### `method-required-super`
Checks if `super()` is called in methods that require it (e.g., `create`, `write`).
```python
# Bad
def create(self, vals):
    return vals

# Good
def create(self, vals):
    return super().create(vals)
```

#### `translation-required`
Checks if strings are translated.
```python
# Bad
raise UserError("Error")

# Good
raise UserError(_("Error"))
```

#### `translation-contains-variable`
Checks if translation contains variable.

#### `translation-positional-used`
Checks if positional arguments are used in translation.

#### `translation-field`
Checks if translated fields are correct.

#### `translation-format-interpolation`
Checks format interpolation in translation.

#### `translation-fstring-interpolation`
Checks f-string interpolation in translation.

#### `translation-too-few-args`
Checks if too few arguments are passed to translation.

#### `translation-too-many-args`
Checks if too many arguments are passed to translation.

#### `translation-unsupported-format`
Checks if unsupported format is used in translation.

#### `translation-not-lazy`
Checks if translation is not lazy.

#### `attribute-deprecated`
Checks for use of deprecated attributes.

#### `method-compute`
Checks commit/rollback in compute methods.
```python
# Bad
@api.depends('a')
def _compute_a(self):
    self.env.cr.commit()
```

#### `method-search`
Checks naming of search methods.

#### `method-inverse`
Checks naming of inverse methods.

#### `bad-builtin-groupby`
Checks for bad usage of built-in groupby.

#### `category-allowed`
Checks if category is allowed.

#### `consider-merging-classes-inherited`
Checks if inherited classes should be merged.

#### `context-overridden`
Checks if context is overridden properly.

#### `except-pass`
Checks for `except pass` (bare except).

#### `external-request-timeout`
Checks if external requests have a timeout.

#### `invalid-commit`
Checks for invalid commit usage.

#### `invalid-email`
Checks for invalid email format.

#### `missing-return`
Checks if method returns something when expected.

#### `no-raise-unlink`
Checks if unlink raises exception.

#### `no-search-all`
Checks for search without domain (all records).

#### `no-wizard-in-models`
Checks if wizard is defined in models directory.

#### `no-write-in-compute`
Checks if write comes inside compute.

#### `prohibited-method-override`
Checks if prohibited methods are overridden.

#### `renamed-field-parameter`
Checks if field parameter is renamed.

#### `test-folder-imported`
Checks if test folder is imported.

#### `use-vim-comment`
Checks usage of vim comments.

#### `website-manifest-key-not-valid-uri`
Checks validity of website manifest key.

### Biome
Fast formatter and linter for JavaScript. Configuration is in `biome.json`.

#### Formatter Style
The project enforces specific formatting rules:
- **Indentation**: 4 spaces.
- **Line Width**: 120 characters.
- **Quotes**: Double quotes (`"`).
- **Semicolons**: Always.
- **Trailing Commas**: ES5 compatible (objects, arrays, etc.).

#### `style/useTemplate`
Prefer template literals over string concatenation.
```javascript
// Bad
const s = "Hello " + name;

// Good
const s = `Hello ${name}`;
```

#### `style/noDefaultExport` (Warning)
Avoid default exports.
```javascript
// Bad
export default function() {}

// Good
export function myFunc() {}
```

#### `style/useSelfClosingElements` (Warning)
Use self-closing elements when possible.
```javascript
// Bad
<div className="foo"></div>

// Good
<div className="foo" />
```

#### `style/useConst`
Require `const` declarations for variables that are only assigned once.
```javascript
// Bad
let abcd = 1234;
console.log(abcd);

// Good
const abcd = 1234;
console.log(abcd);
```

#### `complexity/useLiteralKeys`
Use dot notation for literal keys.
```javascript
// Bad
obj["key"]

// Good
obj.key
```

#### `complexity/noArguments` (Warning)
Try to reduce the use of keyword `arguments`.
```javascript
// Warning
init() {
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments
    this._super(...arguments);
    this.orm = this.bindService("orm");
}

// Good
init(...args) {
    // Spread the arguments based on the function
    this._super(..args);
    this.orm = this.bindService("orm");
}
```

#### `suspicious/noAssignInExpressions`
Disallow assignments in expressions.
```javascript
// Bad
if (x = y) { }

// Good
x = y;
if (x) { }
```

#### `correctness/noUndeclaredVariables`
Disallow usage of undeclared variables.

#### `correctness/noUnusedVariables` (Warning)
Disallow unused variables.
```javascript
// Bad
const x = 1; // x is never used
```

#### `correctness/noUnusedFunctionParameters` (Off)
Allow unused parameters to maintain explicit visibility of the parent function's signature.
```javascript
// `params` not used. This function overrided from
// SnippetOptionWidget._computeWidgetState(methodName: string, params: any[]): Promise<string | undefined> | string | undefined
_computeWidgetState: function (methodName, params) {
    switch (methodName) {
        case "setSelectedEvents": {
            return this.$target[0].dataset.recordData || "";
        }
    }
    return this._super(...arguments);
}
```

