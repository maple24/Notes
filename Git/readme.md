# Table of contents
- [Table of contents](#table-of-contents)
  - [add more emails](#add-more-emails)
  - [delete file](#delete-file)
  - [diff](#diff)
  - [gitignore](#gitignore)
  - [log](#log)
  - [merge](#merge)
  - [push](#push)
  - [rebase](#rebase)
  - [remote](#remote)
  - [rename remote branch](#rename-remote-branch)
  - [reset vs revert](#reset-vs-revert)
  - [semantic commit messages](#semantic-commit-messages)
  - [status](#status)
  - [stash](#stash)
  - [upstream](#upstream)

## add more emails
The only identity to differ from admin or guest is email address. Say you are pushing codes from company and home, your company email is your default commit account, one way to recognize it as yourself is to add emails to git account.

## delete file
```sh
# If you want to delete a file from remote and locally
git rm 'file name'
git commit -m'message'
git push -u origin branch

# If you want to delete a file from remote only
git rm --cached 'file name'
git commit -m'message'
git push -u origin branch
```

## diff
```sh
# lists out the changes between your current working directory and your staging area
git diff

# check diff between two branches
git diff master my-branch  # same as 'git diff master..my-branch'

# show difference for a specific file or directory
git diff file_name

# lists out the changes between the staged area and last commit
git diff --staged
```

## gitignore
```sh
bin
# without a trailing slash, the rule will match a file and a directory
bin/
# ignore all
bin/*
# ingore all files and folders
/bin
# match folder in root directory

Bin/*
Ignore all files and directories inside the directory
```

## log
```sh
git log
git log show <commit number>
git log --stat
git log --oneline
git reflog
```

## merge
`Feature branch can merge master branch.Master branch can also merge feature branch`
![merge1](assets/merge1.png)
![merge2](assets/merge2.png)
```sh
# Start a new feature
git checkout -b new-feature main
# Edit some files
git add <file>
git commit -m "Start a feature"
# Merge in the new-feature branch
git checkout main
git merge new-feature

## in oneline
git merge feature main
```

## push
```sh
git push <remote> <local_branch>:<remote_name>
```

## rebase
![git rebase1](assets/gitrebase1.png)
![git rebase2](assets/gitrebase2.png)
`vanilla workflow of git rebase`
```sh
git checkout -b my-feature-branch
git rebase master
git checkout master
git merge my-feature-branch
```
> The major benefit of rebasing is that you get a much cleaner project history.

> While working in Git, developers often make temporary commits that may have not appropriate commit messages. Before merging those commits to the master, it is necessary to combine them into a single commit with clear and comprehensive commit message.
`combine commits`
```sh
# Running git rebase in interactive mode
git rebase -i HEAD~3 # or git rebase -i <some hash>

# Replace pick with squash
# commands: 
# pick = use commit
# reword = use commit, but eddit the commit message
# edit = use commit, but stop for amending
# squash = use commit, but meld into previous commit
# fixup = like 'sqush', but discard this commit  log message
# exec = run command(the rest of the line) using shell
# drop = remove commit

# Choose between commit messages
# one more editor window will show up to change the resulting commit message.

# Pushing changes
# you should run git push to add a new commit to the remote origin.
git push --force origin HEAD
git push --force-with-lease origin HEAD  # more safer way to push combined commits
```
`The Golden Rule of Rebasing`
> Once you understand what rebasing is, the most important thing to learn is when not to do it. The golden rule of git rebase is to never use it on public (main)branches.

## remote
```sh
git remote -vv
git remote show origin
```

## rename remote branch
```sh
Gg push origin <current branch>:refs/heads/<remote name>
```

## reset vs revert
> Git reset will overwrite previous commit, while git revert will create a new commit.
```sh
Git reset --hard HEAD~ #(discard all changes except last commits)
Git reset --soft HEAD~ #(keep all changes)
Git reset HEAD~ #(discard everything)
```

## semantic commit messages
- `chore`: add Oyster build script 
- `docs`: explain hat wobble 
- `feat`: add beta sequence 
- `fix`: remove broken confirmation message 
- `refactor`: share logic between 4d3d3d3 and flarhgunnstow 
- `style`: convert tabs to spaces 
- `test`: ensure Tayne retains clothing

## status
```sh
git status
git status -sb # clean log
```

## stash
> Git stash is a useful feature of git when the git user needs to switch from one working directory to another working directory for fixing any issue and the modified files of the current working directory are required to store before switching. Git stash stores all modified tracked, untracked, and ignored files and helps the user to retrieve the modified content when requires.
```sh
git stash -u/--include-untracked

# there are two ways to restore a git stash
# 1.git stash apply
# The git stash apply command restores the stash but doesn't delete it from the reference
git stash list
git stash apply stash@{n}

# 2.git stash pop
# The git stash pop command restores the stashed changes and schedules the stash for deletion from the reference
git stash list
git stash pop stash@{n}
```

## upstream
```sh
# Set upstream when pushing to remote 
git push -u origin topic 
# Set upstream without pushing it 
# with option -u / --set-upstream-to 
git branch -u origin/topic 
git branch --set-upstream-to=origin/topic

# check upstream
git branch -vv
cat .git/config

# unset upstream
git branch --unset-upstream [<branchname>]
```