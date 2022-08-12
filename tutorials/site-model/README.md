# Site model in CodeML

## Motivation

In this tutorial we will use CodeML - a program from the PAML package from Ziheng Yang - to check for selection among different sites of the alignment. We will use a dataset that was previously published and try to recreate existing results.

## Data

For this tutorial we will use an alignment of the β globin gene from 17 vertebrate species. This dataset was analised for signs of selection by [Yang et al., 2000](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461088/).

For such analyses we need an alignment of homologous protein-coding DNA sequences that start with the 1st codon position and end with a 3rd. We will use an alignment file in PhyLip format, `bglobin.phy`, and the corresponding phylogenetic tree file, `bglobin.trees`.

The files are available on the left-hand panel under the heading **Data**.


## Setting up the analysis with CodeML

CodeML is a part of the software package PAML that allows you to use codon models to detect selection on protein-coding genes. Unlike PhyML, CodeML works with control files rather than command line options. 

For this tutorial you will first need to understand the control file options that CodeML provides. These options are described in the PAML package [documentation](http://abacus.gene.ucl.ac.uk/software/pamlDOC.pdf), available from the PAML [website](http://abacus.gene.ucl.ac.uk/software/paml.html).

One important recommendation is to start with an existing control file and modify it to suit your needs. More often than not wtiting a file like that from scratch will be more trouble than it's worth.

You will need to set up several runs with the same input files.

### Analysis runs

Set up CodeML to analyse the given alignment and tree under the **M0**, **M3**, **M7**, **M8** and **M8a** models.

For the **M3** model use 3 rate categories.

The **M8a** model is the same as **M8**, but with one of the **ω** fixed to 1. This means that you will use the  `NSsites = 8` control file option, and use  `fix_omega = 1`.

Set the codon frequencies to the **F3X4** model, use the **no clock, unrooted tree** option and let CodeML estimate the substitution model parameters **κ** and **ω**.

In this run, allow CodeML to estimate the branch lengths of the tree using the branch lengths from the provided tree file as initial values.

> - Which of the models defined by this run are nested?
> - Write a control file to run CodeML with the specified settings;
> - Run CodeML in console.

## Interpreting the results

Now that you ran all the analyses, open the statistics files from the runs. Study the output of the runs and try to answer the following questions:

> - Perform likelihood ratio tests on the nested models.
> - Does the data exhibit a strong variation in the ω rates (test for **M0** vs **M3**)?
>
> - Compare results from the LRT between **M7** and **M8** and the LRT between **M8a** and **M8**. Are they both significant (or both non-significant)?
> - If LRTs suggest positive selection, which sites are inferred to be under positive selection (model **M8**)? Use the Bayes Empirical Bayes estimates and find the sites for which ω is strictily above 1.
> - Compare your results to the analyses of this dataset (**D2** in the paper) in the original PAML [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461088/). Do your observations agree with those of Yang et al.?

Example output files are provided on the left-hand panel, under the heading **Output from CodeML v4.10.0**.

## Answers
