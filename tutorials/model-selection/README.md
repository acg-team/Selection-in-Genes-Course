# Model selection

## Motivation



In this tutorial you will investigate substitution model selection on a limited set of models. 

## Data

For this tutorial we will use an alignment file in PhyLip format, same as we used in the first tutorial, `primate-nt.phy`.

This file is available on the left-hand panel under the heading **Data**.


## Setting up the analyses with PhyML

Once again, we will use the PhyML command line interface to run the analyses. This time you will start 6 independent analyses on the same data, which will allow you to see which model configuration could be best suited for the job.

Once you've downloaded the data, set up and run the analyses with the same MSA, with the 6 different substitution model settings defined in the table below. Allow PhyML to search the tree space using maximum likelihood in all analyses.

| Run ID      | Substitution model | Gamma            | Proportion invariate sites |
| ----------- | ------------------ | ---------------- | -------------------------- |
| **JC**      | JC69               | No               | 0                          |
| **JC+G**    | JC69               | Yes, α estimated | 0                          |
| **JC+G+I**  | JC69               | Yes, α estimated | Estimated                  |
| **HKY**     | HKY85              | No               | 0                          |
| **HKY+G**   | HKY85              | Yes, α estimated | 0                          |
| **HKY+G+I** | HKY85              | Yes, α estimated | Estimated                  |

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/model-selection/data/primates-nt.phy -d nt -q -m JC69 -f m -c 1 -v 0 -o tlr --run_id JC-->

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/model-selection/data/primates-nt.phy -d nt -q -m JC69 -f m -a e -v 0 -o tlr --run_id JC+G-->

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/model-selection/data/primates-nt.phy -d nt -q -m JC69 -f m -a e -v e -o tlr --run_id JC+G+I-->

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/model-selection/data/primates-nt.phy -d nt -q -m HKY85 -f m -c 1 -v 0 -o tlr --run_id HKY-->

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/model-selection/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -v 0 -o tlr --run_id HKY+G-->

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/model-selection/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -v e -o tlr --run_id HKY+G+I-->



## Computing the Akaike Information Criterion

Once all 6 runs are completed, compute the Akaike Information Criterion (AIC) for each run:
$$
AIC = 2k - 2\mathrm{log}(L),
$$
where $k$ is the number of free parameters of the model and $L$ is the likelihood that you get for the best tree under this model.

> - Find out the number of free parameters for each model;
> - Find the likelihood value for the ML tree in each run;
> - Compute the AIC for all 6 models that you tested.

<!--k=(2∗no. taxa−3)+no. parameters in substitution model+extra parameters k=(2∗no. taxa−3)+no. parameters in substitution model+extra parameters-->

<!--substitution models: JC = 0 parameters | HKY = 4 parameters | GTR = 8-->
<!--parameters-->
<!--invariant sites = +1 parameter-->
<!--gamma rates = +1 parameter-->

## Interpreting the results

Now that you computed the AIC for all the models, rank them best to worst.

<!--We select the model with the lowest AIC value. In this case, **GTR + Gamma**-->

> - Does adding the Gamma distribution create a significant difference in AIC?
> - Does adding invariable sites to the model make a difference to AIC?
> - Which model fits the data best based on AIC?
> - Why does AIC penalise more parameters over fewer parameters?
> - Could we have used LRT to choose among models? Why or why not?

<!--HKY = Trans/transv + pi?-->
