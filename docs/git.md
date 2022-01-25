# Git overview
Here are some instructions for working with git and GitHub as we work through our assignments.  Follow directions closely and be careful and methodical with your changes in git -- it can be easy to mess things up. 

## Before your first assignment

----------
1. In the GitHub UI, create a private repository in the wustl-data organization called `assignments-<your_WUSTL_ID>`, substituting your WUSTL ID.

2. Run the following to make your own copy of the "template" (_upstream_) repository and put it on GitHub with the correct permissions set:
    ```bash
    git clone --bare https://github.com/wustl-data/assignments.git
    cd assignments
    git push --mirror https://github.com/wustl-data/assignments-<your_WUSTL_ID>.git
    cd ..
    rm -rf assignments.git
    ```

3. Clone your private version of the repo so you can work on it locally:

    ```bash
    git clone https://github.com/yourname/private-repo.git
    cd private-repo
    ```

4. Add the class repo as a remote repo called `upstream`:

    ```bash
    git remote add upstream https://github.com/wustl-data/assignments.git
    ```

That's it for initial setup.

## Before each assignment

1. Make sure your repository is up to date with all of your local changes using `git status`.  
    - If you have uncommitted code, you'll need to commit or stash the changes using `git stash` before pulling code and switching branches.

2. Run `git fetch upstream` to retrieve the latest branches and commits from the `upstream` branch; these arent merged with your local clone yet though. You can view a list of all your branches with `git branch -v -a`. For each assignment, I will put a new Markdown file in `docs/instructions`, e.g. `hw1.md` for you to fetch.
    > Review this diagram and understand the differences between the `upstream` repo, the `origin` repo, and your local repo:

    ![](https://i.stack.imgur.com/cEJjT.png)

3. Check out the assignment branch using the command `git switch -c hw1 upstream/hw1` where `hw1` can be whatever assignment branch you would like to check out. The `-c` argument creates a local copy of the upstream branch.

4. View the instructions for the assignment. The easiest way to do this is probably by navigating to the `docs` folder in the [upstream repository](https://github.com/wustl-data/assignments/tree/main/docs) on GitHub, but you can also view it directly from VS Code (preview icon in upper right, or Ctrl+Shift+V) or by using `grip` (e.g. `grip docs/instructions/hw1.md`)

5. Work from the assignment branch as you go -- feel free to make additional branches off of this branch if you want to try new things in your code without fear of losing code that works!

## During each assignment

1. Run step 2 in the previous section ("Run `git fetch upstream`...") before every working session to always have the most up to date instructions -- I might even add some helper code for folks to pull down if a lot of people are struggling with a certain aspect of the assignment.
    > More advanced git for the curious: We shouldn't get any [_merge conflicts_](https://docs.microsoft.com/en-us/visualstudio/version-control/git-resolve-conflicts?view=vs-2022) when running a fetch or pull since you shouldn't be editing the `docs` files I provide, and I shouldn't be editing any code you provide. It's common practice (and good practice) to run `git fetch` instead of `git pull` to avoid automatically merging changes that came from the remote repository, however, `git pull` may be used as a shortcut if you're sure about the changes.
    
    > When pulling or fetching remote changes, you might be curious about what exactly has changed about the remote code before you merge it with your code base. Running `git fetch` followed by a `git status` or a `git diff` allows for an easy way for you to do this.  However, if you do run `git fetch` instead of `git pull`, _don't forget to merge the changes_ with `git merge FETCH_HEAD`.

2. Make sure you're on the right branch before you get started: `git branch` to see all your branches and `git checkout <branch name>` to switch branches.

3. Not git-related, but don't forget to activate your virtual environment each session with `poetry shell`, or you will run into `ModuleNotFound` errors.

4. **ABC - Always Be Committing**. Don't forget to make frequent commits so I can retroactively track the progress of your code as you worked on it.

5. For some assignments, I may decide to provide some tests for your code so that you can run your autograder tests locally instead of needing to upload to Gradescope every time you would like to check correctness. To run these tests, simply use the command `pytest`. Of course, regardless of local tests, you may upload to Gradescope at any time--this will help me give you feedback if you need it. Gradescope runs the "official" tests using `pytest` behind the scenes. 
    > Hint: a new passing test is usually a good opportunity to commit your code.

6. If you are running into problems, please post an issue on the [**upstream** repository issue board](https://github.com/wustl-data/assignments/issues). This is where I and your classmates are most likely to see it. If you have sensitive information in your issue or context that would be considered sharing a solution, you may start an issue in your private GitHub repo, but you may need to get my attention by tagging me in GitHub or sending me an email. Open private issues sparingly; you generally should be able to present your issues in an appropriate context.

7. I will suggest leaving your issue open until the assignment is due, even if the issue is resolved, so other students can more easily see the discussion if they have a similar question. However, feel free to close the issue if it feels like clutter.


## Suggesting edits to the upstream repo

If you see an error in the docs that you think could use correction, or would like to share some example code, feel free to make a pull request on the template (upstream) repository.

Use the GitHub UI to create a fork of the upstream repo (the small "Fork" button at the top right of the public repo page). Then:

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
1. On your assignment branch, push your changes to your `origin` repo on GitHub: `git push`
2. Submit your assignment to GradeScope using the GitHub uploader or a .zip of your repository (latter method not tested).


## Why all this git? Isn't this a data science course?
> It is my opinion that version control should be a common skill among _anyone_ writing _any_ amount of code. The benefits are numerous and directly applicable to data manipulation and data management, including but not limited to data integrity, collaboration, and data exploration. Additionally git is ubuquitous in both software engineering and data science and git skills are of high value to potential employers. Getting used to the syntax and the flow of working in git can be frustrating at first, but the benefits will pay off many times over. 
> **That being said**. Please reach out with any git-related headaches and I will gladly walk through them with you. While I hope you will become skilled and confident with git as we go, mistakes will inevitably happen -- debugging these mistakes are not a major focus of this course and I would rather make sure you are spending more time on the data science than figuring out all the intricacies of git.