### How should we build a tree of about 2.6 million tips?

  1. Supermatrix
    * Create a huge matrix of all available data,
    * Use parsimony, distance, likelihood, or Bayesian methods to estimate a tree



<img width="800" src="images/atols.png" />



### How should we build a tree of about 2.6 million tips?

  1. Supermatrix
    * Create a huge matrix of all available data,
    * Use parsimony, distance, likelihood, or Bayesian methods to estimate a tree

### Problems:
  1. Hard to establish homology on this scale.
  2. Few models are appropriate on this scale.
  3. Hard to compute a reliable answer on this scale.
  4. **Lots** of missing data.



### How should we build a tree of about 2.6 million tips?

  1. <strike>Supermatrix</strike>
  2. Supertree analyses



### Supertree analyses
  1. Gather a large set of partially overlapping estimated trees - These will be the data.
  1. Define an optimality criterion or procedure for resolving conflict.
  3. Produce a "supertree" that has all of the species
  in the sample.



<img src="images/WiegmannPNAS.png" />



<img width="500" src="images/WiegmannFlyTree.jpg" />




<img src="images/using_trees.png" />



<img src="images/fractionTreesArchived.png" />



<img src="images/overview.png "/>



<img src="images/architecture.png"/>



### Input Tree Curation tool
https://tree.opentreeoflife.org/curator

  1. Map OTUs to a common taxonomy.
  2. Correction rooting of tree.
  3. Identification the ingroup.
  4. Add metadata (currently unused)

https://tree.opentreeoflife.org/curator/study/view/ot_1050




### Input tree storage
https://github.com/OpenTreeOfLife/phylesystem-1

  1. Versioned,
  2. Provenance of who uploaded and curated the data



### Assembly of the Open Tree Taxonomy (OTT)

See Rees and Cranston [preprint](http://biorxiv.org/content/biorxiv/early/2017/03/13/116418.full.pdf)
  for details; that manuscript is the source of several of the next images and examples

An automated system creates OTT by merging:
  * 6 large taxonomies (NCBI, GBIF, IRMNG, SILVA, Index Fungorum, WoRMS)
  * 2 small taxonomies from publications Hibbett *et al.* (2007) and Schäferhoff *et al.* (2010)
  * a curated set of corrections.



### Why is merging taxonomies hard?



### Why is merging taxonomies hard?

  1. Taxonomic names are not identifiers.
    * A species has 1 valid name per classification, but there can be more than >1 classification.
      * Genus name could differ.
      * Both genus name and epithet can differ.
    * The same name can refer to different taxa governed by different codes.
    * Higher taxonomic names unregulated
  2. Very few taxon concept definitions are recorded.
  3. The largest databases tend to have less metadata about the names (e.g. authority info)
 



### Steps
  1. Merge taxonomies iteratively
  2. Align names in the next taxonomy to the current union taxonomy
    1. Find candidate alignments based on name matching,
    2. Consider placement, rank, shared descendants, *etc.* tp decide if a candidate is a good match



###    # A cross-code homonym example

*Aporia sordida*
  * A tea plant [in the last gbif version we used](http://www.gbif.org/species/6880118/)
  * A butterfly [in the version of IRMNG we used](http://www.marine.csiro.au/mirrorsearch/ir_search.taxon_info?id=10682816)

(currently changed in both sources)



<img src="images/ReesCranstonFig2.jpg"/><br />
Rees & Cranston, Fig. 2



<img src="images/ReesCranstonFig3-upper.png" /><br />
Rees & Cranston, Fig. 3




<img src="images/ReesCranstonFig3-lower.png" /><br />
Rees & Cranston, Fig. 3



### Open Tree Taxonomy stats
  * currently at version 3.0 [info+download link](https://tree.opentreeoflife.org/about/taxonomy-version/ott3.0)
  * 3.1 million taxonomic names thought to be valid
  * 1.8 million synonyms
  * browsable at https://tree.opentreeoflife.org/taxonomy



<img src="images/architecture.png"/>



## Goals of the summary tree creator
Paraphrasing [Redelings and Holder (2017)](https://peerj.com/articles/3058/),
the summary tree should:

  1. display no unsupported groups,
  2. defer higher ranked trees,
  3. be as resolved as feasible, and
  4. displays as many groupings from input trees as possible.



### Defn: a tree "displays group *X*"

Recall that the summary tree *S* will have more species than the input trees.
Consider:
  * some input tree *T1* that has a subtree called *X*,
  * imagine pruning the summary tree *S* down to the leaf set 
    of *T1*

If the pruned tree shows a subtree with only the leaves of *X*, then
  *S* displays *X*.




<img src="images/RedelingsHolderFig1.png"/>




### A definition of "supported"
If edge *Y* in the summary tree *S* can be collapsed, and the
    resulting tree still displays the same set of input
    groups, then we say that edge *Y* was "unsupported".

If collapsing that edge means that the tree now longer
    displays input group *X*, then we say that "*Y* was supported by *X*"

