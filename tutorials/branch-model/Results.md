### Configuration files for all runs

In case you would like to compare your configuration files to the ones that were used to produce these results, you can find them in the left-hand panel under the heading **Example control files**.

### Answers to the tutorial questions

Assuming that the output is as given in this tutorial, these are the expected answers to the tutorial questions.

- > Based on LRTs, what model fits your data the best (among 2-ratio, 3-ratio and free-ratio models)? What are the degrees of freedoms for each comparison?

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
| M0 vs Free-ratio          | 2(-896.412 - (-906.017)) = 19.21 | 23 - 13 = 10       | **0.0377**   |
| M0 vs Three-ratio         | 2(-901.102 - (-906.017)) = 9.83  | 15 - 13 = 2        | **0.00734**  |
| M0 vs Two-ratio           | 2(-904.637 - (-906.017)) = 2.76  | 14 - 13 = 1        | 0.0966       |
