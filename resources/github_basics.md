# **Git & GitHub Basics — Setup and Workflow Guide**

## **1. Install Git**

Download and install Git from:
🔗 [https://git-scm.com/downloads](https://git-scm.com/downloads)

After installation, configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## **2. Create a GitHub Account**

Sign up at:
🔗 [https://github.com/](https://github.com/)

---

## **3. Set up SSH for GitHub (recommended for pushing without entering passwords)**

### a) Check for existing SSH keys:

```bash
ls -al ~/.ssh
```

### b) Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

Press **Enter** for defaults, and set a passphrase if desired.

### c) Start the SSH agent and add your key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### d) Add the key to GitHub:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the output, go to **GitHub → Settings → SSH and GPG keys → New SSH key**, paste it, and save.

### e) Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

## **4. Clone a Repository**

```bash
git clone git@github.com:username/repository.git
```

*(Use the SSH URL from GitHub’s "Code" button.)*

---

## **5. Install a Python Repo Locally with pip**

If the repo has a `setup.py` or `pyproject.toml`, you can install it:

```bash
cd repository
pip install -e .
```

`-e` (editable mode) means changes in the code update immediately without reinstalling.

---

## **6. Basic Git Workflow**

### **a) Check repo status**

```bash
git status
```

### **b) Add changes**

```bash
git add filename.py
# or add all changes:
git add .
```

### **c) Commit changes**

```bash
git commit -m "Descriptive commit message"
```

### **d) Push changes to GitHub**

```bash
git push
```

### **e) Pull latest changes from remote**

```bash
git pull
```

---

## **7. Branching**

Create and switch to a new branch:

```bash
git checkout -b new-feature
```

Switch back to main:

```bash
git checkout main
```

Push the branch:

```bash
git push -u origin new-feature
```

---

## **8. Forking**

If you don’t have write access to a repo:

1. Click **Fork** on GitHub to create your own copy.
2. Clone your fork:

   ```bash
   git clone git@github.com:yourusername/repository.git
   ```
3. Make changes, commit, push, then open a Pull Request to the original repo.

---

## **9. Summary Table — Common Commands**

| Action           | Command                           |
| ---------------- | --------------------------------- |
| Clone repo       | `git clone <url>`                 |
| Check status     | `git status`                      |
| Add file(s)      | `git add <file>` / `git add .`    |
| Commit changes   | `git commit -m "message"`         |
| Push to remote   | `git push`                        |
| Pull from remote | `git pull`                        |
| Create branch    | `git checkout -b <branch>`        |
| Switch branch    | `git checkout <branch>`           |
| Merge branch     | `git merge <branch>`              |
| View log         | `git log --oneline --graph --all` |
