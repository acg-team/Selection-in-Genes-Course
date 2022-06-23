### Configuration files for all runs

In case you would like to compare your configuration files to the ones that were used to produce these results, you can find them in the left-hand panel under the heading **Example control files**.

### Answers to the tutorial questions

Assuming that the output is as given in this tutorial, these are the expected answers to the tutorial questions.

> - Based on LRTs, what model fits your data the best (among two-ratio, three-ratio and free-ratio models)? 

Before we can do LRTs we need to first determine which models are nested and compute the number of parameters for each model. Both the two-ratio and the three-ratio

The free-ratio model can be constrained to become both the two-ratio and the three-ratio model, meaning that it is nested in both. The three-ratio model can be constrained to be like the two-ratio model, meaning that the three-ratio model is nested within the two-ratio one.

For all runs we allow CodeML to optimise branch lengths on the 7 taxa tree, which means that for each model we will have at least 2*7-3 = 11 parameters. We also estimate the transition-transversion ratio κ, adding another parameter to all models.

For the free-ratio model we will also estimate an ω per branch, meaning that we will have 11 additional parameters, bringing the total parameter number to 11+1+11=23.

For the two-ratio model we only estimate 2 different ω, one for the background and one for the foreground branch that we labelled, bringing the total parameter number to 11+1+2=14.

For the three-ratio model we estimate 3 different ω, one for the background and two different ones for the two foreground branches, bringing the total parameter number to 11+1+3=15.

We can now write down the LRTs for all nested models, <img src="https://render.githubusercontent.com/render/math?math=2\Delta l = 2(l_\mathrm{nested} - l_\mathrm{null})">. We also need to compute the degrees of freedom, which in the case of nested models is simply the difference in parameter numbers. Finally, we set our significance level to 0.05.

| Models                    | LRT                              | Degrees of freedom | Significance |
| ------------------------- | -------------------------------- | ------------------ | ------------ |
| Two-ratio vs free-ratio   | 2(-896.412 - (-904.637)) = 16.45 | 23 - 14 = 9        | 0.058        |
| Three-ratio vs free-ratio | 2(-896.412 - (-901.102)) = 9.38  | 23 - 15 = 8        | 0.311        |
| Two-ratio vs three-ratio  | 2(-901.102 - (-904.637)) = 7.07  | 15 - 14 = 1        | **0.00784**  |

From these tests we see that we cannot reject neither the two-ratio or the three-ratio model in favour of the free-ratio one. This might mean that the free ratio one actually has too many parameters for this dataset and is not a reasonable model choice.

On the other hand, the two-ratio vs three-ratio test is significant, meaning that we can reject our null hypothesis of two ratios being sufficient to explain the differences in ω along the different tree branches.

To get a better gauge on what models make the most sense for our data, we might also run the analysis under the M0 model and do some more testing. For the M0 model we will only estimate the ω and the κ, as well as all branch lengths, bringing the total parameter number to 13.

| Models            | LRT                              | Degrees of freedom | Significance |
| ----------------- | -------------------------------- | ------------------ | ------------ |
| M0 vs Free-ratio  | 2(-896.412 - (-906.017)) = 19.21 | 23 - 13 = 10       | 0.0377       |
| M0 vs Three-ratio | 2(-901.102 - (-906.017)) = 9.83  | 15 - 13 = 2        | **0.00734**  |
| M0 vs Two-ratio   | 2(-904.637 - (-906.017)) = 2.76  | 14 - 13 = 1        | 0.0966       |

These tests confirm our previous conclusions. Firstly, we can reject the M0 model in favour of the free- and three-ratio models. Secondly, we cannot reject the M0 in favour of the two-ratio model. Combined with our previous tests, we can conclude that of all the models tested the three-ratio one is the best choice, with the M0 and two-ratio models being too constrained and the free-ratio model likely being too free for the data at hand.

However, we are now performing 6 different tests based on the same data and analyses, meaning that we need to perform at least some basic kind of multiple testing correction. We can use Bonferroni correction, which is a conservative approach in which we simply divide the selected p-value by the number of tests and use that as the cutoff in each of the tests. In this case we selected 0.05 as our p-value, which means that with the correction the p-value for each of the tests performed will be 0.05/6 = 0.008(3). Notably, both of the significant test results still hold true.

> - What are the estimates of ω from the best model? What can you conclude from them?

Assuming that the three-ratio model fits our data best, we can read off the estimates of ω for the background branches and the two different foreground branches that we marked on the tree.

| ω class        | Value  |
| -------------- | ------ |
| Background     | 0.540  |
| Colobine clade | 3.646  |
| Humanoid clade | 999.00 |

While it might seem tempting to assume that the *Colobine* clade branch shows signs of positive selection because its ω is greater than 1, we cannot make that claim based on this data. Based on the LRTs performed in this tutorial we cannot distinguish it from the background branches, meaning that we cannot conclude anything based on the value.

On the other hand, we can say that the Hominoid branch might show signs of positive selection as the ω estimate for it is significantly different from the background.

> - Compare your results to the analyses of this dataset in the original [paper](https://academic.oup.com/mbe/article/15/5/568/987857?login=false). Do your observations agree with those of Yang?

Yes. Moreover, in the original paper Yang performed more analyses that show that the ω estimates for the *Colobine* clade are not significantly different than 1, meaning that there is no evidence of strong positive selection along this branch. However, The humanoid clade seems to exhibit signs of positive selection with an ω > 1 in all tests.
