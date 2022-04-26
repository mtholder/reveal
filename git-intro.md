#### Hi (again)!
  * [Mark T. Holder](https://phylo.bio.ku.edu)
  * computational evolutionary biologist in EEB and the BI
  * https://orcid.org/0000-0001-5575-0536



#### Credits
  * https://swcarpentry.github.io/git-novice/
  * https://github.com/kcranston/2013-08-ku



#### Version control
Except for trivial tasks, programming involves
  * writing code,
  * testing whether it works,
  * repeat
You will have many versions of your code.
A version control system helps you manage
changes to a code-base




#### `git` – _a_ distributed version control system
“Distributed”:  every developer has the entire version history. There is _no_ central server.

`git` lets you:
  * return to a previous snapshot of your code,
  * merge work from several developers,
  * easily share your code,
  * easily back up your code.




#### `git` ≠ github
  * `git` the command-line tool that manages versioning and distributing changes between different copies of the repository
  * [https://github.com](https://github.com) is web site that provides a lot of collaboration tools on top of git repositories




#### Core `git` commands
  * `git init` – create and empty repository
  * `git clone` – obtain an existing repository
  * `git add` – to tell git that you want to track a file
  * `git commit` – to add content to the repository
  * `git checkout` – copy code out of the repository to your filesystem
  * `git status` – create a report of how git sees the world
  * `git diff` – to show difference between versions




#### Setup - once per machine
The file `~/.gitconfig` stores some global settings that apply
to any git repository on your machine. `git config` command
is a tool to edit it. 2 are very important for attributing your commits correctly:

    $ git config --global user.name "Your Name Here"
    $ git config --global user.email "your.email@some.server"

[This link](https://mtholder.github.io/git-novice/02-setup/index.html#line-endings) shows how to set your text editor




#### A `git` versioned directory
`git` uses a directory on your computer.
  * The directory:
    * is your **working directory**
    * contains your versioned files and subdirs
    * can contain unversioned files (not controlled by `git`)
    * top-level holds a `.git` repository
  * The `.git` repository is:
    * the local database storing the history
    * contains info for the *index* or *staging area* which I won't discuss in detail (see [here](../git-branching.html) if you want).




#### 2 ways to make a `git` repository
  * `git init` to start a new one from scratch
  * `git clone` to make a copy of an existing repo.
