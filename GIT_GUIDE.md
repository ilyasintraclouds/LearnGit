# Git Guide

This document contains Git commands, concepts, and explanations with their purpose and flags.

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

### Rename Branch

```bash
git branch -M main
```

**Purpose:**
Renames the current branch to `main`.

**Flags:**

* `-M` → Forces rename

---

### Push to Remote Repository

```bash
git push -u origin main
```

**Purpose:**
Uploads local commits to the remote repository.

**Flags:**

* `-u` → Sets upstream branch

---

## 📌 3. Core Concepts

### Working Directory

Where you actively modify files.

### Staging Area

Intermediate area where changes are prepared before committing.

### Repository

Stores all commits and history.

---

## 📌 4. Branching (To Be Expanded)

### Create a Branch

```bash
git checkout -b <branch-name>
```

**Purpose:**
Creates and switches to a new branch.

---

### Switch Branch

```bash
git checkout <branch-name>
```

**Purpose:**
Switches to an existing branch.

---

## 📌 5. Advanced Commands (To Be Expanded)

### Cherry Pick

```bash
git cherry-pick <commit-hash>
```

**Purpose:**
Apply a specific commit from another branch.

---

### Stash

```bash
git stash
```

**Purpose:**
Temporarily saves uncommitted changes.

```bash
git stash pop
```

**Purpose:**
Restores stashed changes.

---

### Rebase

```bash
git rebase <branch>
```

**Purpose:**
Moves commits to a new base.

---

### Reset

```bash
git reset --hard <commit>
```

**Purpose:**
Resets to a specific commit and removes changes.

---

### Revert

```bash
git revert <commit>
```

**Purpose:**
Creates a new commit that undoes changes.

---

## 🚀 Notes

* Prefer small, meaningful commits
* Avoid using `--hard` unless necessary
* Always pull before pushing in team environments
