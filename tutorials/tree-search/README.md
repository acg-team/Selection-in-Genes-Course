# Inferring a phylogeny using ML

## Motivation

Often times the first step in any analysis is phylogenetic tree inference. Maximum likelihood and Bayesian methods often take a long time to find a tree, so it is important to understand why these methods are percieved as the state-of-the-art despite their computational burden.

In this tutorial you will investigate the difference between a simple distance-based method for estimating phylogenetic trees (BioNJ) and a maximum likelihood tree search.

## Data

For this tutorial we will use an alignment file in PhyLip format, same as we used in the first tutorial, `primate-nt.phy`.

This file is available on the left-hand panel under the heading **Data**.


## Setting up the analysis with PhyML

Once again, we will use the PhyML command line interface to run the analyses. You will now run two analyses, one with no tree search, and one while estimating the tree using maximum likelihood .

Once you've downloaded the data, set up two analyses with the same input file.

### First run

Set up PhyML to analyse the data using the HKY85 model with the gamma distribution parameter, the transition/transversion ratio and the stationary frequencies estimated by ML, and the proportion of invariable sites set to 0.

Set the starting tree to one computed using BioNJ and disable tree topology and branch length optimisation, but keep rate parameter optimisation active.

Additionally, set the run ID to "bionj".

> - Write a command to run PhyML with the specified settings;
> - Run PhyML in console.

### Second run

Set up PhyML to analyse the data using the HKY85 model with the gamma distribution parameter, the transition/transversion ratio and the stationary frequencies estimated by ML, and the proportion of invariable sites set to 0.

Set the starting tree to one computed using BioNJ and enable full tree search.

Additionally, set the run ID to "ml_tree".

> - Write a command to run PhyML with the specified settings;
> - Run PhyML in console.

## Interpreting the results

Now that you ran both analyses, open the statistics files from the two runs. The files will be located in the same folder as where you put your sequence file and will be called something like `primates-nt.phy_phyml_stats_bionj.txt`  and `primates-nt.phy_phyml_stats_ml_tree.txt` . Study the output of the runs and answer the following questions:

> - Are the parameter estimates different?
> - Is there a difference in the likelihood between the two runs?

Additionally, open the two tree files, which will be called something like `primates-nt.phy_phyml_tree_bionj.txt`  and `primates-nt.phy_phyml_tree_ml_tree.txt`. 

> - Are these trees different to one another?
> - Where do the differences come from?

Example output files are provided on the left-hand panel, under the heading **Output**.

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/tree-search/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -t e -v 0 -o r --run_id bionj-->

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/tree-search/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -t e -v 0 -o tlr --run_id ml_tree-->
