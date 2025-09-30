# **Terminal Quick Reference**

~~~md
# Terminal & Remote Access Quick Reference

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
~~~

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