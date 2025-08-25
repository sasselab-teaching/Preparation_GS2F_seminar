# 📦 Making Your Python Code Pip-Installable with setuptools

You want to make a Python package that you can install in **editable mode** with:

```bash
pip install -e .
```

This is super useful when you’re developing, because changes you make in your source code are reflected immediately without re-installing.

------

### 1. Project Structure

Let’s say your project is called `mypackage`. A minimal structure looks like this:

```
mypackage/
├── pyproject.toml
├── setup.cfg        # optional but recommended
├── setup.py         # optional if pyproject.toml is used fully
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── core.py
└── tests/
    └── test_core.py
```

- `src/mypackage/` contains your actual package code.
- `tests/` is where you keep tests.
- `pyproject.toml` and/or `setup.cfg` define the packaging metadata.

------

### 2. `pyproject.toml` (modern way)

At minimum, you need this so pip knows to use `setuptools`:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

------

### 3. `setup.cfg` (recommended for metadata)

Instead of putting everything in `setup.py`, you can declare package metadata here:

```ini
[metadata]
name = mypackage
version = 0.1.0
author = Your Name
description = A small example package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/yourusername/mypackage
license = MIT

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.8

[options.packages.find]
where = src
```

This tells setuptools:

- Package code lives in `src/`
- Discover packages automatically
- Works with modern pip

------

### 4. `setup.py` (only needed for legacy/compatibility)

You can add a very minimal `setup.py` if you want, but with `setup.cfg` + `pyproject.toml` it’s optional:

```python
from setuptools import setup

setup()
```

------

### 5. Install in Editable Mode

From your project root (where `pyproject.toml` is):

```bash
pip install -e .
```

- `-e` = editable mode
- The `.` = current directory

Now if you open a Python shell:

```python
import mypackage
mypackage.__file__
```

It should point to your `src/mypackage` folder.

------

### 6. (Optional) Add Dependencies

If your package has dependencies, add them in `setup.cfg`:

```ini
[options]
install_requires =
    requests
    numpy>=1.20
```

Then when you `pip install -e .`, those will be installed too.

------

✅ That’s it! You now have a pip-installable, editable package.

Perfect — let’s do it in **two stages**:

------

# 🔹Minimal Working Example

Here’s the *smallest* setup that works with `pip install -e .`.

### Directory Layout

```
mypackage/
├── pyproject.toml
├── setup.cfg
└── src/
    └── mypackage/
        ├── __init__.py
        └── core.py
```

### `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

### `setup.cfg`

```ini
[metadata]
name = mypackage
version = 0.1.0
description = A minimal example package
author = Your Name
license = MIT

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.8

[options.packages.find]
where = src
```

### `src/mypackage/__init__.py`

```python
from .core import hello
```

### `src/mypackage/core.py`

```python
def hello(name: str) -> str:
    return f"Hello, {name}!"
```

------

### 🚀 Try it out

From inside `mypackage/`:

```bash
pip install -e .
```

Then open Python:

```python
>>> import mypackage
>>> mypackage.hello("World")
'Hello, World!'
```

That’s the **minimal editable install** working! 🎉

------

# 🔹 `pyproject.toml` (PEP 621 Style)

`pyproject.toml` is the modern standard for packaging metadata.
 Instead of spreading config across `setup.cfg` + `setup.py`, you can declare everything directly in TOML.

------

### Example: Modern `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
description = "A modern example package using PEP 621"
authors = [
    { name="Your Name", email="you@example.com" }
]
license = { text = "MIT" }
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests",
    "numpy>=1.20"
]

[project.optional-dependencies]
dev = ["pytest", "black", "mypy"]

[project.urls]
Homepage = "https://github.com/yourusername/mypackage"
Documentation = "https://yourdocs.example.com"
```

------

### 🔍 Breakdown

- **`[build-system]`**
  - Tells pip which build backend to use (setuptools here).
  - Required in *every* `pyproject.toml`.
- **`[project]`**
  - Core metadata (name, version, description, authors, license).
  - `requires-python` declares compatibility.
  - `dependencies` installs runtime deps automatically.
- **`[project.optional-dependencies]`**
  - Extras you can install with `pip install .[dev]`.
- **`[project.urls]`**
  - Links for PyPI and docs.

------

### ✅ Editable Install Still Works

Even with PEP 621 metadata:

```bash
pip install -e .
```

No `setup.cfg` or `setup.py` required. (`setup.py` is only for backwards compatibility now.)

------

👉 So:

- **Minimal approach** → `pyproject.toml` + `setup.cfg`.
- **Modern approach** → just `pyproject.toml` (PEP 621).