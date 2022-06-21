### Configuration files for all runs

In case you would like to compare your configuration files to the ones that were used to produce these results, you can find them in the left-hand panel under the heading **Example control files**.

### Answers to the tutorial questions

Assuming that the output is as given in this tutorial, these are the expected answers to the tutorial questions.

> - Does the LRT for positive selection indicate positively selected sites on the foreground branch?

The two models, model A and model A1 differ in only one parameter. The proportions of different sites are estimated in both, but in A1 ω<sub>2</sub> is fixed to 1, meaning that the number of parameters and the corresponding number of degrees of freedom for this test is 1. However, 1 is on the edge of possible parameter space for the A model (the alternative model has a constraint on ω<sub>2</sub> to be greater or equal to 1 which means the test is one sided), so to check for significance we use a mixture of 0 and χ<sup>2</sup><sub>1</sub>. The critical values of this mixture distribution are 2.71 and 5.41 at the 5% and 1% levels. We can also just use χ<sup>2</sup><sub>1</sub> to keep the test conservative.

The likelihood ratio for this test is computed as:

<center>2Δl = 2(l<sub>MA</sub> - l<sub>MA1</sub>)</center>

| Test              | LRT                              | Degrees of freedom | Significance for χ<sup>2</sup><sub>1</sub> | Significance for mixture |
| ----------------- | -------------------------------- | ------------------ | ------------------------------------------ | ------------------------ |
| **MA** vs **MA1** | 2(-901.563 - (-902.302)) = 1.478 | 16-15 = 1          | 0.224                                      | >5%                      |

The test shows that we cannot reject the null hypothesis that the *Colobine* branch has positively selected sites, meaning there is no statistically significant support for positive selection in the primate lysozyme data set.

> - Are the results of the LRT consistent with the results of the analysis of this dataset from the previous tutorial on branch models?

The previous analysis showed that while ω was significantly higher than the background ratios, it was not significantly greater than 1. This means that the conclusions we can draw from these two tests are the same.

> - Compare your results to the analyses of this dataset in the original [paper](https://academic.oup.com/mbe/article/22/12/2472/1009544?login=false). Do your observations agree with those of Zhang et al.?

Yes, they do.
