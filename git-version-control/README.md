---
noteId: "9da44990487111f19b2df1139983349d"
tags: []

---

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
  * [Git Cheat Sheet](https://git-scm.com/docs/git-cheat-sheet)
  * [Installing-Git](https://git-scm.com/install/mac)

**First Time Git Configuration**

Before you can start using Git, you need to configure it. Run each of the following lines on the command line to make sure everything is set up.

* sets up Git with your name

```bash
git config --global user.name "<Your-Full-Name>"
```

* sets up Git with your email

```bash
git config --global user.email "<your-email-address>"
```

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

1. You can create a local directory and turn it into a Git repository or You can take a local directory that is currently not under version control, and turn it into a Git repository
2. Clone an existing remote repository on your local machine

We begin with **method 1**.

Create a new project directory:

```bash
mkdir esme_ml
cd esme_ml
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
echo "training ml model" > README.md
```

Check status:

```bash
git status
```

You will see **README.md** under **Untracked files** — meaning Git sees it but is not tracking it yet.

---

## **2.2 Staging Changes**

To start tracking the change on file:

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

Record the snapshot (Record changes to the local repository):

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
Let’s change a file that was already tracked. If you change a previously tracked file called README.md.

```bash
echo "chose the best ml model after training" >> README.md
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
git commit -m "Update README"
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

c

`README.log` no longer appears — Git ignores it.

Track the `.gitignore` file:

```bash
git add .gitignore
git commit -m "Add .gitignore file"
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

* **git rm** : removes file from staging *and deletes it locally* 
* **git rm --cached** : untracks file *but keeps it locally*

## **Example**

### 6.1 Create files

```bash
touch README.ML.md README.DL.md README.LLM.md
git add README.ML.md README.DL.md README.LLM.md
git commit -m "Add ML, DL, LLM files"
```

### 6.2 Removing files

To remove a file from Git, you have to remove it from your **tracked files (more accurately, remove it from your staging area)** and then commit. 

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

### 6.3 Remove a file with `git rm`

```bash
git rm README.DL.md
git commit -m "Remove README.DL.md"
```

### 6.4 Untrack a file using git rm --cached

This is particularly useful if you forgot to add something to your .gitignore file

```bash
git rm --cached README.ML.md
git commit -m "Stop tracking README.ML.md"
```

---

# **7. Viewing Commit History**

After you have created several commits, or if you have cloned a repository with an existing commit history, you’ll probably want to look back to see what has happened. 
See commit history:

```bash
git log
```

Show changes for each commit:

```bash
git log -p
```

Show statistics for files modified in each commit:

```bash
git log --stat
```

prints each commit on a single line, which is useful if you’re looking at a lot of commits.

```bash
git log --oneline
```

Display an ASCII graph of the branch and merge history beside the log output.

```bash
git log --graph
```
---

# **8. Working With Remote Repositories**

Remote repositories are stored on platforms like GitHub, GitLab, etc... To be able to collaborate on any Git project, you need to know how to manage your remote repositories. 
Remote repositories are versions of your project that are hosted on the Internet 

## **8.1 Listing remotes**

```bash
git remote -v
```

No remote appears yet because this repository was created with `git init`.

---

## **8.2 Adding a Remote**

After creating a GitHub repository, connect it:

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

* **`git pull`** : *fetch + merge*
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

### **Inspecting a Remote**

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

### **1. Sharing Tags**

By default, `git push` does **not** transfer tags.

Push a single tag:

```bash
git push <remote-name> <tagname>
```
or

Push **all** tags:

```bash
git push <remote-name> --tags
```

---

### **Tip (Optional) : 2. Deleting Tags**

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

## **4. Branching and Merging**

Creating a New Branch called `testing`

```bash
git branch testing
```
Check status:
you can see `master` and `testing` branch pointer to the same commit. But 
How does Git know what branch you’re currently on? It keeps a special pointer called HEAD

```bash
git status
```

Now switch to that branch `testing`, This moves HEAD to point to the `testing` branch.

```bash
git checkout testing
```

Hint: you can create branch and switch directly into branch with one command
```bash
git checkout -b testin`
```

Create a new python file:

## **4.1 Create a python file and write some code**

```bash
touch main.py
```

Stage and commit:

```bash
git add main.py
git  commit -m 'update code main.py'
```

Now switch to that branch `master`, This moves HEAD to point to the `master` branch.

```bash
git checkout master
```

## **4.2 Create a new python test file and write code for testing some code in main module**
touch test_somme.py

Stage and commit:

```bash
git add test_somme.py
git  commit -m 'update code test_somme.py'
```
Check status:

```bash
git status
```

Stage and commit:

```bash
git add main.py
git  commit -m 'update code main.py'
```
Check status:

```bash
git status
```

You can run command below, it will print out the history of your commits, 
showing where your branch pointers are and how your history has diverged.

```bash
git log --oneline --decorate --graph --all 
```

## Github Project: Git Commands Documentation Template:

  * [Project TP ](https://docs.google.com/document/d/1sqDkIJlGH-GRhikZjF2TqWfzBiYF6lPLBJrsLocQu8c/edit?usp=sharing)
  * [data](https://drive.google.com/file/d/18s2hc8oKBIp2A59xWOpVkCC3wHGtThr_/view?usp=sharing)

