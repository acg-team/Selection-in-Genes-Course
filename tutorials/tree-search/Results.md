### Commands for all runs

In case you would like to compare your commands to the ones that were used to produce the given results, the commands are given below (adjust the file paths according to where you stored the files).

`phyml -i /path/to/course/tutorials/tree-search/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -t e -v 0 -o r --run_id bionj`

`phyml -i /path/to/course/tutorials/tree-search/data/primates-nt.phy -d nt -q -m HKY85 -f m -a e -t e -v 0 -o tlr --run_id ml_tree`

### Answers to the tutorial questions

#### Interpreting statistics

The first questions have to be answered using the statistics files from the two runs.

> - Are the parameter estimates different?

| Parameter                             | BioNJ tree | ML tree |
| ------------------------------------- | ---------- | ------- |
| **Gamma shape (α)**                   | 0.555      | 0.555   |
| **Transition/transversion ratio (κ)** | 3.234      | 3.251   |
| **f(A) (π<sub>Α</sub>)**              | 0.293      | 0.293   |
| **f(C) (π<sub>C</sub>)**              | 0.218      | 0.218   |
| **f(G) (π<sub>G</sub>)**              | 0.255      | 0.256   |
| **f(T) (π<sub>T</sub>)**              | 0.234      | 0.233   |

The different parameter estimates are sligthly different between two runs, however the largest difference is at most 0.02 (between the estimates of the transition/transversion ratios).

> - Is there a difference in the likelihood between the two runs?

The likelihood of the BioNJ tree is -6181.134, and the likelihood for the ML-estimated tree is -6172.580. The likelihood for the ML-estimated tree is higher, as expected.

#### Interpreting trees

The last questions have to be answered using the tree files from the two runs.

<figure>
  <img src="https://github.com/acg-team/Selection-in-Genes-Course/raw/gh-pages/tutorials/tree-search/figures/trees.png" alt="Left: BioNJ tree, right: ML tree" style="width:90%">
  <figcaption align = "center" style="width:90%"> <br>Left, the BioNJ tree computed by PhyML. Right, the tree estimated by PhyML using ML.</figcaption>
</figure>


> - Are these trees different to one another?

Between the two runs, while the topologies of the trees are almost the same, the branch lengh estimates are quite different. We can see this based on the scale that is shown on the tree figures, the BioNJ tree is scaled in 0.02 units, while the ML tree is scaled in 0.03 units. Moreover, the total tree length is 0.490 for the BioNJ tree, and 0.546 for the ML tree.

We can also observe minor differences in topologies. For example, in the BioNJ tree DLangur and Colobus sequences are grouped together in a clade, while in the ML tree they are not. Moreover, in the BioNJ tree Squirrel, Tamarin, PMarmoset, Saki and Titi sequences form a clade, while in the ML tree these sequences are in a clade with Spider, Woolly and Howler sequences.

> - Where do the differences come from?

The two trees are estimated using very different methods. BioNJ is a distance-based clustering method with linear computational complexity. It is a greedy clustering approach that only takes into account pairwise distances between sequences. This method is known to be statistically consistent under some conditions, however these conditions are rarely satisfied in real life.

On the other hand, while for such a small dataset the ML tree estimation is also fast, this method is technically NP-complete. Maximum likelihood tree search in its pure form is intractable on datasets of any size greater than 10. However, due to the efficient heuristics that PhyML uses, we can reconstruct a good tree in a reasonable amount of time. The ML reconstruction properly accounts for the evolution of molecular sequences, using an evolutionary model to find the best known fitting tree. Since it is not based on pairwise distances, it also accounts for lineages sharing evolutionary history. This makes ML tree search the preferred method of tree inference over much faster distance-based methods.
