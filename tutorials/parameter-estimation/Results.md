### Setting the parameters

To get the help message, run `phyml -h` in the console.

> - Find out how to provide the input alignment file and specify the data type (nucleotide sequences in a sequential format);

The input alignment is provided using the `-i` argument followed by the path to the MSA file, e.g. `-i /path/to/course/tutorials/parameter-estimation/data/primates-nt.phy`.

We specify the data type using the `-d` argument followed by the data type, e.g. `-d nt` for nucleotide data (the other options are `aa` for amino-acids and `generic`).

Finally, we use the `-q` flag to indicate the the MSA file is in sequential, rather than interleaved, format.

> - Find out how to set the evolutionary model;

The evolutionary model is set using the `-m` argument followed by the model name or description, e.g. `-m HKY85` (other options include JC69, K80, GTR, etc. for nucleotides and LG, WAG, JTT, etc. for amino-acids).

> - Find out how to set the way stationary nucleotide frequencies are estimated (empirical or maximum likelihood (ML) estimates);

The stationary frequencies can be set with the `-f` argument followed by estimation technique or exact values, if known, e.g. `-f e` for empirical estimates and `-f o` for frequencies estimated by ML.

> - Find out how to provide a user-specified tree;

We set the tree using the `-u` argument followed by the path to the tree file, e.g. `-u  /path/to/course/tutorials/parameter-estimation/data/primates-nt.newick`.

> - Find out how to disable tree topology and branch optimization;

We can restrict optimisation to specific parameters using the `-o` argument followed by a letters encoding which parameters you want to optimise, e.g. `-o r` means that PhyML will only optimise the different rate parameters, but not the tree topology or branch lengths. Other options are e.g. to optimise the tree topology and branch lengths, but not the rates (`-o tl`), to disable parameter optimisation altogether (`-o n`), and others.

> - Find out how to set the run ID so that you can distinguish the output from the two runs.

You can set the run ID using the `--run_id` argument followed by a text ID of your choice, e.g. `--run_id empirical_frequencies`.

### Commands for all runs

In case you would like to compare your commands to the ones that were used to produce the given results, the commands are given below (adjust the file paths according to where you stored the files).

`phyml -i /path/to/course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/parameter-estimation/data/primates-nt.newick -m HKY85 -f m -a e -t e -v 0 -o r --run_id ml`

`phyml -i /path/to/course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/parameter-estimation/data/primates-nt.newick -m HKY85 -f e -a e -t e -v 0 -o r --run_id empirical`

### Answers to the tutorial questions

#### Interpreting statistics

The first questions have to be answered using the statistics files from the two runs.

We can use a snippet (header and footer removed) of the output for ML frequency estimates as an example:

``` oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
. Sequence filename: 			primates-nt.phy
. Data set: 				#1
. Initial tree: 			user tree (/Users/pece/Repositories/Selection-in-Genes-Course/tutorials/parameter-estimation/data/primates-nt.newick)
. Model of nucleotides substitution: 	HKY85
. Number of taxa: 			20
. Log-likelihood: 			-6172.58105
. Unconstrained log-likelihood: 	-5060.29926
. Composite log-likelihood: 		-41518.55490
. Parsimony: 				739
. Tree size: 				0.54587
. Discrete gamma model: 		Yes
  - Number of classes: 			4
  - Gamma shape parameter: 		0.555
  - Relative rate in class 1: 		0.04403 [freq=0.250000] 		
  - Relative rate in class 2: 		0.28647 [freq=0.250000] 		
  - Relative rate in class 3: 		0.85666 [freq=0.250000] 		
  - Relative rate in class 4: 		2.81284 [freq=0.250000] 		
. Transition/transversion ratio: 	3.251070
. Nucleotides frequencies:
  - f(A)=  0.29344
  - f(C)=  0.21764
  - f(G)=  0.25591
  - f(T)=  0.23301

. Run ID:				ml
. Random seed:				1651861751
. Subtree patterns aliasing:		no
. Version:				3.3.20220408
. Time used:				0h0m0s (0 seconds)
```

> - What are the important values in these files?

For sanity checks we can use the first parameters which define the filename of the MSA file, the input tree, model of evolution and the number of taxa. All these values should match the parameters you intended to set (e.g. the model should be HKY85).

To interpret the results of the analysis we need to pay attention to the Log-likelihood (-6172.581 in this case) and parameter estimates. In this case we can see the estimates for the gamma shape parameter (0.555), the transition-transversion ratio (3.251) and the nucleotide frequencies (0.293, 0.218, 0.256, 0.233).

> - Is there any difference between the stationary frequencies between the two runs?

The empirical stationary frequencies were estimated as (0.285, 0.213, 0.258, 0.244), while using ML we got (0.293, 0.218, 0.256, 0.233). While the stationary frequencies are different, they are not glaringly different.
> - Is there a difference in the likelihood?

The likelihood for the analysis with empirical stationary frequencies is -6173.496, and the likelihood with frequencies estimated by ML is -6172.581. The difference between the two likelihood values is 0.915, which is negligible in comparison to the scale of the values.

> - Which estimation option is better and why do you think so?

Depending on the dataset one or the other option will make the most sense. For recently diverged organisms we can safely assume that the empirical frequencies are a good representation of the true stationary frequencies, as in this case. We can conclude this also from the fact that the values are not dramatically different between the two runs. This can save us some computation and reduces the number of parameters that we need to infer.

On the other hand, if we know that the stationary frequencies for a given dataset might differ from empirical, e.g. if the dataset is not a representative sample of the population, it might make sense to estimate them using ML. However, this is a very hard question to answer in general and the answer depends on your knowledge of the specific dataset you are working on. Moreover, accurate estimation of frequencies in such a case is a lot to expect from a piece of software that only works on the data provided. So, in case you are certain that the stationary frequencies are indeed different to the ones you can deduce from the data, a better strategy might be to provide them to the software as fixed values.

#### Interpreting trees

The last questions have to be answered using the tree files from the two runs.

We can use the tree from the analysis with ML-estimated frequencies as an example:

![](https://github.com/acg-team/Selection-in-Genes-Course/raw/gh-pages/tutorials/parameter-estimation/figures/tree.png)



> - Are these trees different to one another and to the input tree?

They are not.

> - Should they actually be different?

The trees should not be different, neither in topology nor in branch lengths as we have disabled optimisation of both. The analyses should have run on the fixed input tree.

### Checking against the PhyML GUI

To check that you set the exact same parameters in the GUI as in the command line, you can try running the two analyses with the same random seed number. The random seed is what is used to start the pseudo-random number generation in your computer, so chances are that if you set all parameters to the same values and fix the seed you will get an identical replicate of your other analysis.

Unfortunately you cannot set the seed in the GUI, so you will have to run the analysis with the GUI first, then copy the seed used in that run and use it for the console command.

To make your task easier, here are the commands that set the right parameters (adjust the file paths according to where you stored the files and set the seed):

`phyml -i /path/to/course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/parameter-estimation/data/primates-nt.newick -m HKY85 -f m -a e -t e -v 0 -o r --run_id ml --r_seed 1651861751` 

`phyml -i /path/to/course/tutorials/parameter-estimation/data/primates-nt.phy -d nt -q -u /path/to/course/tutorials/parameter-estimation/data/primates-nt.newick -m HKY85 -f e -a e -t e -v 0 -o r --run_id empirical --r_seed 13`
