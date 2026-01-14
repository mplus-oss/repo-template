# JavaScript / TypeScript Rules

This document outlines the rules and configurations for JavaScript and TypeScript-based projects generated with this template.

This rules inspired from Airbnb best practices.

## Versioning
The project supports configurable Node.js and Bun versions. Version files will be created based on configuration:
- `.node-version` - Node.js version (e.g., `22.0.0`)
- `.bun-version` - Bun version (e.g., `1.1.0`)

## Dependencies
Core dependencies for development and tooling are defined in `package.json`.

### Tooling
- [**biome**](https://biomejs.dev/guides/manual-installation/): Used for formatting and lint checking.

## Linting & Formatting
All configuration is in the `biome.json` file.

### Formatter Settings
- **Indent Style**: Spaces (2 spaces)
- **Line Width**: 100 characters
- **Line Ending**: LF
- **Quote Style**: Single quotes (`'`) for JS, double quotes (`"`) for JSX
- **Trailing Comma**: All
- **Semicolons**: Always

### Style Rules

#### `noVar`
Disallows the use of `var` declarations.
```javascript
// Bad
var name = 'John';

// Good
const name = 'John';
let count = 0;
```

#### `useConst`
Requires `const` for variables that are never reassigned.
```javascript
// Bad
let name = 'John';
console.log(name);

// Good
const name = 'John';
console.log(name);
```

#### `useTemplate`
Enforces template literals instead of string concatenation.
```javascript
// Bad
const greeting = 'Hello, ' + name + '!';

// Good
const greeting = `Hello, ${name}!`;
```

#### `useBlockStatements`
Requires block statements for control flow.
```javascript
// Bad
if (condition) doSomething();

// Good
if (condition) {
  doSomething();
}
```

#### `noParameterAssign`
Disallows reassigning function parameters.
```javascript
// Bad
function process(data) {
  data = data.trim();
  return data;
}

// Good
function process(data) {
  const trimmed = data.trim();
  return trimmed;
}
```

#### `useSelfClosingElements`
Enforces self-closing syntax for components without children.
```jsx
// Bad
<Component></Component>

// Good
<Component />
```

### Suspicious Rules

#### `noDoubleEquals`
Disallows `==` and `!=` in favor of strict equality.
```javascript
// Bad
if (value == null) { }
if (x != y) { }

// Good
if (value === null) { }
if (x !== y) { }
```

#### `noAssignInExpressions`
Disallows assignment expressions in non-assignment contexts.
```javascript
// Bad
if (x = getValue()) { }

// Good
const x = getValue();
if (x) { }
```

#### `noArrayIndexKey` (warning)
Warns against using array indices as React keys.
```jsx
// Bad (warning)
items.map((item, index) => <Item key={index} />);

// Good
items.map((item) => <Item key={item.id} />);
```

### Complexity Rules

#### `useLiteralKeys`
Enforces literal keys over computed expressions when possible.
```javascript
// Bad
const obj = { ['key']: value };

// Good
const obj = { key: value };
```

### Correctness Rules

#### `noUnusedVariables`
Disallows unused variables.
```javascript
// Bad
const unusedVar = 'hello';
function doWork() {
  return 'done';
}

// Good
function doWork() {
  return 'done';
}
```

#### `useHookAtTopLevel`
Enforces React Hooks rules - hooks must be called at the top level.
```jsx
// Bad
function Component({ condition }) {
  if (condition) {
    const [state, setState] = useState(0); // Hook inside condition
  }
  return <div />;
}

// Good
function Component({ condition }) {
  const [state, setState] = useState(0);
  if (condition) {
    // use state here
  }
  return <div />;
}
```

### Accessibility Rules

#### `useAltText`
Requires `alt` attribute on img elements.
```jsx
// Bad
<img src="photo.jpg" />

// Good
<img src="photo.jpg" alt="A scenic mountain view" />
```

#### `useKeyWithClickEvents` (warning)
Warns when click events lack corresponding keyboard events.
```jsx
// Bad (warning)
<div onClick={handleClick} />

// Good
<div onClick={handleClick} onKeyDown={handleKeyDown} role="button" tabIndex={0} />
```

#### `useValidAnchor`
Enforces valid anchor elements.
```jsx
// Bad
<a>Click here</a>
<a href="#">Click here</a>

// Good
<a href="/page">Click here</a>
<button onClick={handleClick}>Click here</button>
```

### TypeScript-Specific Rules (Overrides)

These rules apply only to `.ts`, `.tsx`, `.mts`, and `.cts` files.

#### `useConsistentArrayType` (warning)
Enforces shorthand array type syntax.
```typescript
// Bad (warning)
const items: Array<string> = [];

// Good
const items: string[] = [];
```

#### `noExplicitAny` (warning)
Warns against using `any` type.
```typescript
// Bad (warning)
function process(data: any) { }

// Good
function process(data: unknown) { }
function process(data: string) { }
```
