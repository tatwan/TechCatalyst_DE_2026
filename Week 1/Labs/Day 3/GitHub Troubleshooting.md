## Updating you .gitignore



* Make sure to include all your `venv` related python environments that you created. If you used `pyhton -m venv <some env>` list that environment folder inside the `.gitignore`:

```
# Ignore Jupyter Notebook checkpoints
**/.ipynb_checkpoints/

# macOS system files
.DS_Store
.gitignore

# VSCode settings
.vscode/


# Ignore all .env files anywhere in the repo
**/.env

# Ignore all .cfg files anywhere in the repo
**/*.cfg

# Ignore backup files any where 
**/*.bkp

# Ignore my virtual envionments 
dev2/
devpy/
MyWork/
Class Work/
```

* The error message **"fatal: refusing to merge unrelated histories"** happens when Git detects that the local repository and the remote repository (in this case, on GitHub) do not share a common commit history

  * You can force Git to merge the histories by adding the `--allow-unrelated-histories` flag to your pull command:

    ```
    git pull origin main --allow-unrelated-histories
    ```

  * Git will attempt to merge the two histories.

  * If there are overlapping files or directories, you may encounter merge conflicts that you'll need to resolve manually.

  * After fixing any conflicts, add the resolved files and complete the merge with:

    ```
    git add .
    git commit
    ```

* To **find conflicts after a `git pull`**, follow these steps:

  * After a conflicted `git pull`, running `git status` will clearly list all files with conflicts. You'll see something like:

    ```
    On branch main
    You have unmerged paths.
    (fix conflicts and run "git commit")
    (use "git merge --abort" to abort the merge)
    
    Unmerged paths:
      (use "git add <file>..." to mark resolution)
        both modified:   somefile.py
    
    ```

  * **Open the conflicted files**
    Each conflicted file will contain special conflict markers in the code:

    - `<<<<<<< HEAD` shows your branch's changes.
    - `=======` separates the changes.
    - `>>>>>>> branch-name` shows the incoming changes from the branch you're merging in.

    For example:

    ```
    <<<<<<< HEAD
    your changes here
    =======
    incoming changes here
    >>>>>>> branch-name
    
    ```

    Search for `<<<<<<<` in your files to jump to each conflict

* **Other helpful commands for investigating conflicts:**

  * `git diff` shows the differences between branches or commits, including areas of conflict.
  * `git log --merge` lists commits that are causing the conflict