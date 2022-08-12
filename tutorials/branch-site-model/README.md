# Branch-site model in CodeML

## Motivation

In this tutorial we will use CodeML - a program from the PAML package from Ziheng Yang - to check for site-specific selection along a foreground branch using a branch-site model. We will use a dataset that was previously published and try to recreate existing results.

## Data

For this tutorial we will use a small dataset of lysozyme sequences from primates, previously analysed in [Yang, 1998](https://academic.oup.com/mbe/article/15/5/568/987857?login=false). We will use a 7-species subset that represents the four major primate lineages of the phylogeny to save time on the analyses.

For such analyses we need an alignment of homologous protein-coding DNA sequences that start with the 1st codon position and end with a 3rd. We will use an alignment file in PhyLip format, `lysozymeSmall.phy`, and the corresponding phylogenetic tree file, `lysozymeSmall.newick`.

The files are available on the left-hand panel under the heading **Data**.


## Setting up the analysis with CodeML

CodeML is a part of the software package PAML that allows you to use codon models to detect selection on protein-coding genes. The control file options you need to set for your analyses are described in the PAML package [documentation](http://abacus.gene.ucl.ac.uk/software/pamlDOC.pdf), available from the PAML [website](http://abacus.gene.ucl.ac.uk/software/paml.html).

In this tutorial, we will run the LRT for branch-site positive selection. For this test we have to first define the foreground and background branches in the phylogenetic tree of given sequences. Only the foreground branches may experience positive selection. In this analysis we have a biological hypothesis for what branches may experience positive selection (*Colobine* monkeys), however this might not always be the case. When no biological hypothesis is available to select foreground branches, apossible approach is to test several or all branches on the tree, treating every branch  in turn as the foreground branch. However, if we run such tests we need to apply multiple testing correction as the probability of rejecting falsely at least one of the hypotheses can be high (see [Anisimova and Yang. 2007](https://academic.oup.com/mbe/article/24/5/1219/1041272?)).

You will set up an analysis that treats the branch leading to the *Colobine* clade (in our case the *Colobine* clade is represented by two sequences, `Cgu/Can_co` for *Angolan colobus* and `Pne_langur` for *Douc langur*) as foreground.

<!--You can then try to the LRTs on all the branches in the tree and see whether the results correspond to what you expect.-->

### Testing the Colobine clade

Set up CodeML to analyse the lysozyme alignment using the branch-site **model A**, the alternative hypothesis, and **model A1**, the null hypothesis that disallows positive selection.

**Model A** divides the sites into 4 classes, conserved (0 < ω<sub>0</sub> < 1), neutral (ω<sub>1</sub> = 1) and two variable classes on the foreground branch with ω<sub>2</sub> ≥ 1, indicating possible positive selection. All of these classes are defined by two proportions p0 and p1 that are estimated from the data.

**Model A1** has a similar setup but restricts ω<sub>2</sub> = 1, meaning that no sites with positive selection are allowed at the foreground branch.

Set the codon frequencies to the **F3X4** model, use the **no clock, unrooted tree** option and let CodeML estimate the substitution model parameters **κ**, and **ω** values.

Let CodeML estimate the branch lengths of the tree.

> - Label the branch leading to the *Colobine* clade in the tree file with a tag;
> - Write a control file to run the analysis using **model A** in CodeML;
> - Write a control file to run the analysis using **model A1** in CodeML;
> - Run CodeML in console.

## Interpreting the results

Now that you ran both analyses, open the statistics files from the runs. Study the output of the runs and try to answer the following questions:

> - Does the LRT for positive selection indicate positively selected sites on the foreground branch?
> - Are the results of the LRT consistent with the results of the analysis of this dataset from the previous tutorial on branch models?
> - Compare your results to the analyses of this dataset in the original [paper](https://academic.oup.com/mbe/article/22/12/2472/1009544?login=false). Do your observations agree with those of Zhang et al.?

Example output files are provided on the left-hand panel, under the heading **Output from CodeML v4.10.0 **.

## Answers
