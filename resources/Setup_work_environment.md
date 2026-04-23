# Python Environment Setup with uv and Jupyter in VS Code

This guide explains how to install **uv**, **Python**, **JupyterLab**, and **VS Code**, and how to run notebooks locally or on a remote server over SSH. It uses **uv** as the default tool for Python environments and package management.

------

## 1. Install uv

`uv` manages Python versions, virtual environments, and project dependencies.

### Windows

Install with PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS / Linux

Install with the official installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal and verify the installation:

```bash
uv --version
```

------

## 2. Install a Python Version with uv

If you do not already have a suitable Python version, install one with `uv`:

```bash
uv python install 3.12
```

To list available or installed versions:

```bash
uv python list
```

------

## 3. Create a Project Environment

### New project folder

To start a new project, create and initialize the folder with `uv init`:

```bash
uv init my_project
cd my_project
```

If you want to choose a specific Python version for the environment, run:

```bash
uv venv --python 3.12
```

This creates a `.venv` directory in the project folder.

Activate it:

```bash
# Linux / macOS
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

You can then install dependencies for the new project with commands such as:

```bash
uv add jupyterlab ipykernel
```

### Existing project folder

If the project folder already exists, first change into that folder:

```bash
cd path/to/project
```

If the folder already contains a `pyproject.toml`, install the project and its dependencies with:

```bash
uv sync
```

`uv sync` creates the environment and installs the package from the project metadata (`pyproject.toml` and `setup.cfg`).

If the folder exists but is not yet initialized as a `uv` project, run:

```bash
uv init
uv venv --python 3.12
```

Then activate the environment:

```bash
# Linux / macOS
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

------

## 4. Set Up Git for the Project Folder

If the project folder is not yet a Git repository, initialize it with:

```bash
git init
```

Create or update a `.gitignore` file so that the local environment and notebook cache files are not committed:

```gitignore
# The python environment created by uv (gets recreated using uv sync on other machines)
.venv/

# Jupyter notebook checkpoints and cache
__pycache__/
.ipynb_checkpoints/
*.pyc

# VS Code settings and workspace files
.vscode/

# macOS system files
.DS_Store
```

Importantly, the `pyproject.toml`, `setup.cfg`, and `uv.lock` (created by uv) files should **not** be ignored, as they contain the project metadata and dependencies, which make it possible to reproduce the environment on other machines.

If your project folder contains large data files, it makes sense to also remove them from git tracking by adding them to `.gitignore`. Large files should be stored and shared separately.

```gitignore
# E.g. data stored in 'data' folder:
data/
```

Stage the files and create the first commit:

```bash
git add .
git commit -m "Initial commit"
```

If you already created an empty repository on GitHub, link it as the remote:

```bash
git remote add origin git@github.com:yourusername/your-repository.git
```

If the default branch should be named `main`, set it explicitly:

```bash
git branch -M main
```

Push the local repository to the remote:

```bash
git push -u origin main
```

If the folder is already a Git repository, you only need to check that `.gitignore` contains the relevant entries, then commit and push your changes as usual.

------

## 5. Install JupyterLab and ipykernel

Inside the project environment, install JupyterLab and the notebook kernel package:

```bash
uv add jupyterlab ipykernel
```

To install packages without changing project metadata, use:

```bash
uv pip install jupyterlab ipykernel
```

To register the environment explicitly as a notebook kernel:

```bash
uv run python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

------

## 6. Install VS Code

- Download: [VS Code](https://code.visualstudio.com/)
- Install extensions:
  - **Python** (Microsoft)
  - **Jupyter** (Microsoft)
  - **Remote - SSH** (Microsoft)

------

## 7. Create and Use a Notebook in VS Code

1. **Open your project folder** in VS Code.
2. **Select interpreter**:
    `Ctrl+Shift+P` → *Python: Select Interpreter* → choose the Python executable from `.venv`.
3. **Create notebook**:
    File → New File → Save as `my_notebook.ipynb`.
4. **Choose kernel**:
    Click the top-right kernel selector → pick the `.venv` interpreter or the kernel you registered with `ipykernel`.

If VS Code does not show the environment immediately, reload the window.

------

## 8. Install Libraries

Add common scientific packages with:

```bash
uv add numpy pandas matplotlib seaborn scipy scikit-learn
```

To install packages temporarily without updating `pyproject.toml`, use:

```bash
uv pip install numpy pandas matplotlib seaborn scipy scikit-learn
```

Inside a notebook, prefer:

```python
%pip install numpy pandas matplotlib seaborn scipy scikit-learn
```

If these packages should remain part of the project setup, add them later with `uv add` in the terminal.

------

## 9. Running Locally

To start JupyterLab in the browser from the project folder:

```bash
uv run jupyter lab
```

Open the URL shown in the terminal, for example `http://localhost:8888`.

------

## 10. Running on a Remote SSH Server

There are two common ways to run Jupyter notebooks on a remote server:

------

### A. VS Code Remote SSH Setup

1. **Open Command Palette**:
    `Ctrl+Shift+P` → *Remote-SSH: Open SSH Configuration File*.
2. **Add your server** configuration:

```ssh-config
Host myserver
     HostName my.server.address
     User myusername
     Port 22
     IdentityFile ~/.ssh/id_rsa
```

1. **Connect to the server**:
    `Ctrl+Shift+P` → *Remote-SSH: Connect to Host* → choose `myserver`.

> After the first connection, you can also use *Remote-SSH: Connect Current Window to Host*.

1. **Install required extensions on the remote** if prompted:
    - **Python**
    - **Jupyter**
2. **Install uv on the remote machine** if it is not already available.
3. **Create or sync the remote environment** in the project folder:

```bash
uv sync
```

1. **Select the remote interpreter** in VS Code:
    Open a notebook → top-right kernel selector → choose the Python interpreter from the remote `.venv`.

The notebook runs on the remote server while you edit and interact with it in VS Code.

------

### B. Run Jupyter via SSH Tunnel

This approach uses a terminal and a local browser instead of VS Code Remote SSH.

#### Step 1: Establish SSH tunnel **from your local machine**

Run **on your local machine**, not the server:

```bash
ssh -L 8888:localhost:8888 myusername@my.server.address
```

- `-L 8888:localhost:8888` forwards server port `8888` to local port `8888`.
- Keep this terminal open while you work.

#### Step 2: Start Jupyter on the **remote server**

On the server:

```bash
# Change into your project directory
cd path/to/your/project

# Create the environment if needed and install dependencies
uv sync

# Start Jupyter Lab on the remote server, no browser
uv run jupyter lab --no-browser --port=8888
```

- `--no-browser` prevents the server from trying to open a browser.
- `--port=8888` ensures the port matches the tunnel you created.

#### Step 3: Open Jupyter locally

1. On your **local machine**, open a browser.
2. Navigate to:

```text
http://localhost:8888
```

1. Enter the token displayed in the server terminal if prompted.

Jupyter runs on the remote server, but you interact with it locally.

------

### Summary of Where Commands Run

| Command                                           | Run on        |
| ------------------------------------------------- | ------------- |
| `ssh -L 8888:localhost:8888 myserver`             | Local machine |
| `uv sync`                                         | Remote server |
| `uv run jupyter lab --no-browser --port=8888`     | Remote server |
| Open browser at `http://localhost:8888`           | Local machine |

------

## 11. Switching Kernels Between Local and Remote

- When connected via **Remote SSH**, VS Code shows remote `.venv` environments in the kernel picker.
- You can run the same `.ipynb` on:
  - a local `uv` environment
  - a remote `uv` environment
  without changing notebook code.
