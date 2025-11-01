# Python Environment Setup & Jupyter in VS Code (Local + Remote)

This guide covers installing **Miniconda/Mamba**, **JupyterLab**, and **VS Code**, creating notebooks, installing libraries, and running them locally or via SSH on a remote server. It now includes steps to make Conda the default Python.

------

## 1️⃣ Install Miniconda or Mamba

### Step 1a: Install Miniconda

```bash
# Linux/Mac
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

During installation:

- Press `Enter` to read through the license.
- Type `yes` to accept the license.
- Press `Enter` to confirm the installation location (or choose custom path).
- **Important**: When asked **"Do you wish the installer to initialize Miniconda3 by running conda init?"**, type `yes`.

Then:

```bash
# Restart terminal or source your shell config
source ~/.bashrc   # or source ~/.zshrc if using zsh
```

------

### Step 1b: Install Mamba (optional, faster Conda)

After installing Miniconda:

```bash
conda install -n base -c conda-forge mamba
```

Or install **Mambaforge** directly (includes Mamba by default):

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
bash Mambaforge-Linux-x86_64.sh
```

------

### Step 1c: Make Conda/Mamba Your Default Python

1. Initialize Conda for your shell (if you didn’t do this during installation):

```bash
conda init
```

1. Restart your terminal.
2. Verify that Conda is active by default:

```bash
conda info
python --version
```

You should see `base` environment activated automatically and Python pointing to Conda’s installation.

> ⚠️ If you want to **disable auto-activation** of the base environment later, you can run:
>
> ```bash
> conda config --set auto_activate_base false
> ```

------

## 2️⃣ Create a Conda Environment (Recommended)

```bash
# Example: create Python 3.12 environment named 'myenv'
conda create -n myenv python=3.12
conda activate myenv
```

------

## 3️⃣ Install JupyterLab

Inside your environment:

```bash
mamba install jupyterlab
# or
conda install jupyterlab
# or via pip
pip install jupyterlab
```

------

## 4️⃣ Install VS Code

- Download: [VS Code](https://code.visualstudio.com/)
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
    Click top-right kernel selector → pick your environment.

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

Instead of using VS Code, you can also start JupyterLab in the browser:

```bash
jupyter lab
```

Open the URL shown in your terminal (e.g., `http://localhost:8888`).

------

## 8️⃣ Running on a Remote SSH Server

When working with a remote server, you have two main ways to run Jupyter notebooks:

------

### A. VS Code Remote SSH Setup (Recommended)

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

> ⚡ Tip: After the first connection, you can also choose `Remote-SSH: Connect Current Window to Host` to open the current VS Code window on the server.

1. **Install required extensions on the remote** if prompted:
   - **Python**
   - **Jupyter**
2. **Select remote interpreter** in VS Code:
   - Open a notebook → top-right kernel selector → choose a **remote Conda environment**.

Now, your notebook runs **entirely on the remote server**, but you can edit and interact with it locally in VS Code.

------

### B. Run Jupyter via SSH Tunnel (Manual Method)

This is the “classic” approach without VS Code remote, using the terminal and browser.

#### Step 1: Establish SSH tunnel **from your local machine**

Run **on your local machine**, not the server:

```bash
ssh -L 8888:localhost:8888 myusername@my.server.address
```

- `-L 8888:localhost:8888` forwards the server's port `8888` to your local machine's port `8888`.
- Keep this terminal open while you work.

#### Step 2: Start Jupyter on the **remote server**

On the server (after logging in via SSH):

```bash
# Activate your Conda environment
conda activate myenv

# Start Jupyter Lab on the remote server, no browser
jupyter lab --no-browser --port=8888
```

- `--no-browser` prevents it from trying to open a browser on the remote server.
- `--port=8888` ensures the port matches the tunnel you created.

#### Step 3: Open Jupyter locally

1. On your **local machine**, open a browser.
2. Navigate to:

```
http://localhost:8888
```

1. Enter the token displayed in the server terminal if prompted.

> ✅ Result: You’re now running Jupyter on the remote server but interacting with it locally, as if it were running on your machine.

------

### Summary of Where Commands Run

| Command                                 | Run on        |
| --------------------------------------- | ------------- |
| `ssh -L 8888:localhost:8888 myserver`   | Local machine |
| `conda activate myenv`                  | Remote server |
| `jupyter lab --no-browser --port=8888`  | Remote server |
| Open browser at `http://localhost:8888` | Local machine |

------

This approach is helpful if:

- You **don’t want to install VS Code remotely**.
- You want to **use the browser interface** instead of VS Code notebooks.

------

## 9️⃣ Switching Kernels Between Local & Remote

- When connected via **Remote SSH**, VS Code will show **remote Conda environments** in the *Select Kernel* dropdown.
- You can run the same `.ipynb` on:
  - Local Conda env
  - Remote Conda env
     without changing code.

------

✅ **Result**: You now have a fully working setup for Python, Jupyter, and VS Code, both locally and remotely, with Conda/Mamba as your default Python and easy environment management.

------

