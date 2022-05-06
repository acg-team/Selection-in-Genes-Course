# Practical: Investigating different parameter estimation approaches

## Motivation

Before going into complex phylogenetic analyses it is important to see the basic workflow and understand that minor changes in the analysis setup (i.e. your prior assumptions) can make a great difference in the result.

In this tutorial you will run PhyML on a given alignment of primate sequences with a fixed tree, and will investigate the difference in the results that stems from different approaches to parameter estimates.
Bear in mind that this is a warm-up round, as most real-life analyses will most likely not have a phylogenetic tree available.

## Data

Before we can perform any analyses, we need to download the inout data for this tutorial. We will use an alignment file in PhyLip format, `primate-nt.phy`, and a phylogenetic tree file, `primate-tree.newick`.

> **Downloading data**
> 
> A link to the alignment file, `primate-nt.phy`, is on the left-hand panel, under the heading **Data**.
> **Right-click** on the link and select **"Save Link As..."** (Firefox and Chrome) or **"Download Linked File As..."** (Safari) and save the file to a location on your local drive. Note that some browsers will automatically change the extension of the file from `.phy` to `.phy.txt`. If this is the case, simply rename the file. 
>
> Alternatively, if you **left-click** on the link most browsers will display the alignment file. You can then press **File > Save As** to store a local copy of the file. Note that some browsers will inject an HTML header into the file, which will make it unusable (making this the less preferable option for downloading data files).
>


## Setting up the analysis with PhyML

PhyML provides a few different options for running your analyses. You could use the [web server](http://www.atgc-montpellier.fr/phyml/), or the standalone version as a console application. The console application can be used with an interactive (yet clunky) user interface, or with command line parameters.

We recommend that you use the standalone version with command line parameters, as this will allow you to later easily run PhyML as part of a pipeline on your machine.

Once you've downloaded the data, set up two analyses with the same input files. 

### Setting the parameters

Before you start, run the help comand of PhyML to see the parameter options you can choose:

```
phyml --help
```

PhyML allows you to select from a range of standard molecular evolution models like JC69, K80, etc, set the Gamma distribution parameters to allow for across-site variability, estimate the transition/transversion ratio among other options.

> Read the manual entry for PhyML that you got with the previous command and do the following:
>
> - Find out how to provide the input alignment file and specify the data type (nucleotide sequences in a sequential format);
> - Find out how to set the evolutionary model;
> - Find out how to set the way stationary nucleotide frequencies are estimated (empirical or maximum likelihood (ML) estimates);
> - Find out how to provide a user-specified tree;
> - Find out how to disable tree topology and branch optimization;
> - Find out how to set the run ID so that you can distinguish the output from the two runs.

### First run

Set up PhyML to analyse the data using the HKY85 model with the gamma distribution parameter and the transition/transversion ratio estimated by ML, and the proportion of invariable sites set to 0.

Fix the tree to the provided file and disable tree topology and branch length optimisation, but keep rate parameter optimisation active.

Set the stationary frequencies to be estimated by ML.

Additionally, set the run ID to "ml".

> - Write a command to run PhyML with the specified settings;
> - Run PhyML in console.

### Second run

Set up PhyML to analyse the data using the HKY85 model with the gamma distribution parameter and the transition/transversion ratio estimated by ML, and the proportion of invariable sites set to 0.

Fix the tree to the provided file and disable tree topology and branch length optimisation, but keep rate parameter optimisation active.

Set the stationary frequencies to be estimated empirically from the data.

Additionally, set the run ID to "empirical".

> - Write a command to run PhyML with the specified settings;
> - Run PhyML in console.

## Interpreting the results

Now that you ran both analyses, open the statistics files from the two runs. The files will be located in the same folder as where you put your sequence file and will be called something like `primates-nt.phy_phyml_stats_ml.txt`  and `primates-nt.phy_phyml_stats_empirical.txt` . Study the output of the runs and answer the following questions:

> - What are the important values in these files?
> - Is there any difference between the stationary frequencies between the two runs?
> - Is there a difference in the likelihood?
> - Which estimation option is better and why do you think so?

Additionally, open the two tree files, which will be called something like `primates-nt.phy_phyml_tree_ml.txt`  and `primates-nt.phy_phyml_tree_empirical.txt`. 

> - Are these trees different to one another and to the input tree?
> - Should they actually be different?

Example output files are provided on the left-hand panel, under the heading **Output**.

## Additional tasks

Run the PhyML console user interface by simply typing phyml in the console:

```
phyml
```

Run the same analyses as before by navigating the user interface. Set the same options, but make sure your run ID is different from your previous runs, e.g. "empirical_gui".

> - Do you get the same values in the output?
> - Why or why not?

#### Troubleshooting

To check that you actually set the exact same parameters, you can try running the two analyses with the same random seed number. The random seed is what is used to start the pseudo-random number generation in your computer, so chances are that if you set all parameters to the same values and fix the seed you will get an identical replicate of your other analysis.

Unfortunately you can't set the seed in the GUI, so you'll have to run the analysis with the GUI first, then copy the seed used in that run and use it for the console command.

To make your task easier, here are the commands that set the right parameters (adjust the file paths according to where you stored the files and set the seed):

```
phyml -i ~/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -t e -v 0 -u ~/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.newick -o r --run_id ml --r_seed 1651861751
```

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -t e -v 0 -u /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.newick -o r --run_id ml --r_seed 1651861751-->

```
phyml -i ~/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -m HKY85 -f e -a e -t e -v 0 -u ~/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.newick -o r --run_id empirical --r_seed 13 
```
