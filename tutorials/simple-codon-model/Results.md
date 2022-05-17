### Configuration files for all runs

In case you would like to compare your configuration files to the ones that were used to produce these results, you can find them in the left-hand panel under the heading **Example control files**.

### Answers to the tutorial questions

Assuming that the output is as given in this tutorial, these are the expected answers to the tutorial questions.

- > Among the two first runs, when is the log-likelihood higher? Why do you think it is?

For the first run with the branch lengths fixed to the values given in the input file, the log likelihood is *-1172.4*. For the second run with the branch lengths estimated by CodeML using maximum likelihood, the log likelihood is *-1137.69*.

The log likelihood for the second run is expectedly higher, as CodeML was allowed to optimise the branch lengths, meaning that the branch lengths were modified to increase the likelihood value.

<!--In the run with estimated branch lengths, do you observe codon usage bias?-->

<!--Study the statistics of nucleotide usage for different codon positions. Which position displays the most bias? Why?-->

- > What are the estimates of the transition-transversion ratio κ? 

For the first run the estimate of κ is *2.519*, and for the second it is *2.47*2. This can tell you that while the branch leghts were fixed to an arbitrary value in the first run, it did not have a significant impact on the estimate of the transition-transversion ratio.

- > What are the estimates of ω? How would you interpret these estimates?

For the first run the estimate of ω is *0.839*, and for the second it is *0.9*02. Both of these values are below 1, however not significantly. From prior information we also know that this specific gene is a well-known example of adaptive evolution. As in these analyses ω is averaged over all positions in the sequences we can conclude that the exact value is not very informative.

- > Compare your results to the analyses of this dataset (**D10** in the paper) in the original PAML [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461088/). Do your observations agree with those of Yang et al.?

In the original paper Yang et al. estimate ω to be *0.901*, and the final likelihood is *-1137.69*.  These are the same values (up to the third decimal point) that we get when we allow CodeML to optimise branch lengths of the tree.

- > Between the second run and the "bonus" run, are the tree branch estimates different? Are there a lot of differences between the two runs?

In both runs we allowed CodeML to optimise branch lengths, in the second run using the input tree branch lengths as starting values and using random initial values in the "bonus" run. If the analysis is not sensitive to starting values (and it often will not be for such a small dataset) the resulting branch length values will be the same in both runs. An easy way to do an initial check whether that is the case is to look at the tree lengths from the two runs, which in both cases is *1.76*. So in this case the initial values did not have a big influence and the estimates of branch lengths are the same for both runs.
