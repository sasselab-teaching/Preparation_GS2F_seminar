# Basics for using the terminal

## Bash

`bash` is **one of many shells** that can be used in a terminal. Whether `bash` is available or the default depends on your operating system and terminal setup:

------

### 1️⃣ Common Shells

| Shell                                 | Typical OS / Notes                                           |
| ------------------------------------- | ------------------------------------------------------------ |
| **bash** (Bourne Again SHell)         | Default on most Linux distros, available on MacOS. Widely used in tutorials. |
| **zsh** (Z Shell)                     | Default on newer MacOS versions (from Catalina onward). Can run `bash` commands mostly. |
| **sh** (Bourne Shell)                 | Very basic shell, compatible with most scripts.              |
| **fish** (Friendly Interactive Shell) | Optional, user-friendly shell with fancy features, not fully compatible with `bash` scripts. |
| **PowerShell**                        | Default on Windows terminals (modern Windows). Can run bash commands via WSL or Git Bash. |

------

### 2️⃣ How to Check Which Shell You’re Using

In your terminal, type:

```bash
echo $SHELL
```

- `/bin/bash` → bash
- `/bin/zsh` → zsh
- `/usr/bin/fish` → fish
- On Windows: may show PowerShell or WSL path

------

### 3️⃣ Running Bash Commands in Other Shells

- **Most shells** (zsh, sh, even fish with some tweaks) can run `bash` scripts, especially simple ones like `wget`, `bash installer.sh`, etc.
- If a tutorial says `bash install.sh`, and your shell is zsh, you can usually just run the same command:

```bash
bash install.sh
```

- On Windows, you may need:
  - **Git Bash** (bundled with Git for Windows)
  - **WSL (Windows Subsystem for Linux)**

------

✅ **Summary:**
 `bash` is common but **not guaranteed** to be your default shell. Many commands in Python/Conda/Jupyter tutorials assume bash because it’s standard on Linux and MacOS. On Windows, using Git Bash, WSL, or a Linux VM is often necessary to follow bash-based instructions directly.

## Terminal & Remote Access Quick Reference

## 1. Navigating the Terminal
- **`pwd`** – Show current directory.
- **`ls`** – List files and folders.
  - `ls -l` – Detailed list.
  - `ls -a` – Show hidden files.
- **`cd <directory>`** – Change directory.
- **`mkdir <name>`** – Create a new folder.
- **`rm <file>`** – Delete a file.
  - `rm -r <folder>` – Delete a folder recursively.
- **`cp <source> <destination>`** – Copy files or folders.
- **`mv <source> <destination>`** – Move or rename files/folders.

---

## 2. Viewing & Editing Files
- **`cat <file>`** – Show file contents.
- **`less <file>`** – Scroll through file (press `q` to quit).
- **`nano <file>`** – Simple terminal text editor.
- **`vim <file>`** – Advanced text editor.

---

## 3. File Permissions
- **`chmod <mode> <file>`** – Change permissions (e.g., `chmod +x script.sh` to make executable).
- **`chown <user>:<group> <file>`** – Change file ownership.

---

## 4. Running Scripts
- **Bash script**:
  ```bash
  bash script.sh

or make executable:

```bash
chmod +x script.sh
./script.sh
```

- **Python script**:

  ```bash
  python3 script.py
  ```

------

## 5. System Info & Processes

- **`whoami`** – Show logged-in user.
- **`uname -a`** – Show system information.
- **`top`** – Live process monitor.
- **`ps aux`** – List running processes.
- **`kill <PID>`** – Terminate a process by ID.

------

## 6. Connecting to a Remote Server (SSH)

- **Syntax**:

  ```bash
  ssh username@hostname
  ```

- **Example**:

  ```bash
  ssh alice@192.168.1.10
  ```

- Add `-p <port>` for non-default SSH port.

------

## 7. File Transfer

### SFTP (Interactive)

```bash
sftp username@hostname
```

**Common commands**:

- `ls` – List remote files.
- `lcd <path>` – Change local directory.
- `cd <path>` – Change remote directory.
- `get <file>` – Download from remote.
- `put <file>` – Upload to remote.
- `exit` – Quit SFTP.

### SCP (Quick Copy)

```bash
scp file.txt user@host:/remote/path
scp user@host:/remote/path/file.txt ./localpath
```

------

## 8. Downloading from the Internet

- **`curl -O <url>`** – Download file.
- **`wget <url>`** – Download file (if installed).

------

## 9. Safety Tips

- Avoid `sudo` unless absolutely necessary.
- Always double-check paths before using `rm -r`.
- Use **`tab`** for auto-completion.
- Use **↑ / ↓** to scroll through command history.
- Press **Ctrl+C** to stop a running process.