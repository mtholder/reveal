### Using all data

Cons:
  * Can create long branches by lack of data for some tips or
     increasing the size of tree
  * Poor data overlap between taxa can lead to rogue taxa and terraces

Pros:
  * Uses all the data
  * Helps you spot the weakness in your phylogenetic argument



### Conclusions

  * Readers want to know how your phylogenetic model fits with all available data
  * More convincing to present full data, and **interrogate** analyses for causes of incongruence
  * That doesn't mean "total evidence"



### One recent example

[Dell'Ampio *et al.* (2014)](http://mbe.oxfordjournals.org/content/31/1/239) finds
  indecisive data sets still can contribute strong support of
Entognatha: (Collembola+Protura+Diplura)
  * not supported by their preferred `M_Ento` data set
  * 81% BP in an alternative with 253 loci only 79 cover C+P+D
  * up to 94% BP when these 79 loci are removed!

See [MARE software](https://www.zfmk.de/de/forschung/forschungszentren-und-gruppen/mare).



## Interaction effects

  * Missing data × model misspecification
  * Missing data × model partitioning
  * Missing data × ascertainment biases
  * Missing data × tree depth



### Missing data × model misspecification

  * Both [Lemmon *et al.* (2009)](http://sysbio.oxfordjournals.org/content/58/1/130) and
 [Roure *et al.* (2013)](http://mbe.oxfordjournals.org/content/30/1/197.abstract)
find that artificial data from 2 tips (or 1 tip) can mislead tree preferency by 
**contaminating parameter estimates**.
  * Conditions were contrived, but still indicates troubling lack of robustness.



### Missing data × model misspecification

  * Our models of substitution are not good enough to deal with deep divergences.

<img src="./images/Pisani-et-al-2015-fig-2.png">

Figure 2 from [Pisani *et al.* (2015)](http://www.pnas.org/cgi/doi/10.1073/pnas.1518127112) results from
[PhyloBayes CAT model](http://megasun.bch.umontreal.ca/People/lartillot/www/index.htm) analyses.



### Missing data × model partitioning

In a partitioned model, do the subsets of the data share
  the same substitution parameter, relative edge lengths, 
  or mean subset rate? Or some combination of parameter sharing...

  * "unlinking" parameters avoids errors caused by "parameter contamination" when loci evolve differently.
  * It causes terraces in likelihood space - See [Sanderson *et al.*, 2015](http://sysbio.oxfordjournals.org/content/64/5/709.full.pdf+html)
  and references therein




<img width="65%" src="images/Sanderson-et-al-2015-from-fig-2.png"/>

(from Figure 2 of [Sanderson *et al.*, 2015](http://sysbio.oxfordjournals.org/content/64/5/709.full.pdf+html))




<img width="70%" src="images/Sanderson-et-al-2015-fig-1.png"/>

(Figure 1 of [Sanderson *et al.*, 2015](http://sysbio.oxfordjournals.org/content/64/5/709.full.pdf+html))



<img width="70%" src="images/Sanderson-et-al-2015-fig-4.png"/>

(Figure 4 of [Sanderson *et al.*, 2015](http://sysbio.oxfordjournals.org/content/64/5/709.full.pdf+html))



### Missing data × model partitioning

Damned if you do partition:
  * Terraces 
    * complicate tree searching (but see [Chernomour *et al.* (2016)](http://sysbio.oxfordjournals.org/content/early/2016/04/26/sysbio.syw037.short)
  and recent work in [RAxML](http://sco.h-its.org/exelixis/software.html))
    * Can inflate BP ([Sanderson *et al.*, 2015](http://sysbio.oxfordjournals.org/content/64/5/709.full.pdf+html)).
  * Rogue taxa
    * complicate the usefulness of consensus summaries (see [RogueNaRok by Aberer *et al.*](http://rnr.h-its.org/about))
  * Added time finding many modes caused by large # of parameters

Damned if you don't:
  * parameter contamination + inconsistency, if process heterogeneity is important for your data.




### Missing data × ascertainment biases




### Missing data × tree depth




### Filtering columns of multiple sequence alignments

