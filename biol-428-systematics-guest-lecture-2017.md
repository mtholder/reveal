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



### Input tree storage
https://github.com/OpenTreeOfLife/phylesystem-1

  1. Versioned,
  2. Provenance of who uploaded and curated the data



### Assembly of the Open Tree Taxonomy (OTT)

See Rees and Cranston [preprint](http://biorxiv.org/content/biorxiv/early/2017/03/13/116418.full.pdf)
  for details; that manuscript is the source of several of the next images

An automated system creates OTT by merging:
  * 6 large taxonomies (NCBI, GBIF, IRMNG, SILVA, Index Fungorum, WoRMS)
  * 2 small taxonomies from publications Hibbett *et al.* (2007) and Schäferhoff *et al.* (2010)
  * a curated set of corrections.