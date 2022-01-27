# Git overview
Here are some instructions for working with git and GitHub as we work through our assignments.  Follow directions closely and be careful and methodical with your changes in git -- it can be easy to mess things up. 

For some it may be useful to have a GUI interface for GitHub -- I hear good things about [GitHub Desktop](https://desktop.github.com/). If you find yourself struggling to keep pace with git concepts, the app might be useful. If you can, however, try to get back to (or stick with) the command line -- building your command line skills will allow you to write code faster and more precisely. See our [Resources](./resources.md) page for some helpful articles and tutorials.

## Before your first assignment

----------
1. In the GitHub UI, create a private repository in the wustl-data organization called `assignments-<your_WUSTL_name>`, substituting your WUSTL login name.

2. Run the following to make your own copy of the class "template" (_upstream_) repository `assignments` and put it on GitHub with the correct permissions:
    > Don't forget to substitute http links with SSH links if you set up your git credentials with SSH.
    ```
    git clone --bare https://github.com/wustl-data/assignments.git
    cd assignments.git
    git push --mirror https://github.com/wustl-data/assignments-<your_WUSTL_name>.git
    cd ..
    ```
    Delete your local cache of the repo:
    ```
    rm -rf assignments.git 
    ```

3. Clone your private version of the repo so you can work on it locally:

    ```
    git clone https://github.com/wustl-data/assignments-<your_WUSTL_name>.git
    cd assignments-<your_WUSTL_name>
    ```

4. Add the class repo as a remote repo called `upstream`:

    ```
    git remote add upstream https://github.com/wustl-data/assignments.git
    ```

That's it for initial setup.

> Note: you may want to subscribe to the upstream repo by clicking "watch" at the top of the repo and setting your notifications settings to your liking. 

## Before each assignment

1. Make sure your repository is up to date with all of your local changes using `git status`.  
    - If you have uncommitted code, you'll want to commit or stash the changes using `git stash` before pulling code and switching branches.

2. Get the new assignment by merging from upstream
    1. Run `git fetch upstream` to retrieve the latest branches and commits from the `upstream` branch; these arent merged with your local clone yet though. You can view a list of all your branches with `git branch -v -a`. For each assignment, I will put a new Markdown file in `docs/assignments` named e.g. `hw1.md` for you to fetch.
        > Review this diagram and understand the differences between the `upstream` repo, the `origin` repo, and your local repo:

        ![](https://i.stack.imgur.com/cEJjT.png)
    
    2. (Optional) Examine the changes to the repository to your satisfaction for a given branch by running:
        ```
        git log main..upstream/main
        git log main..upstream/hw1
        ```
        which shows the commit messages of the changes, or:
        ```
        git diff main upstream/main
        git diff main upstream/hw1
        ```
        which shows the line-by-line diff of the changes.
    3. (not optional) Merge the changes with `git merge upstream/main`/`git merge upstream/hw1`. In the unfortunate circumstance that you run into any merge conflicts at this step, try to resolve them but reach out for help if you need to.

    > If you'd like to condense these commands into one, you can run `git pull upstream` which will automatically merge changes. Use with caution.


3. Check out the assignment branch using the command `git switch -c hw1 upstream/hw1` where `hw1` can be whatever assignment branch you would like to check out. The `-c` argument creates a local copy of the upstream branch.

4. View the assignment. One way to view is to open the `docs/assignments` folder in the [upstream repository](https://github.com/wustl-data/assignments/tree/main/docs/assignments) on GitHub, but you can also view it directly from VS Code (preview icon in upper right, or Ctrl+Shift+V) or by using `grip` (e.g. `grip docs/assignments/hw1.md`) to start a rendering server (view the markdown in the browser, and open a new terminal while the server runs). 

5. Work from the assignment branch as you go -- feel free to make additional branches off of this branch if you want to try new things in your code without fear of losing code that works!

## During each assignment

1. Run step 2 in the previous section ("Run `git fetch upstream`...") before every working session to always have the most up to date instructions -- I might even add some helper code for folks to pull down if a lot of people are struggling with a certain aspect of the assignment.

2. Make sure you're on the right branch before you get started: `git branch` to see all your branches and `git checkout <branch name>` to switch branches.

3. Not git-related, but don't forget to activate your virtual environment each session with `poetry shell`, or you will run into `ModuleNotFound` errors. Run `exit` to quit the virtual environment.

4. **ABC - Always Be Committing**. Don't forget to make frequent commits so I can retroactively track the progress of your code as you worked on it.

5. For some assignments, I may decide to provide some tests for your code so that you can run your autograder tests (or other tests) locally instead of needing to upload to Gradescope every time you would like to check correctness. To run these tests, simply use the command `pytest`. Of course, regardless of local tests, you may upload to Gradescope at any time--this will help me give you feedback if you need it. Gradescope runs the "official" tests using `pytest` behind the scenes. 
    > Hint: a new passing test is usually a good opportunity to commit your code.

6. If you are running into problems or have questions about an assignment, please post an issue on the [**upstream** repository issue board](https://github.com/wustl-data/assignments/issues). This is where I and your classmates are most likely to see it. If you have sensitive information in your issue or context that would be considered sharing a solution, you may start an issue in your private GitHub repo, but you may need to get my attention by tagging me in GitHub or sending me an email. Open private issues sparingly; you generally should be able to present your issues in an appropriate context.

7. I will suggest leaving your issue open until the assignment is due, even if the issue is resolved, so other students can more easily see the discussion if they have a similar question. However, feel free to close the issue if it feels like clutter.


## Suggesting edits to the upstream repo

If you see an error in the docs that you think could use correction, or would like to share some example code, feel free to make a pull request on the template (upstream) repository.

Use the GitHub UI to create a fork of the upstream repo (the small "Fork" button at the top right of the public repo page). Then (in pseudo-pseudocode):

```
git clone https://github.com/yourname/the-fork.git
cd the-fork
git remote add private_repo_yourname https://github.com/yourname/private-repo.git
git checkout -b pull_request_yourname
git pull private_repo_yourname main
git push origin pull_request_yourname
```

Now you can create a pull request via the Github UI for the upstream repo.

## After each assignment
1. On your assignment branch, push your changes to your `origin` repo on GitHub:
    ```
    git push
    ```
2. Submit your assignment to GradeScope using the GitHub uploader or a .zip of your repository (latter method not tested).


## Why all this git? Isn't this a data science course?
> Version control should be a common skill among _anyone_ writing _any_ amount of code. The benefits are numerous and directly applicable to data manipulation and data management, including but not limited to data integrity, collaboration, and data exploration. Additionally git is ubuquitous in both software engineering and data science and git skills are of high value to potential employers. Getting used to the syntax and the flow of working in git can be frustrating at first, but the benefits will pay off many times over. 
> **That being said**. Please reach out with any git-related headaches and I will gladly walk through them with you. While I hope you will become skilled and confident with git as we go, mistakes will inevitably happen -- debugging these mistakes are not a major focus of this course and I would rather make sure you are spending more time on the data science than figuring out all the intricacies of git.
