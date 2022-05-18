### Commands for all runs

In case you would like to compare your commands to the ones that were used to produce these results, the commands are given below.

#### JC:

`phyml -i /path/to/course/tutorials/model-selection/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/model-selection/data/primates-nt.newick -m JC69 -f m -c 1 -v 0 -o lr --run_id JC`

#### JC+G:

`phyml -i /path/to/course/tutorials/model-selection/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/model-selection/data/primates-nt.newick -m JC69 -f m -a e -v 0 -o lr --run_id JC+G`

#### JC+I:

`phyml -i /path/to/course/tutorials/model-selection/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/model-selection/data/primates-nt.newick -m JC69 -f m -c 1 -v e -o lr --run_id JC+I`

#### JC+G+I:

`phyml -i /path/to/course/tutorials/model-selection/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/model-selection/data/primates-nt.newick -m JC69 -f m -a e -v e -o lr --run_id JC+G+I`

#### HKY:

`phyml -i /path/to/course/tutorials/model-selection/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/model-selection/data/primates-nt.newick -m HKY85 -f m -c 1 -v 0 -o lr --run_id HKY`

#### HKY+G:

`phyml -i /path/to/course/tutorials/model-selection/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/model-selection/data/primates-nt.newick -m HKY85 -f m -a e -v 0 -o lr --run_id HKY+G`

#### HKY+I:

`phyml -i /path/to/course/tutorials/model-selection/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/model-selection/data/primates-nt.newick -m HKY85 -f m -c 1 -v e -o lr --run_id HKY+I`

#### HKY+G+I:

`phyml -i /path/to/course/tutorials/model-selection/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/model-selection/data/primates-nt.newick -m HKY85 -f m -a e -v e -o lr --run_id HKY+G+I`

## AIC for all runs

Once all the runs are complete we can compute the number of parameters for each model and compute the AIC.

Altogether we have 20 taxa, meaning that for each run PhyML needs to estimate 20*2 - 3 = 37 branch lengths.

For the JC69 model we do not estimate any parameters, and for the HKY85 model we need to estimate 3 stationary frequencies (the fourth one can be calculated as the frequencies add up to one) and the transition/transversion ratio, adding 4 parameters.

Adding gamma categories for any of the analyses adds another parameter (gamma shape), and adding invariable sites adds one more (proportion of invariable sites).

Knowing the parameter numbers and likelihoods from the runs we can compute the AIC using the following formula:

<img src="https://render.githubusercontent.com/render/math?math=AIC = 2k - 2\mathrm{log}(L)">

| Run ID      | No of parameters | Likelihood | AIC          | ΔAIC    |
| ----------- | ---------------- | ---------- | ------------ | ------- |
| **JC**      | 37+0+0+0 = 37    | -6379.664  | *12833.328*  | 404.168 |
| **JC+G**    | 37+0+1+0 = 38    | -6304.381  | 12684.762    | 255.602 |
| **JC+I**    | 37+0+0+1 = 38    | -6311.417  | 12698.834    | 269.674 |
| **JC+G+I**  | 37+0+1+1 = 39    | -6304.377  | 12686.754    | 257.594 |
| **HKY**     | 37+4+0+0 = 41    | -6250.999  | 12583.998    | 154.838 |
| **HKY+G**   | 37+4+1+0 = 42    | -6172.580  | **12429.16** | 0       |
| **HKY+I**   | 37+4+0+1 = 42    | -6180.097  | 12444.194    | 15.034  |
| **HKY+G+I** | 37+4+1+1 = 43    | -6172.553  | 12431.106    | 1.946   |

The maximal AIC is in italics, the minimal is in bold.

### Answers to the tutorial questions

> - Does adding the Gamma distribution create a significant difference in AIC?

Between the runs under JC and JC+G we see an AIC difference of 148.566, and between HKY and HKY+G we see a difference of 154.838. Assuming that a significant difference is at least 10 units, we can conclude that adding the gamma distribution significantly improves model fit to the data.

> - Does adding invariable sites to the model make a difference to AIC?

The difference in AIC between JC and JC+I is 134.494, and the difference between HKY and HKY+I is 139.804. Assuming that a significant difference is at least 10 units, we can conclude that adding invariable sites significantly improves model fit to the data.

However, once we add the Gamma that accounts for low mutation rates too, between the runs under JC+G and JC+G+I we see an AIC difference of -1.992, and between HKY+G and HKY+G+I we see a difference of -1.946. Assuming that a significant difference is at least 10 units, we can conclude that adding invariable sites does not significantly improve model fit. If anything, it seems to be making model fit slightly worse.

> - Which model fits the data best based on AIC?

Based off the AIC criterion, HKY+G fits the data best.

> - Why does AIC penalise more parameters over fewer parameters?

AIC penalises more model parameters to minimise the effect of overfitting the model to the data.

> - Could we have used LRTs to choose among all or some of these models? Why or why not?

JC69 is nested within HKY85, which means that we could have used an LRT to compare the goodness of fit between these two models. Moreover, both models without gamma and invariable sites are nested within the respective models with gamma, with invariable sites, and with gamma and invariable sites.

Models with gamma or with invariable sites are nested within models that have both. 

However, we cannot compare JC+G and JC+I (and HKY+G and HKY+I respectively) using LRTs, as these models are not nested.
