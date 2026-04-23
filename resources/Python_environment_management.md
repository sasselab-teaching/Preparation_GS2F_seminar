# Managing Python Packages and Environments

This document introduces three common ways to manage Python packages and isolated project environments:

- `pip` together with `venv` or `virtualenv`
- `conda` or `mamba`
- `uv`

All three approaches are useful. They differ mainly in scope, speed, and how much they manage beyond Python packages.

------

## 1. Overview

### `pip` + virtual environments

- `pip` is the standard package manager for Python.
- It installs packages from the Python Package Index (PyPI).
- It does not manage environments by itself, so it is usually paired with `venv` or `virtualenv`.
- This is a common and lightweight setup for general Python development.
- It is ideal for containerized (docker) environments as it introduces minimal additional dependencies and where you have control over the container's Python version.

### `conda` / `mamba`

- `conda` is a package manager, dependency manager, and environment manager.
- `mamba` is a faster reimplementation of the dependency solver and package installer for the Conda ecosystem.
- These tools can manage Python packages and non-Python dependencies such as compiled libraries.
- They are widely used in data science, machine learning, and scientific computing.
- This is especially useful if you are managing environments that contain Python and R code together or if you need to manage complex dependencies that are easier to install from `conda-forge`.

### `uv`

- `uv` is a fast Python package and environment manager.
- It can install Python versions, create virtual environments, and manage project dependencies.
- It works well with modern Python project layouts based on `pyproject.toml`.
- It is increasingly used as a faster alternative to `pip` + `venv` for many Python-only workflows.
- For purely Python based projects, `uv` is ideal because of its speed and the robust reproducibility of environments it creates, when moving between machines or sharing with collaborators.
- While `pip` + `venv` usually depends on the Python version installed on the system, `uv` can manage multiple Python versions and create environments with specific versions, which can be very useful for testing or when working on projects that require different Python versions.

------

## 2. Scope and Package Sources

| Tool | Main package source | Environment management | Non-Python dependencies |
| ---- | ------------------- | ---------------------- | ----------------------- |
| `pip` + `venv` | PyPI | Yes, with `venv` or `virtualenv` | Limited |
| `conda` / `mamba` | Anaconda channels, `conda-forge`, adding PyPI packages through pip is also possible | Built in | Good |
| `uv` | PyPI | Built in | Limited |

In practice:

- `pip` and `uv` are mainly focused on Python packages.
- `conda` and `mamba` can also manage external compiled dependencies more directly.
- `uv` and `pip` often fit best when a project is defined in `pyproject.toml` and mostly depends on Python packages from PyPI.

------

## 3. Installing the Tools

### Installing `pip` + `venv`

`pip` and `venv` usually come with a standard Python installation.

