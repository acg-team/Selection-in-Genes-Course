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

### AIC for all runs

Once all the runs are complete we can compute the number of parameters for each model and compute the AIC.

Altogether we have 20 taxa, meaning that for each run PhyML needs to estimate 20*2 - 3 = 37 branch lengths.

For the JC69 model we do not estimate any parameters, and for the HKY85 model we need to estimate 3 stationary frequencies (the fourth one can be calculated as the frequencies add up to one) and the transition/transversion ratio, adding 4 parameters.

Adding gamma categories for any of the analyses adds another parameter (gamma shape), and adding invariable sites adds one more (proportion of invariable sites).

Knowing the parameter numbers and likelihoods from the runs we can compute the AIC using the following formula:

<img src="https://render.githubusercontent.com/render/math?math=AIC = 2k - 2l">

| Run ID      | No of parameters | Likelihood | AIC          |
| ----------- | ---------------- | ---------- | ------------ |
| **JC**      | 37+0+0+0 = 37    | -6379.664  | *12833.328*  |
| **JC+G**    | 37+0+1+0 = 38    | -6304.381  | 12684.762    |
| **JC+I**    | 37+0+0+1 = 38    | -6311.417  | 12698.834    |
| **JC+G+I**  | 37+0+1+1 = 39    | -6304.377  | 12686.754    |
| **HKY**     | 37+4+0+0 = 41    | -6250.999  | 12583.998    |
| **HKY+G**   | 37+4+1+0 = 42    | -6172.580  | **12429.16** |
| **HKY+I**   | 37+4+0+1 = 42    | -6180.097  | 12444.194    |
| **HKY+G+I** | 37+4+1+1 = 43    | -6172.553  | 12431.106    |

The maximal AIC is in italics, the minimal is in bold.

### LRTs for among site variation

We first need to define the set of tests we can perform to check whether adding among-site variation improves model fit. The tests need to be on nested models, and a comprehensive set of tests for this hypothesis is as follows:

- **JC** vs **JC+G**;
- **JC+I** vs **JC+G+I**;
- **HKY** vs **HKY+G**;
- **HKY+I** vs **HKY+G+I**.

We already know the numbers of parameters for each model, which allows us to easily get the degrees of freedom for each comparison. For example, **JC** has 37 parameters and is nested within **JC+G**, which has 38 parameters, meaning that the degrees of freedom for this comparison will be 38-37=1.

The LRT statistic is computed as follows:

<img src="https://render.githubusercontent.com/render/math?math=2\Delta l = 2(l_\mathrm{nested} - l_\mathrm{null})">

| Test                      | Degrees of freedom | LRT     | Significance        |
| ------------------------- | ------------------ | ------- | ------------------- |
| **JC** vs **JC+G**        | 38-37 = 1          | 150.566 | < 10e<sup>-20</sup> |
| **JC+I** vs **JC+G+I**    | 39-38 = 1          | 14.08   | 0.000175            |
| **HKY** vs **HKY+G**;     | 42-41 = 1          | 156.838 | < 10e<sup>-20</sup> |
| **HKY+I** vs **HKY+G+I**; | 43-42 = 1          | 15.088  | 0.000103            |

### Answers to the tutorial questions

The AIC values on their own are not interpretable, however we can use a set of rules of thumb to interpret the differences in AIC. The rules for differences are as follows:

- <img src="https://render.githubusercontent.com/render/math?math=\Delta_\mathrm{AIC} \leq 2">: model has substantial support;
- <img src="https://render.githubusercontent.com/render/math?math= 4 \leq \Delta_\mathrm{AIC} \leq 7">: model has considerably less support;
- <img src="https://render.githubusercontent.com/render/math?math=\Delta_\mathrm{AIC} > 10">: model has essentially no support.

These rule of thumb criteria are defined multiple times in literature, e.g. [Posada and Buckley, 2004](https://academic.oup.com/sysbio/article/53/5/793/2842928).

> - Does adding the Gamma distribution create a significant difference in AIC?

Between the runs under JC and JC+G we see an AIC difference of 148.566, and between HKY and HKY+G we see a difference of 154.838. Both of these values are above 10, meaning that we see no support for models without the Gamma distribution.

> - Does adding invariable sites to the model make a difference to AIC?

The difference in AIC between JC and JC+I is 134.494, and the difference between HKY and HKY+I is 139.804.  Both of these values are above 10, meaning that we see no support for the models without invariable sites.

However, once we add the Gamma that accounts for low mutation rates too, between the runs under JC+G and JC+G+I we see an AIC difference of 1.992, and between HKY+G and HKY+G+I we see a difference of 1.946. These differences are below 2, meaning that both these models have significant support.

> - Which model fits the data best based on AIC?

Based off the AIC criterion, HKY+G fits the data best.

> - Why does AIC penalise more parameters over fewer parameters?

AIC penalises more model parameters to minimise the effect of overfitting the model to the data.

> - Could we have used LRTs to choose among all or some of these models? Why or why not?

JC69 is nested within HKY85, which means that we could have used an LRT to compare the goodness of fit between these two models. Moreover, both models without gamma and invariable sites are nested within the respective models with gamma, with invariable sites, and with gamma and invariable sites.

Models with gamma or with invariable sites are nested within models that have both. 

However, we cannot compare JC+G and JC+I (and HKY+G and HKY+I respectively) using LRTs, as these models are not nested.

> - Which of the LRTs are significant if we set the significance level to 0.05 and apply Bonferroni correction for multiple testing?

When we apply Bonferroni correction for a given significance level we simply divide the significance level by the number of tests perfomed. Therefore, for an overall significance level of 0.05 on 4 tests we set the significance level for each individual test to 0.05/4 = 0.0125. As we can see all the tests are significant despite the applied correction, meaning that no matter the null model, we always reject it in favour of the model with site variation.

> - What can you conclude from these tests?

From these tests we can conclude that models with site variation are a better choice for the given dataset.
