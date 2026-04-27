# **Lab 1 — Git**

## **Overview**

**Git** is a distributed version control system used to track changes in files and coordinate work across teams.
It is essential for **collaborative**, **reproducible**, and **auditable** workflows in **MLOps**, **Data Science**, and **Machine Learning Engineering**.

---

## **Objectives**

By the end of this lab, you will be able to:

* Use core Git operations: **init**, **add**, **commit**, **status**, **diff**, **log**, **rm**, **tag**
* Understand the difference between **untracked**, **unstaged**, **staged**, and **committed** changes
* Explore change history using **git log** and **git diff**
* Configure clean versioning using **.gitignore**
* Connect and work with remote repositories (**GitHub**)
* Push, pull, fetch, and inspect remote branches
* Create, list, and delete Git **tags**

---

## **Prerequisites**

Make sure you have the following installed:

* **Git**
* Resources:

  * [About Git](https://git-scm.com/about)
  * [Git Cheat Sheet]([https://git-scm.com/docs/git-cheat-](https://git-scm.com/docs/git-cheat-) sheet)

---

# **1. Git Basics**

In this first part, you will learn the foundational local Git operations:

* Creating or cloning a repository
* Tracking and staging changes
* Committing snapshots
* Viewing file history
* Ignoring files

---

## **1.1 Creating a Git Repository**

Git allows you to start tracking a project in two ways:

1. Turn a local folder into a Git repository
2. Clone an existing remote repository

We begin with **method 1**.

Create a new project directory:

```bash
mkdir ~/git_basics
cd ~/git_basics
```

---

## **1.2 Checking the Status of a Directory**

Run:

```bash
git status
```

You will see:

```
fatal: not a git repository (or any of the parent directories): .git
```

This is expected — the directory is not yet under version control.

---

## **1.3 Initializing a Git Repository**

To turn the current directory into a Git repository:

```bash
git init
```

A hidden `.git` folder is now created.

Check it:

```bash
ls -la
```

Check the repository status again:

```bash
git status
```

---

# **2. Tracking Files**

## **2.1 Creating and Editing Files**

Create a new file:

```bash
touch README.md
```

Add text:

```bash
echo "MLOps training" > README.md
```

Check status:

```bash
git status
```

You will see **README.md** under **Untracked files** — meaning Git sees it but is not tracking it yet.

---

## **2.2 Staging Changes**

To start tracking the file:

```bash
git add README.md
```

Check status:

```bash
git status
```

Now the file appears under **Changes to be committed** — meaning it is staged.

---

## **2.3 Committing Changes**

Record the snapshot (Record changes to the local repository ):

```bash
git commit -m "Add README file"
```

Check status:

```bash
git status
```

You should see:

```
nothing to commit, working tree clean. This means you have a clean working directory
```

---

# **3. Modifying Tracked Files**

Edit the existing file:

```bash
echo "MLOps Pipeline" >> README.md
```

Check status:

```bash
git status
```

You will see:

* **Changes not staged for commit** → the file was modified
* It must be staged again before committing

Stage and commit:

```bash
git add README.md
git commit -m "Update README with pipeline"
```

---

# **4. Ignoring Files**

Sometimes you want Git to **ignore** certain files (logs, temp files, datasets, artifacts, etc..).

Create files:

```bash
touch .gitignore README.log
echo "log content" > README.log
```

Git sees README.log as untracked.

Add this rule to `.gitignore`:

```bash
echo "*.log" >> .gitignore
```

Check status:

```bash
git status
```

`README.log` no longer appears — Git ignores it.

Track the `.gitignore` file:

```bash
git add .gitignore
git commit -m "Add .gitignore"
```

---

# **5. Viewing Changes**

Modify README.md:

```bash
echo "MLOps uses DevOps principles" >> README.md
```

Check the diff:

```bash
git diff
```

This shows **unstaged changes** : This command compares what is in your working directory with what is in your staging area
The result tells you the changes you’ve made that you haven’t yet staged.

Stage and commit:

```bash
git add README.md
git commit -m "Add DevOps principles note"
```

---

# **6. Removing Files**

Git provides two types of removal:

* **git rm** → removes file from staging *and deletes it locally* 
* **git rm --cached** → untracks file *but keeps it locally*

## **Example**

### 6.1 Create files

```bash
touch README.ML.md README.DL.md README.LLM.md
git add README.ML.md README.DL.md README.LLM.md
git commit -m "Add ML, DL, LLM files"
```

### 6.2 Remove a file manually

```bash
rm README.LLM.md
```

Git detects the deletion:

```bash
git status
```

Stage the deletion:

```bash
git add README.LLM.md
git commit -m "Remove README.LLM.md"
```

### 6.3 Remove a file with git rm

```bash
git rm README.DL.md
git commit -m "Remove README.DL.md"
```

### 6.4 Untrack a file using git rm --cached

```bash
git rm --cached README.ML.md
git commit -m "Stop tracking README.ML.md"
```

---

# **7. Viewing Commit History**

See commit history:

```bash
git log
```

Show changes for each commit:

```bash
git log -p
```

Show stats only:

```bash
git log --stat
```

---

# **8. Working With Remote Repositories**

Remote repositories are stored on platforms like GitHub, GitLab, etc...

## **8.1 Listing remotes**

```bash
git remote -v
```

No remote appears yet because this repository was created with `git init`.

---

## **8.2 Adding a Remote**

After creating a GitHub repository, connect it:
Here is a **clean, clear, and professional** version of your text:

---

To connect your local repository to a remote repository, use:

Follow these steps:

1. Go to your GitHub account and create a **new empty remote repository**.
   (You can name it the same as your local project, but this is optional.)

2. In the repository's **Code** section, copy the **HTTPS URL**
   (or the **SSH URL** if you’ve already configured SSH keys).

3. Add the remote to your local repository using the command below, replacing
   `<remote-name>` (commonly `origin`) and `<remote_url>` with the copied GitHub URL.

If you choose to use an **SSH URL**, make sure you have previously generated an SSH key and added the **public key** to your GitHub account.

```bash
git remote add <remote-name> <remote_url>
```

Verify:

```bash
git remote -v
```

---

## **8.3 Pushing to Your Remote Repository**

To upload your local commits to a remote repository, use:

```bash
git push <remote-name> <branch-name>
```

This command sends your current branch to the specified remote.
Once configured, you can run the same command anytime to push new commits to the server.

---

### **Tip: Fetch Remote Data (Does NOT Merge)**

Git provides two different ways to retrieve updates from a remote repository:

* **`git pull`** → *fetch + merge*
  Automatically downloads remote updates **and merges** them into your current branch.

* **`git fetch`** → *fetch only*
  Downloads remote updates **without merging** or modifying your working directory.

---

To test this, create a new file directly in your remote repository (GitHub), add some text, and commit the change.

**Creating a File Directly in a Remote GitHub Repository**

1. **Go to your repository on GitHub**
   Open your browser and navigate to the GitHub repository where you want to test fetching or pulling changes.

2. **Add a new file**

   * Click the **"Add file"** button.
   * Select **"Create new file"**.

3. **Name your file**

   * Enter a name for the file, for example: `test.txt`.

4. **Add some content**

   * Type any text you like into the editor, e.g., `This is a test file for Git fetch/pull`.

5. **Commit the change**

   * Scroll down to the **"Commit new file"** section.
   * Enter a commit message, e.g., `"Add test.txt for Git fetch/pull demo"`.
   * Choose **"Commit directly to the main branch"** 
   * Click **"Commit new file"**.

6. **Verify the file**

   * After committing, you will see the new file listed in your repository.
   * This file now exists only in the **remote repository**.

---

Now you are ready to **test fetching or pulling this change** to your local repository:


### **1. Download remote data *with automatic merge***
To fetch and merge:
Use:

```bash
git pull <remote-name>
```

This will:

1. Fetch the latest changes
2. Automatically merge the remote branch into your current branch

Or Use 

### **2. Download remote data *without merging***

Use:

```bash
git fetch <remote-name>
```

This retrieves new commits into your remote-tracking branches but does **not** modify your active branch.

If you want to integrate the fetched changes manually, run:

```bash
git merge <remote-name>/<branch-name>
```
---

### **Tip (Optional): Inspecting a Remote**

If you want to see detailed information about a remote (its URL, branches, and tracking status), use:

```bash
git remote show <remote-name>
```

---

### **Tip (Optional): Renaming or Removing a Remote**

**Rename a remote:**

```bash
git remote rename <old-remote-name> <new-remote-name>
```

This will also update all related remote-tracking branch references automatically
(e.g., `old-name/master` becomes `new-name/master`).

---

**Remove a remote:**

If a remote is no longer needed — for example, if the server has moved or a mirror is no longer used — you can remove it with:

```bash
git remote remove <remote-name>
```

or the shorthand:

```bash
git remote rm <remote-name>
```

---
# **9. Tagging**

Git allows you to mark specific points in your project’s history as important. This feature is commonly used to mark **release versions** such as `v1.0`, `v2.0`, and so on.


# **Creating an Annotated Tag**

Use the command:

```bash
git tag -a <tagname> -m "<your tagging message>" <commit-SHA>
```

If you omit the commit SHA, Git will tag the current commit.

You can verify the new tag by running:

```bash
git tag
```

---

# **Tips (Optional)**

### **1. Sharing Tags**

By default, `git push` does **not** transfer tags.

Push a single tag:

```bash
git push <remote-name> <tagname>
```

Push **all** tags:

```bash
git push <remote-name> --tags
```

---

### **2. Deleting Tags**

Delete a local tag:

```bash
git tag -d <tagname>
```

To delete the tag on the remote:

```bash
git push <remote-name> --delete <tagname>
```

---

### **3. Listing Tags**

List all tags:

```bash
git tag -l
```

or:

```bash
git tag --list
```


