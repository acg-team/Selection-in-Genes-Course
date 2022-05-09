# Simple codon model in CodeML

## Motivation

Detecting selection is a powerful tool to increase our understanding of evolution. To start off easy, we will first run an analysis with the simple one ratio model, one that assumes the same selective pressure on all sites and throughout time. 

In this tutorial we will use CodeML -- a program from the PAML package from Ziheng Yang -- to detect whether a specific gene is under selection. We will use a dataset that was previously published and try to recreate existing results.

## Data

For this tutorial we will use an alignment file of 13 HIV *env* gene sequences from Sweden. This dataset was first published in 1997 [[Leitner et al., 1997](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC191698/)], and is quite unique as the transmission history is exactly known for these samples. This same dataset was later analised for signs of selection by [Yang et al., 2000](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461088/).

For such analyses we need an alignment of homologous protein-coding DNA sequences that start with the 1st codon position and end with a 3rd. We will use an alignment file in PhyLip format, `HIVenvSweden.phy`, and the corresponding phylogenetic tree file, `HIVenvSweden.trees`.

The files are available on the left-hand panel under the heading **Data**.


## Setting up the analysis with CodeML

CodeML is a part of the software package PAML that allows you to use codon models to detect selection on protein-coding genes. Unlike PhyML, CodeML works with control files rather than command line options. 

For this tutorial you will first need to understand the control file options that CodeML provides. These options are described in the PAML package [documentation](http://abacus.gene.ucl.ac.uk/software/pamlDOC.pdf), available from the PAML [website](http://abacus.gene.ucl.ac.uk/software/paml.html).

One important recommendation is to start with an existing control file and modify it to suit your needs. More often than not wtiting a file like that from scratch will be more trouble than it's worth.

You will need to set up two runs with the same input files.

### First run

Set up CodeML to analyse the given alignment and tree under the **M0** model.

<!--Codon model to use? F1X4?-->

In this run, fix the branch lengths of the tree to the ones given by the input file.

<!--No clock, unrooted tree, fixed branch lengths?-->

Additionally, set the name of the output file to `HIVenvSweden_M0_fixedbranches`

> - Write a control file to run CodeML with the specified settings;
> - Run CodeML in console.

### Second run

<!--Does the second run make sense at all?-->

Set up CodeML to analyse the given alignment and tree under the **M0** model.

<!--Codon model to use? F1X4?-->

In this run, allow CodeML to estimate the branch lengths of the tree.

<!--Clock, rooted tree, initial branch lengths?-->

Additionally, set the name of the output file to `HIVenvSweden_M0_MLbranches`

> - Write a control file to run CodeML with the specified settings;
> - Run CodeML in console.

## Interpreting the results

Now that you ran both analyses, open the statistics files from the two runs. Study the output of the runs and try to answer the following questions:

> - Among the two runs, when is the log-likelihood higher? Why do you think it is?
> - In the run with estimated branch lengths, do you observe codon usage bias?
> -  Study the statistics of nucleotide usage for different codon positions. Which position displays the most bias? Why?
> - What is the ML estimate of the transition-transversion ratio κ? 
> - What is the ML estimate of the ω-ratio? How would you interpret these ML estimates?
> - Compare your results to the analyses of this dataset in the original PAML [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1461088/) (it is dataset D10). Do your observations agree with those of Yang et al.?

Example output files are provided on the left-hand panel, under the heading **Output**.

<!--How to read off codon usage bias?-->
