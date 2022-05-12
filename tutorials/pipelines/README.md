# Recreating a part of an existing pipeline

## Data

For this tutorial you will use a subset of the major histocompatibility complex class I (MHC-I) sequences from bird species that were studied in the publication by [O'Connor et al., 2018](https://www.nature.com/articles/s41559-018-0509-3).

The `phylip` MSA files are available in a zip archive on the left-hand panel under the heading **Data**.

## Analysis 

Set up an analysis pipeline on you machine (or cluster if you have access to one) that can process the sequence data files sequentially.

1. Run PhyML on each sequence file under the **HKY85+G** model. Use your better judgement to set the model parameters appropriately;
2. Run CodeML on the sequence files and the trees inferred by PhyML. In this case you will need to run the site models to come to a decision on whether you see traces of positive selection for each of the species;
3. Summarise your output;
4. Profit (;
