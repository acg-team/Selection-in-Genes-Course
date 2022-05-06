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
> **Right-click** on the link and select **"Save Link As..."** (Firefox and Chrome) or **"Download Linked File As..."** (Safari) and save the file to a convenient location on your local drive. Note that some browsers will automatically change the extension of the file from `.phy` to `.phy.txt`. If this is the case, simply rename the file. 
>
> Alternatively, if you **left-click** on the link most browsers will display the alignment file. You can then press **File > Save As** to store a local copy of the file. Note that some browsers will inject an HTML header into the file, which will make it unusable (making this the less preferable option for downloading data files).
>


## Setting up the analysis with PhyML

PhyML provides a few different options for running your analyses. You could use the [web server](http://www.atgc-montpellier.fr/phyml/), or the standalone version as a console application. The console application can be used with an interactive (yet clunky) user interface, or with command line parameters.

We recommend that you use the standalone version with command line parameters, as this will allow you to later easily run PhyML as part of a pipeline on your machine.

Once you've downloaded the data, set up two analyses with the same files. 

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
> - Find out how to disable tree optimization.

### First run

Set up PhyML to analyse the data using the HKY85 model with a Gamma distribution (parameter estimated using ML) and a proportion of invariable sites estimated my ML.

Fix the tree to the provided file and disable tree search.

Set the stationary frequencies to be estimated by ML.

> - Write a command to run PhyML with the specified settings;
> - Run PhyML in console.

### Second run

Set up PhyML to analyse the data using the HKY85 model with a Gamma distribution (parameter estimated using ML) and a proportion of invariable sites estimated my ML.

Fix the tree to the provided file and disable tree search.

Set the stationary frequencies to be estimated epmirically from the data.

> - Write a command to run PhyML with the specified settings;
> - Run PhyML in console.

### Interpreting the results

Now that you ran both analyses, take a look at the statistics from both runs. Is there any difference between the stationary frequencies?

> - Is there any difference between the stationary frequencies?
> - Is there a difference in the likelihood?
> - Which estimation option is better and why do you think so?

<!--Set the model to HKY+Gamma, estimating the transition/transversion ratio and the alpha parameter of the Gamma distribution by maximum likelihood (ML), nucleotide frequencies are estimated by ML.-->

<!--phyml --help-->

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -m HKY85 -f e -a e -t e -u /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.newick -o n-->

<!--phyml -i /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -t e -u /Users/pece/Repositories/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.newick -o n-->

----



