# Jinja2 Rules

This document outlines the rules and configurations for Jinja2 templates generated with this template.

## Dependencies
Core dependencies for development and tooling are defined in `requirements.txt`.

### Tooling
- [**j2lint**](https://github.com/aristanetworks/j2lint?tab=readme-ov-file#getting-started): Used for linting Jinja2 templates.

## Linting
The linter runs via pre-commit on files with `.j2`, `.jinja2`, or `.jinja` extensions.

### Rules

#### `S0` - `jinja-syntax-error`
Ensures valid Jinja2 syntax.
```jinja2
{# Bad #}
{% if condition %
{{ value }}
{% endif %}

{# Good #}
{% if condition %}
{{ value }}
{% endif %}
```

#### `S1` - `single-space-decorator`
Requires single space between curly brackets and variable name.
```jinja2
{# Bad #}
{{value}}
{{  value  }}

{# Good #}
{{ value }}
```

#### `S2` - `operator-enclosed-by-spaces`
Operators must be enclosed by spaces.
```jinja2
{# Bad #}
{{ my_value|to_json }}
{{ a+b }}

{# Good #}
{{ my_value | to_json }}
{{ a + b }}
```

#### `S3` - `jinja-statements-indentation`
Enforces proper indentation for nested statements (4 spaces).
```jinja2
{# Bad #}
{% if condition %}
{% if nested %}
{{ value }}
{% endif %}
{% endif %}

{# Good #}
{% if condition %}
    {% if nested %}
        {{ value }}
    {% endif %}
{% endif %}
```

#### `S4` - `jinja-statements-single-space`
Requires single space after `{%` and before `%}`.
```jinja2
{# Bad #}
{%if condition %}
{% endif%}

{# Good #}
{% if condition %}
{% endif %}
```

#### `S5` - `jinja-statements-no-tabs`
Indentation must use spaces, not tabs.
```jinja2
{# Bad - using tabs #}
{% if condition %}
	{{ value }}
{% endif %}

{# Good - using 4 spaces #}
{% if condition %}
    {{ value }}
{% endif %}
```

#### `V1` - `jinja-variable-lower-case`
Variables must use lowercase characters.
```jinja2
{# Bad #}
{{ MyVariable }}
{{ CONSTANT_VALUE }}

{# Good #}
{{ my_variable }}
{{ constant_value }}
```

#### `V2` - `jinja-variable-format`
Multi-word variables must use underscores as separators.
```jinja2
{# Bad #}
{{ myVariable }}
{{ my-variable }}

{# Good #}
{{ my_variable }}
```

## Inline Rule Disabling
Rules can be disabled inline using comments:
```jinja2
{# j2lint: disable=S1 #}
{{value}}

{# j2lint: disable=V1 #}
{{ MyVariable }}
```

