# Project Git Report

## I. Git Operations Used
The following Git commands were used during the project:

- `git init` – Initialize a new Git repository.  
- `git add <filename>` – Stage files for committing.  
- `git commit -m "message"` – Save staged changes with a description.  
- `git branch <branchname>` – Create a new branch.  
- `git checkout <branchname>` – Switch between branches.  
- `git merge <branchname>` – Combine changes from another branch into the current one.  
- `git tag v2.0` – Create a version tag.  
- `git push origin main` – Upload commits to the remote repository.  
- `git push origin v2.0` – Push a specific tag to the remote.  
- `git log --oneline --graph` – View commit history in a compact tree structure.  

---

## II. Branch Structure and Merge Strategy

- **Main branch:** The primary branch containing stable and tested code.  
- **Feature branch:** Created for new developments to keep the main branch clean.  
- **Merge strategy:**  
  - Used **fast-forward merge** when the main branch had no diverging commits.  
  - Used **recursive merge** (default in Git) when both branches had new commits.  

Example commands:
```bash
git checkout -b feature-update
# make changes
git add .
git commit -m "Add new feature"
git checkout main
git merge feature-update

