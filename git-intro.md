#### Hi (again)!
  * [Mark T. Holder](https://phylo.bio.ku.edu)
  * computational evolutionary biologist in EEB and the BI
  * https://orcid.org/0000-0001-5575-0536



#### Credits
  * https://swcarpentry.github.io/git-novice/
  * https://github.com/kcranston/2013-08-ku
  * https://www.slideshare.net/chacon/git-101-presentation/



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




#### `git init`

    mkdir from-scratch
    cd from-scratch
    git init
    ls -a     # in bash "dir" on Windows
    find .    # in bash (I don't know on Windows )

  * `git init` should be used inside the directory you want to be the top-level of the versioned content
  * creates a `.git` directory with the necessary structure to hold the `git` database



#### `git clone`

    cd ..
    git clone https://github.com/mtholder/grokking-git.git
    #               ... or ...
    git clone git@github.com:mtholder/grokking-git.git
    #               ... or ...
    git clone ~/some/other/directory/on/your/filesystem

  * Copies an existing repo using one of a few protocols
  * The source of the repo is often GitHub



#### `git add` to version new files

    cd from-scratch
    echo hi >> README.md
    mkdir subdir
    echo hi again >> subdir/README.md
    git status
    git add README.md
    git status
    git add subdir/README.md
    git status




#### *Staging area*
(I lied we have to talk about it a little) 

  * `git add` puts files from your working directory into the staging area
  * They aren't added to the `git` database until you `git commit`



#### `git commit`

    git commit -m "READMEs saying hi"

  * creates a "commit" object in the git database:
    * pointer to previous "parent" commit (none for first commit)
    * snapshot of the whole versioned "tree" of files (if they were added)
    * commit message (with the `-m` flag above)
  * Every commit gets an ID called a SHA




#### Add all flag

    git commit -a -m "some other message"

  * **After** you have added a files **once** to git:
    * whenever you've edited them more:
    * the `-a` will add "all" of them to the commit.
  * Let's you go from working directory -> git database in one command.




#### If you for get the message flag

    git commit -a

(note the lack of the `-m "some message"`)
  * Drops you into your configured text editor
  * [This link](https://mtholder.github.io/git-novice/02-setup/index.html#line-endings) shows how to set your text editor



#### other common commands
  * `git status` shows info on your working directory, the staging area, and the HEAD of the database
  * `git diff` compares contents of files in different versions
  * `git checkout SHAGOESHERE` is like the inverse of a `git commit -a` It sets your working directory to the version identified by the SHA




#### Basic workflow
https://www.slideshare.net/chacon/git-101-presentation/70




#### Let's try it out:
https://mtholder.github.io/git-novice/03-create/index.html
 
(my slight tweaks to the software carpentry intro)