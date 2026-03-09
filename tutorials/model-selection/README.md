# Model selection

<!-- > This tutorial setting slightly changed from when it was taught on 10.05.22.
>
> The differences are:
>
> 1. There is now a fixed tree file provided to ensure that the analyses are comparable.
> 2. There are 2 additional model settings for testing.
> 3. The tutorial now includes some LRTs in addition to AIC computation. -->

## Background

We will use PhyML and a toy dataset to play around with approaches to model selection.

<!-- 
Selecting among different and seemingly equally well-fitting models is 

While many molecular evolution models are available, there is no obvious way to tell which one describes your data better than others. On the one hand, simple evolutionary models are computationally less demanding, but are clearly an oversimplification of reality. On the other hand, complex models are more realistic, but computationally costly and prone to overfitting.

We need to be clever about selecting a model that is appropriate for our data, and use statistical criteria to justify our choices. In this tutorial you will investigate substitution model selection on a limited set of models to find out which would be a better fit to the dataset you're given. -->

## Data

For this tutorial we will use an alignment file in PhyLip format, `primate-nt.phy`, and a phylogenetic tree file, `primate-tree.newick`.

Both files are available on the left-hand panel under the heading **Data**.


## Setting up the analyses with PhyML

We will use the PhyML command line interface to run the analyses. You should run 8 independent analyses on the same data, which will allow you to see which model configuration could be best suited for the job.

Once you download the data, set up and run the analyses with the same MSA and **fixed** guide tree, with the 8 different substitution model settings defined in the table below. Allow PhyML to optimise branch lengths of the tree using maximum likelihood in all analyses.

| Run ID      | Model | Frequencies | Gamma            | Proportion invariate sites |
| ----------- | ----- | ----------- | ---------------- | -------------------------- |
| **JC**      | JC69  | Fixed       | No               | 0                          |
| **JC+G**    | JC69  | Fixed       | Yes, α estimated | 0                          |
| **JC+I**    | JC69  | Fixed       | No               | Estimated                  |
| **JC+G+I**  | JC69  | Fixed       | Yes, α estimated | Estimated                  |
| **HKY**     | HKY85 | Empirical   | No               | 0                          |
| **HKY+G**   | HKY85 | Empirical   | Yes, α estimated | 0                          |
| **HKY+I**   | HKY85 | Empirical   | No               | Estimated                  |
| **HKY+G+I** | HKY85 | Empirical   | Yes, α estimated | Estimated                  |

## Computing the Akaike Information Criterion

The Akaike Information Criterion (AIC) is an estimator of the relative quality of model fit to the data. We can rank the models by AIC value and use the ranking to determine what model fits best, regardless of whether the models are nested or not.

Once all 8 runs are completed, compute the (AIC) for each run:

<center>`AIC = 2k - 2l`,</center>


where `k` is the number of free parameters in this analysis and `l` is the logarithm of the likelihood.

> - Find out the number of free parameters for each run (the number of parameters is the number of branch lengths and the number of substitution model parameters);
> - Find the log likelihood value for each run;
> - Compute the AIC for all 8 models that you ran.

## Performing LRTs to test for among site variation



To test for among site variation we will need to compare the results from models without site variation (no Gamma) to the results of the same model with a Gamma distribution. The LRT statistic is computed as follows:

<center>2Δl = 2(l<sub>alternative</sub> - l<sub>null</sub>)</center>


> - Which of the models in these runs are nested and can be used to test for among site variation?
> - What are the degrees of freedom for each comparison?
> - Perform all possible LRTs to test for among site rate variation;

## Interpreting the results

Now that you computed the AIC for all the models, rank them best to worst.

> - Does adding the Gamma distribution create a significant difference in AIC?
> - Does adding invariable sites to the model make a difference to AIC?
> - Which model fits the data best based on AIC?
> - Why does AIC penalise more parameters over fewer parameters?
> - Could we have used LRTs to choose among all of these models? Why or why not?

Using the LRT statistics that you computed, answer the following questions:

> - Which of the LRTs are significant if we set the significance level to 0.05 and apply Bonferroni correction for multiple testing?
> - What can you conclude from these tests?

## Answers

