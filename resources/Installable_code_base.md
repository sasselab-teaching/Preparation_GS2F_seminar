# Making Your Python Code Installable with setuptools and uv

This guide shows how to structure a Python package so that it can be installed in editable mode and used from local scripts. The packaging examples use `setuptools`, and the workflow examples use `uv` to create environments, install the package, and run code.

See the [Python Environment Management](Python_environment_management.md) guide for more details on how to install uv and how to manage Python environments and dependencies with `uv` and other tools.

Editable installation is useful during development because changes in your source files are available immediately without reinstalling the package after every edit.

------

## 1. Project Structure

Assume the project is called `mypackage`. A minimal structure looks like this:

```text
mypackage/
├── pyproject.toml
├── setup.cfg
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── core.py
├── scripts/
│   └── run_example.py
└── tests/
  └── test_core.py
```

- `src/mypackage/` contains the package code.
- `scripts/` can contain local scripts that import the package.
- `tests/` contains tests.
- `pyproject.toml` and optionally `setup.cfg` define packaging metadata.

------

## 2. Minimal Packaging Configuration

At minimum, `pyproject.toml` needs to declare the build backend:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

You can keep package metadata in `setup.cfg`:

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

This tells setuptools that:

- the package code lives in `src/`
- packages should be discovered automatically
- the project can be built and installed by modern packaging tools

------

## 3. Minimal Working Example

### Example files

`src/mypackage/__init__.py`

```python
from .core import hello
```

`src/mypackage/core.py`

```python
def hello(name: str) -> str:
  return f"Hello, {name}!"
```

`scripts/run_example.py`

```python
import mypackage

print(mypackage.hello("World"))
```

------

## 4. Create the Environment with uv

From the project root:

```bash
uv venv --python 3.12
```

This creates a local `.venv` directory for the project.

If `uv` needs to install that Python version first, you can do that explicitly:

```bash
uv python install 3.12
```

------

## 5. Install the Package in Editable Mode

There are two common ways to work with this project using `uv`.

### Option A: Explicit editable install

Install the current package into the environment in editable mode:

```bash
uv pip install -e .
```

This is the direct `uv` equivalent of `pip install -e .`.

### Option B: Project-based workflow with `uv sync`

If your project dependencies are declared in `pyproject.toml`, you can synchronize the project environment with:

```bash
uv sync
```

For many modern projects, this is the cleaner default workflow.

------

## 6. Test the Installation

You can verify that the package is importable by running Python inside the project environment:

```bash
uv run python
```

Then test the package:

```python
import mypackage
mypackage.hello("World")
```

The package should import successfully, and changes in `src/mypackage/` should be visible immediately because the install is editable.

------

## 7. Run Local Scripts with uv

One advantage of `uv` is that you can run scripts inside the project environment without manually activating it first.

For a local script file:

```bash
uv run python scripts/run_example.py
```

For a package module:

```bash
uv run python -m mypackage.core
```

This is useful because:

- the correct project environment is used automatically
- imports from your package work consistently
- the workflow is the same across different machines

If you prefer, you can still activate the environment manually and run scripts in the traditional way, but `uv run` is usually simpler.

------

## 8. Add Dependencies

If your package needs dependencies, you can declare them in `setup.cfg`:

```ini
[options]
install_requires =
  requests
  numpy>=1.20
```

Or, in a more modern project layout, you can keep them in `pyproject.toml` under `[project].dependencies`.

With a `uv` workflow, you can also add dependencies directly from the command line:

```bash
uv add requests numpy
```

This updates the project metadata and keeps the environment in sync.

------

## 9. Modern `pyproject.toml` Example

Instead of splitting configuration across `pyproject.toml` and `setup.cfg`, you can put the package metadata directly into `pyproject.toml`.

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
description = "A modern example package"
authors = [
  { name = "Your Name", email = "you@example.com" }
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
```

With this setup, editable installation still works:

```bash
uv pip install -e .
```

And a project-based workflow still works:

```bash
uv sync
```

------

## 10. Summary

- Use `setuptools` metadata to make the package installable.
- Use `uv venv` to create a local environment.
- Use `uv pip install -e .` for an explicit editable install.
- Use `uv sync` for a modern project-based workflow.
- Use `uv run` to execute local scripts and modules inside the correct environment.

This is a practical workflow for package development, testing, and running local analysis or utility scripts from the same code base.
