### Configuration files for all runs

In case you would like to compare your configuration files to the ones that were used to produce these results, you can find them in the left-hand panel under the heading **Control files for CodeML v4.10.0**.

### Answers to the tutorial questions

Assuming that the output is as given in this tutorial, these are the expected answers to the tutorial questions.

> - Perform likelihood ratio tests on the nested models.

M0 is nested within the M3 model -- M0 only has one category of rates and therefore one ω value, making it a restricted version of M3 with the number of categories k equal to 1. The rates ω per category in M3 are not restricted by any distribution. This test is usually used as a sanity check, as most datasets will exhibit some kind of variation across sites, meaning that the null will be most often rejected.

Both M7 and M8a are nested within M8. The M8 model defines 2 categories of sites defined by the proportions p<sub>0</sub> and p<sub>1</sub>. For the proportion p<sub>0</sub> of sites belonging to the first category, the model estimates the parameters p and q of the Beta distribution, which constrains all the ω values for this class of sites between 0 and 1 (sites not under strong positive selection). For the proportion p<sub>1</sub> of sites the model estimates an ω value that is necessarily greater than 1. Overall, as p<sub>0</sub> + p<sub>1</sub> = 1, this model has 4 free parameters, p<sub>0</sub>, p, q and ω.

The M7 model is a restricted version of the M8 model where p<sub>0</sub> is constrained to 1, meaning that there are variable rates among all sites, but all rates are constrained between 0 and 1.

Similarly, the M8a model is a restricted version of the M8 model. The M8a model restricts the free value of ω for the p<sub>1</sub> class to 1, meaning that the parameter of the M8a model lies on the edge of the parameter space for M8. This in turn means that we need to use a mixture distribution of 0 and χ<sup>2</sup><sub>1</sub> to check for significance, or we can use χ<sup>2</sup><sub>1</sub> for a more conservative test.

We can now compute the test statistic for all tests: 2Δl = 2(l<sub>alternative</sub> - l<sub>null</sub>). We will use the critical p-value of 0.05, but as we are performing 3 different tests on the same dataset we will apply the Bonferroni correction, meaning that to be significant the p-value for the test needs to be less than 0.05 / 3 = 0.016(6).

| Models            | LRT                                 | Degrees of freedom | Significance            |
| ----------------- | ----------------------------------- | ------------------ | ----------------------- |
| **M0** vs **M3**  | 2(-3687.064 - (-3815.514)) = 256.9  | 37 - 33 = 4        | **< 10e<sup>-16</sup>** |
| **M7** vs **M8**  | 2(-3686.134 - (-3697.223)) = 22.178 | 36 - 34 = 2        | **< 10e<sup>-5</sup>**  |
| **M8a** vs **M8** | 2(-3686.134 - (-3692.349)) = 12.43  | 36 - 35 = 1        | **0.000422**            |

> - Does the data exhibit a strong variation in the ω rates (test for **M0** vs **M3**)?

The null M0 model is rejected with a very low p-value when compared to the M3 model with variable rates among sites. This indicates that variation is present in the dataset and we can continue investigating the different rates.

> - Compare results from the LRT between **M7** and **M8** and the LRT between **M8a** and **M8**. Are they both significant (or both non-significant)?

Both tests between the **M7** and the M8 **and** the **M8a** and **M8** models are significant. The **M8a** vs **M8** is still significant despite using the χ<sup>2</sup><sub>1</sub> distribution for the test statistic rather than the mixture which would be more appropriate for this case. We reject both **M7** and **M8a**, which indicates that there are indeed sites under positive selection in this data.

> - If LRTs suggest positive selection, which sites are inferred to be under positive selection (model **M8**)? Use the Bayes Empirical Bayes estimates and find the sites for which ω is strictily above 1.

LRTs do suggest positive selection, and looking at the ourput files for the M8 model we see that 8 sites are inferred to be under positive selection:

            Pr(w>1)     post mean +- SE for w
    
     7 S      0.979*        2.442 +- 0.534
    42 S      0.539         1.625 +- 0.846
    48 T      0.833         2.176 +- 0.753
    50 D      0.970*        2.430 +- 0.554
    54 G      0.520         1.594 +- 0.870
    67 G      0.961*        2.413 +- 0.573
    85 T      0.616         1.774 +- 0.860
    123 P     0.976*        2.435 +- 0.540
If we look for sites where ω is strictly above 1 (the ω value is above 1 even when the standard error is taken into account) we end up with sites 7, 48, 50, 67, and 123,  all of which except site 48 have 95% posterior probability.

> - Compare your results to the analyses of this dataset (**D2** in the paper) in the original PAML [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461088/). Do your observations agree with those of Yang et al.?

Yes, they do. 

On top of all the tests performed in the original paper we also performed the **M8a** vs **M8** test, for which the asymptotic distribution of the test statistic follows from standard theory, whereas for the **M7** vs **M8** test the distribution of the test statistic is an ad hoc approximation. This can make the **M8a** vs **M8** test more powerful, however this property only holds if for the positively selected sites the value of ω is significantly greater than one. In this case both tests reject the null hypotheses, and **M8** estimates the ω on positively selected sites at 2.081.
