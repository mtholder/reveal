### Goals
 * Learning how to use <code>git</code> branches effectively.
   * <code>git branch</code>
   * <code>git merge</code>
   * <code>git remote add ...</code>
   * <code>git fetch</code>
 * Emphasize the importance of running tests:
   * verification of correctness
   * debugging
   * continuous integration
   * <code>git bisect</code>



### I'm assuming that you:
  * know <code>git clone</code>
  * know how to author commits with <code>git add</code> and <code>git commit</code>
  * have configured your local version of git to work with your account on [GitHub](https://github.com/)

If not see: 
  [Software Carpentry git novice](https://swcarpentry.github.io/git-novice/02-setup/) 
  and/or ask me for help



### Demystifying <code>git</code>
<code>git</code> stores information in 3 types of objects:
  * **blob** objects store the contents of a *versioned*  file
  * **tree** objects store snapshots of a *versioned* directory. This is essentially a
  list of which versions of each **blob** are in that snapshot
  * **commit** objects associate a **tree** snapshot with its parent **commits** and the metadata for a commit (author, timestamp, commit message)

Don't worry about learning the commands I'm about to show - almost on git users use these!



### This is the part where I'll:
  * use <code>tree</code>, <code>git init</code>, my editor, git commit skills
  * use the very obscure <code>git cat-file -p &lt;SHA&gt;</code> to see the core
  objects
  * review using Scott Chacon's truly awesome [Git 101 slideshow](https://www.slideshare.net/chacon/git-101-presentation/117). 



### Important commands (review)
  * <code>git add ...</code> to stage changes so they'll be committed.
  * <code>git commit ...</code> to create commit object and advance the current branch to point
    to that new commit.
  * <code>git checkout &lt;branch-name&gt;</code> makes your working tree look like the tree
    stored at that branch, and registers that branch as the HEAD for future commits.



### Remotes
  * slides from [Git 101 slideshow](https://www.slideshare.net/chacon/git-101-presentation/213).



### remotes and "publishing" your work to a remote
  * A remote is just another git repository. Usually it is on another machine.
  * <code>git push</code> sends commits and the branch to the remote
    * Sends the objects and advances the "upstream" branch pointer
    * So that you have a broken state, you can only push "fast-forwards" (unless you force things)



### Getting information from the remote
  * <code>git fetch</code> retrieves the remote's objects and branch pointers
  * <code>git branch -a</code> lists all branches
  * The key: <code>remote-name/branch-name</code> is just another branch
  * <code>git pull</code> is just shorthand for <code>fetch</code> and then <code>merge</code>




### A fork on GitHub (or other git server)
  * just another remote.
  * has its own branch pointers.




### Joys of having a test script:
  * test before you commit
  * test after you merge (or pull, since a pull is a merge) - unless you did a fast-forward merge
  * <code>git bisect</code>
  * [Travis continuous integration testing](https://travis-ci.org/OpenTreeOfLife/peyotl)