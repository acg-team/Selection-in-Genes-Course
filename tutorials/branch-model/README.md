# Branch model in CodeML

## Motivation

In this tutorial we will use CodeML - a program from the PAML package from Ziheng Yang - to check for selection along different branches of a tree. We will use a dataset that was previously published and try to recreate existing results.

## Data

For this tutorial we will use a small dataset of lysozyme sequences from primates, previously analysed in [Yang, 1998](https://academic.oup.com/mbe/article/15/5/568/987857?login=false). We will use a 7-species subset that represents the four major primate lineages of the phylogeny to save time on the analyses.

For such analyses we need an alignment of homologous protein-coding DNA sequences that start with the 1st codon position and end with a 3rd. We will use an alignment file in PhyLip format, `lysozymeSmall.phy`, and the corresponding phylogenetic tree file, `lysozymeSmall.trees`.

The files are available on the left-hand panel under the heading **Data**.


## Setting up the analysis with CodeML

CodeML is a part of the software package PAML that allows you to use codon models to detect selection on protein-coding genes. The control file options you need to set for your analyses are described in the PAML package [documentation](http://abacus.gene.ucl.ac.uk/software/pamlDOC.pdf), available from the PAML [website](http://abacus.gene.ucl.ac.uk/software/paml.html).

You will need to set up three different runs with the same input files.

### First run

Set up CodeML to analyse the lysozyme alignment under the free ratio model for branches, meaning that each branch in the tree can have its own <img src="https://render.githubusercontent.com/render/math?math=d_n/d_s"> ratio **ω**.

Set the codon frequencies to the **F3X4** model, use the **no clock, unrooted tree** option and let CodeML estimate the substitution model parameters **κ** and, of course, all the different **ω** values for each branch.

Let CodeML estimate the branch lengths of the tree.

Additionally, set the name of the output file to `lysozymeSmall_freeratio.txt`

> - Write a control file to run CodeML with the specified settings;
> - Run CodeML in console.

### Second run

Set up CodeML to analyse the lysozyme alignment only allowing 2 different <img src="https://render.githubusercontent.com/render/math?math=d_n/d_s"> ratios, one for all branches of the tree and one for a specific branch leading to the *Colobine* clade (in our case the *Colobine* clade is represented by two sequences, `Cgu/Can_co` for *Angolan colobus* and `Pne_langur` for *Douc langur*). To do so, you will have to label the branch in the tree file with a tag, e.g. `#1`. 

Set the codon frequencies to the **F3X4** model, use the **no clock, unrooted tree** option and let CodeML estimate the substitution model parameters **κ** and the two different **ω**.

Let CodeML estimate the branch lengths of the tree.

Additionally, set the name of the output file to `lysozymeSmall_tworatios.txt`

> - Write a control file to run CodeML with the specified settings;
> - Run CodeML in console.

### Third run

Set up CodeML to analyse the lysozyme alignment allowing 3 different <img src="https://render.githubusercontent.com/render/math?math=d_n/d_s"> ratios, one special branch as defined in the previous run for the *Colobine* clade, and another leading to the *Hominoid* clade, in this dataset represented by `Hsa_Human_` for *Human* and `Hla_gibbon` for *Lar Gibbon*. To do so, you will have to label a second branch in the tree file with a tag different from the previous one, e.g. `#2`. 

Set the codon frequencies to the **F3X4** model, use the **no clock, unrooted tree** option and let CodeML estimate the substitution model parameters **κ** and the two different **ω**.

Let CodeML estimate the branch lengths of the tree.

Additionally, set the name of the output file to `lysozymeSmall_threeratios.txt`

> - Write a control file to run CodeML with the specified settings;
> - Run CodeML in console.

## Interpreting the results

Now that you ran all analyses, open the statistics files from the three runs. Study the output of the runs and try to answer the following questions:

> - Based on LRTs, what model fits your data the best (among two-ratio, three-ratio and free-ratio models)?
> - What are the estimates of ω from the best model? What can you conclude from them?
> - Compare your results to the analyses of this dataset in the original [paper](https://academic.oup.com/mbe/article/15/5/568/987857?login=false). Do your observations agree with those of Yang?

Example output files are provided on the left-hand panel, under the heading **Output**.

## Answers
