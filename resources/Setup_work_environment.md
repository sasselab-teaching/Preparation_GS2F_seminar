# Python Environment Setup & Jupyter in VS Code (Local + Remote)

This guide covers installing **Miniconda/Mamba**, **JupyterLab**, and **VS Code**, creating notebooks, installing libraries, and running them locally or via SSH on a remote server.

------

## 1️⃣ Install Miniconda or Mamba

### Miniconda

```bash
# Linux/Mac
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
# Follow prompts, then restart terminal
```

### Mamba (faster Conda)

```bash
# After installing Miniconda:
conda install -n base -c conda-forge mamba
```

Or install **Mambaforge** directly:

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
bash Mambaforge-Linux-x86_64.sh
```

------

## 2️⃣ Optional: Minimal `.condarc`

Place in `~/.condarc` to default to conda-forge and speed up installs:

```yaml
channels:
  - conda-forge
  - defaults
channel_priority: strict
auto_activate_base: false
```

------

## 3️⃣ Install JupyterLab

```bash
mamba install jupyterlab
# or
conda install jupyterlab
# or
pip install jupyterlab
```

------

## 4️⃣ Install VS Code

- Download: https://code.visualstudio.com/
- Install extensions:
  - **Python** (Microsoft)
  - **Jupyter** (Microsoft)
  - **Remote - SSH** (Microsoft)

------

## 5️⃣ Create & Use a Notebook in VS Code

1. **Select interpreter**:
    `Ctrl+Shift+P` → *Python: Select Interpreter* → choose your Conda/Mamba env.
2. **Create notebook**:
    File → New File → Save as `my_notebook.ipynb`.
3. **Choose kernel**:
    Click top-right kernel selector in notebook → pick your environment.

------

## 6️⃣ Install Libraries

Inside your environment:

```bash
mamba install numpy pandas matplotlib
# or
pip install numpy pandas matplotlib
```

From inside a notebook:

```python
!pip install numpy pandas matplotlib
```

------

## 7️⃣ Running Locally

Start JupyterLab:

```bash
jupyter lab
```

Open browser → go to URL shown.

------

## 8️⃣ Running on a Remote SSH Server

### A. VS Code Remote SSH Setup

1. Open **Command Palette** (`Ctrl+Shift+P`) → *Remote-SSH: Open SSH Configuration File*.

2. Add:

   ```ssh-config
   Host myserver
       HostName my.server.address
       User myusername
       Port 22
       IdentityFile ~/.ssh/id_rsa
   ```

3. **Connect**:
    `Ctrl+Shift+P` → *Remote-SSH: Connect to Host* → select `myserver`.

VS Code will open a remote window. Install the **Python** and **Jupyter** extensions **on the remote** when prompted.

------

### B. Run Jupyter via SSH Tunnel (Manual Method)

```bash
ssh -L 8888:localhost:8888 myserver
```

On the server:

```bash
conda activate myenv
jupyter lab --no-browser --port=8888
```

Locally: open `http://localhost:8888` in browser.

------

## 9️⃣ Switching Kernels Between Local & Remote

- When connected to a remote server via **VS Code Remote SSH**, VS Code will show **remote environments** in the *Select Kernel* dropdown for notebooks.
- You can run the same `.ipynb` file on either:
  - Local Conda env
  - Remote Conda env
     without changing any code.

------

✅ **You now have a fully working setup for Python, Jupyter, and VS Code, both locally and remotely via SSH, with easy environment management via Conda/Mamba.**



