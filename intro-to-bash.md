## Goals
 * Becoming comfortable running programs via a <code>bash</code>
 * Understanding how to set up pipelines.
 * Becoming familiar with the basic programs used when working in <code>bash</code>.



## Organization
 * brief lecture on the role of a shell in the computing.
 * Most of the workshop will be working through the excellent software carpentry introduction to the shell
   * [Download link](http://swcarpentry.github.io/shell-novice/setup)
   * [Table of contents for the tutorial](http://swcarpentry.github.io/shell-novice/)
 * An example of shell pipelines in summer workshop that I teach in.



## Another example of pipelines
 * Download [ex-pipelines.zip](phylo.bio.ku.edu/slides/ex-pipelines.zip)
 * Task 1: write a script or pipeline to reformat  `model.tre` 
   to make a file that only contains the tree description which 
   is the part that starts with multiple parentheses and ends with 
   a semicolon.



## Task 2: Background
 * The file `step19.sim.log` has the output from 1000 
 simulations. Each produces 2 tree "Length" numbers.
 We are interested in the distribution of the difference between these 2 numbers.
 * `consecutiveDiffs.py` is a python script that will read from standard input. If the 
 input is a series of numbers, the script will write to standard output. It will write
 the difference between 1st and 2nd number, the difference the 3rd and 4th, etc.




## Task 2: find a P-value
 * Can you construct a pipeline to answer the question: **What are the 50 largest differences?**
 


## Checking your answers
  * Steps 13 and the "postscript" of [this computer lab](https://molevol.mbl.edu/index.php/ParametricBootstrappingLab)
   describe one solution.
  * `awk` in those scripts is a tool that works like `cut` in the software carpentry tutorial.