- Install Python from [python.org](https://www.python.org/downloads/) if it is not already available.
- On Windows, make sure Python is added to `PATH` during installation.
- Verify the installation with:

```bash
python --version
pip --version
```

If `venv` is available, you can create environments with:

```bash
python -m venv .venv
```

### Installing `conda` / `mamba`

To use `conda` or `mamba`, you usually start by installing a Conda distribution.

- **Miniconda** is a minimal Conda installation that includes Python and `conda`.
- **Miniforge** is a minimal Conda-based distribution that is configured around `conda-forge` and commonly used in open-source scientific Python workflows. It also comes with `mamba` pre-installed.
- `mamba` can be installed into an existing Conda setup and used as a faster drop-in replacement for many `conda` install commands.

Typical setup options:

- Install **Miniconda** if you want a small Conda installation with the standard Conda tooling. You can obtain it from [anaconda.com](https://www.anaconda.com/docs/getting-started/miniconda/install/overview).
- Install **Miniforge** if you want a lightweight Conda setup centered on `conda-forge`. You can obtain it from the [conda-forge github repository](https://github.com/conda-forge/miniforge).

After installation, verify the setup with:

```bash
conda --version
```

If you want to add `mamba` to an existing Conda installation:

```bash
conda install -n base -c conda-forge mamba
```

Then verify it with:

```bash
mamba --version
```

### Installing `uv`

Install `uv` with the official installer.

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On macOS / Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify the installation with:

```bash
uv --version
```

`uv` can also install Python versions if needed:

```bash
uv python install 3.12
```

------

## 4. Side-by-Side Example

Assume you want to set up a project with:

- Python 3.10
- NumPy, Pandas, Matplotlib
- Jupyter
- plotly-express (only available from PyPI)

### A. `pip` + `venv`

```bash
# Create an environment
python -m venv my_env

# Activate it on Linux / macOS
source my_env/bin/activate

# Activate it on Windows PowerShell
my_env\Scripts\Activate.ps1

# Install packages
pip install numpy pandas matplotlib jupyter plotly-express

# Start Jupyter
jupyter notebook
```

Typical strengths:

- simple and widely available
- good for standard Python projects

Typical limitations:

- dependency resolution can be slower or less convenient
- large scientific stacks may require more manual troubleshooting

### B. `conda` / `mamba`

```bash
# Create an environment
conda create -n my_env python=3.10

# Activate it
conda activate my_env

# Install packages available from conda channels ('-c conda-forge' defines the channel to search for packages)
conda install -c conda-forge numpy pandas matplotlib jupyter
# Install packages only available from PyPI
pip install plotly-express

# Start Jupyter
jupyter notebook
```

If `mamba` is installed, you can replace `conda install` with:

```bash
mamba install -c conda-forge numpy pandas matplotlib jupyter
```

Typical strengths:

- good support for scientific and compiled dependencies
- reliable for mixed dependency stacks

Typical limitations:

- environments are often larger and dependency-solving can be very slow on complex environments (though `mamba` is much faster than `conda`)
- workflows can feel heavier for small Python-only projects

### C. `uv`

```bash
# Create and enter a project folder
uv init my_project
cd my_project

# Create an environment with a specific Python version
uv venv --python 3.10

# Install packages
uv add numpy pandas matplotlib jupyter plotly-express

# Start Jupyter (uv run automatically activates the environment for the command)
uv run jupyter notebook
```

Typical strengths:

- fast environment creation and package installation
- good fit for modern Python projects

Typical limitations:

- focused mainly on Python packages from PyPI
- less suitable when you need many non-Python system dependencies managed for you

------

## 5. Common Commands

### Commands for `pip` + `venv`

```bash
# Create environment
python -m venv .venv

# Activate on Linux / macOS
source .venv/bin/activate

# Activate on Windows PowerShell
.venv\Scripts\Activate.ps1

# Install a package
pip install numpy

# Save dependencies
pip freeze > requirements.txt
```

### Commands for `conda` / `mamba`

```bash
# Create environment
conda create -n myenv python=3.12

# Activate environment
conda activate myenv

# Install a package
conda install -c conda-forge numpy

# List environments
conda env list
```

### Commands for `uv`

```bash
# Initialize a project
uv init my_project

# Enter the project folder
cd my_project

# Create environment
uv venv --python 3.12

# Install a package
uv add numpy

# Run a command inside the environment
uv run python
```

------

## 6. Making Environments Reproducible

To make a project reproducible, the environment definition should be stored together with the source code. In practice, this means that the relevant dependency files should be committed to Git and shared through the same repository as the code, for example on GitHub.

This makes it easier for:

- collaborators who want to run the same code
- you on a different machine
- you returning to the project later

### Reproducibility with `pip` + `venv`

With `pip` + `venv`, a common approach is to freeze the currently installed packages into a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Someone else can then recreate the environment with:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activation would be:

```powershell
.venv\Scripts\Activate.ps1
```

The `requirements.txt` file should be saved alongside the code and committed to the repository.

The major drawback of `pip` + `venv` is that the `requirements.txt` file does not capture the Python version or non-Python dependencies, which can also lead to issues with dependency resolution if the environment is recreated at a later time or on a different machine.

### Reproducibility with `conda` / `mamba`

With `conda` or `mamba`, a common approach is to export the environment to an `environment.yml` file:

```bash
conda env export > environment.yml
```

Someone else can then recreate the environment with:

```bash
conda env create -f environment.yml
conda activate my_env
```

If the environment name inside `environment.yml` should be ignored, it can also be created with a custom name:

```bash
conda env create -n my_new_env -f environment.yml
```

The `environment.yml` file should be saved alongside the code and committed to the repository.

The environment file captures the Python version, the packages (whether installed through conda/mamba or pip), and their versions, which makes it easier to reproduce the same environment later on another machine.

### Reproducibility with `uv`

With `uv`, the project dependencies are automatically recorded in `pyproject.toml`. In addition uv creates a `uv.lock` file, which is used to pin exact resolved versions of packages and their dependencies for stronger reproducibility.

After adding dependencies with `uv add`, the project metadata is updated automatically:

```bash
uv add numpy pandas matplotlib
```

The relevant files to keep are:

- `pyproject.toml` for the declared project dependencies
- `uv.lock`, created by uv when calling `uv sync` and updated by uv when dependencies change, for pinned dependency resolution

Someone else can then recreate the environment with:

```bash
uv sync
```

The `pyproject.toml` file, and usually also `uv.lock`, should be saved alongside the code and committed to the repository.

The `pyproject.toml` file captures the Python version and declared dependencies, and `uv.lock` captures the exact resolved versions, which makes it easier to reproduce the same environment later on another machine.

### Recommendation

Whatever tool you use, keep the environment definition files in the same Git repository as the code.

Typical files are:

- `requirements.txt` for `pip` + `venv`
- `environment.yml` for `conda` / `mamba`
- `pyproject.toml` and `uv.lock` for `uv`

Without these files, other people cannot easily reproduce your setup, and you may also have trouble recreating the same environment later on another machine.

------

## 7. Summary Table

| Feature | `pip` + `venv` | `conda` / `mamba` | `uv` |
| ------- | -------------- | ----------------- | ---- |
| Main focus | Standard Python packaging | Environments plus broader dependency management | Fast Python packaging and environments |
| Package source | PyPI | Conda channels and optionally PyPI | PyPI |
| Environment creation | Separate step with `venv` | Built in | Built in |
| Python version management | External | Built in through Conda environments | Built in |
| Non-Python dependencies | Limited | Strong | Limited |
| Speed | Standard | Good, `mamba` is faster than `conda` | Very fast |
| Good default for | Small to medium Python projects | Scientific stacks with compiled dependencies | Modern Python projects using PyPI |

------

## 8. Practical Recommendation

For most teaching projects in this course:

- use `uv` for pure Python environments and package installation
- use `pip` + `venv` if you want the most standard minimal workflow
- use `conda` or `mamba` when you depend on packages that are easier to install from `conda-forge` or when non-Python dependencies matter

The most important point is that each project should use an isolated environment and a clearly documented dependency setup.
