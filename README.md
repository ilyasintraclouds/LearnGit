# Learn Git

This repository is a hands-on guide to learning Git from the basics to advanced concepts like branching, workflows, and automation.

---

## 📌 1. Repository Setup

### Initialize a Git Repository

```bash
git init
```

**Purpose:**
Initializes a new Git repository in the current directory.

---

### Connect to Remote Repository

```bash
git remote add origin <repo-url>
```

**Purpose:**
Links your local repository to a remote repository.

**Flags:**

* `origin` → Default name for the remote repository

---

### Check Connected Remotes

```bash
git remote -v
```

**Purpose:**
Displays the remote repositories linked to your project.

**Flags:**

* `-v` → Shows URLs along with remote names

---

## 📌 2. Basic Workflow

### Check Repository Status

```bash
git status
```

**Purpose:**
Shows the current state of the working directory and staging area.

---

### Add Files to Staging Area

```bash
git add <file>
```

**Purpose:**
Stages specific files for commit.

```bash
git add .
```

**Purpose:**
Stages all changes in the current directory.

---

### Commit Changes

```bash
git commit -m "message"
```

**Purpose:**
Saves a snapshot of staged changes.

**Flags:**

* `-m` → Adds a commit message inline

---

### Rename Branch to Main

```bash
git branch -M main
```

**Purpose:**
Renames the current branch to `main`.

**Flags:**

* `-M` → Forces rename (overwrites if needed)

---

### Push to Remote Repository

```bash
git push -u origin main
```

**Purpose:**
Uploads local commits to the remote repository.

**Flags:**

* `-u` → Sets upstream, so future pushes can use just `git push`

---

## 📌 3. Key Concepts

### Working Directory

Where you make changes to files.

### Staging Area

Where changes are prepared before committing.

### Repository

Where Git stores the complete history of your project.

---

## 📌 4. Learning Progress

* [x] Initialize repository
* [x] Connect to GitHub
* [x] First commit
* [ ] Branching
* [ ] Merging
* [ ] Rebasing
* [ ] Git Workflows
* [ ] GitHub Actions

---

## 📌 Notes

* Always write meaningful commit messages
* Commit small, logical changes
* Use branches for new features

---

## 🚀 Next Step

Learn how Git tracks changes internally and understand staging vs committing in depth.
