#!/usr/bin/env python3

from glob import glob
from os import makedirs, rename
from os.path import isfile, join, exists, basename

from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment

from subprocess import run, PIPE, Popen

from scipy.stats import chi2

def make_if_not_exists(dir_path):
    if not exists(dir_path):
        makedirs(dir_path)
        print("Directory creates {}".format(dir_path))
    else:
        print("Directory exists {}".format(dir_path))
    print()

def fasta_to_phylip(fasta_dir, phylip_dir):
    fasta_file_list = glob(join(fasta_dir, "*.fas"))
    for fasta_file in fasta_file_list:
        species_name = basename(fasta_file).split(".")[0]
        phylip_file = join(phylip_dir, "{}.phy".format(species_name))
        with open(fasta_file, "r") as fasta_handle:
            alignment = AlignIO.read(fasta_handle, "fasta")
            with open(phylip_file, "w") as phylip_handle:
                AlignIO.write(alignment, phylip_handle, "phylip-sequential")

def infer_trees(phyml_exec, phylip_dir, tree_dir):
    phyml_command = [phyml_exec, "-i"]
    phyml_params = ["-d", "nt", "-m", "HKY85", "-a", "e", "-v", "e", "-o", "tlr", "-f", "e"]
    phylip_file_list = glob(join(phylip_dir, "*.phy"))
    for phy_file in phylip_file_list:
        full_command = phyml_command + [phy_file] + phyml_params
        out = run(full_command)
        species_name = basename(phy_file).split(".")[0]
        stats_file = "{}_phyml_stats.txt".format(phy_file)
        tree_file = "{}_phyml_tree.txt".format(phy_file)
        rename(stats_file, join(tree_dir, "{}_stats.txt".format(species_name)))
        rename(tree_file, join(tree_dir, "{}.newick".format(species_name)))

def run_codeml(codeml_exec, phylip_dir, tree_dir, ctrl_file_template, out_dir):
    phylip_file_list = glob(join(phylip_dir, "*.phy"))
    for phy_file in phylip_file_list:
        species_name = basename(phy_file).split(".")[0]
        control_file_name = join(out_dir, "{}_{}".format(species_name, basename(ctrl_file_template)))
        with open(ctrl_file_template, 'r') as template_handle:
            content = template_handle.read()
            with open(control_file_name, 'w') as control_handle:
                l = "seqfile = {}\n".format(phy_file)
                control_handle.write(l)
                l2 = "treefile = {}\n".format(join(tree_dir, "{}.newick".format(species_name)))
                control_handle.write(l2)
                l3 = "outfile = {}\n".format(join(out_dir, "{}_{}.txt".format(species_name,
                                                                          basename(ctrl_file_template).split(".")[0])))
                control_handle.write(l3)
                control_handle.writelines(content)
        full_command = [codeml_exec, basename(control_file_name)]
        print("Starting with analysis for {}".format(control_file_name))
        out = run(full_command, cwd=out_dir)
        print("Done with analysis for {}".format(control_file_name))
    print()

def parse_codeml_output(out_file):
    np = 0
    lik = 0
    with open(out_file, "r") as handle:
        for line in handle:
            if "lnL" in line:
                np = int(line.split()[3][:-2])
                lik = float(line.split()[4])
    return(np, lik)

def read_likelihoods(out_dir):
    M0_out_file_list = glob(join(out_dir, "*M0.txt"))
    for M0_file in M0_out_file_list:
        species_template  = basename(M0_file)[:-7]
        print("Likelihoods for {} species".format(species_template[:-7]))
        M0_np, M0_lik = parse_codeml_output(M0_file)
        M3_file = join(out_dir, "{}_M3.txt".format(species_template))
        M3_np, M3_lik = parse_codeml_output(M3_file)
        
        print("M0 np {}".format(M0_np))
        print("M0 lik {}".format(M0_lik))
        print("M3 np {}".format(M3_np))
        print("M3 lik {}".format(M3_lik))
    
        LRT = 2*(M3_lik - M0_lik)
        print("LRT {}".format(LRT))
        print("p-value {}".format(1 - chi2.cdf(LRT, M3_np - M0_np)))
        print()
    
if __name__ == "__main__":
    base_dir = "/Users/pece/Repositories/Selection-in-Genes-Course/tutorials/pipelines/"
    phylip_dir = join(base_dir, "data/phylip")
    tree_dir = join(base_dir, "data/trees")
    out_dir = join(base_dir, "data/out")

    phyml_exec = "phyml"
    codeml_exec = "/Users/pece/Repositories/paml/bin/codeml"
    M0_ctrl_file_template = join(base_dir, "data/codeml_M0.ctl")
    M3_ctrl_file_template = join(base_dir, "data/codeml_M3.ctl")

    make_if_not_exists(tree_dir)
    make_if_not_exists(out_dir)
    
    infer_trees(phyml_exec, phylip_dir, tree_dir)

    run_codeml(codeml_exec, phylip_dir, tree_dir, M0_ctrl_file_template, out_dir)
    run_codeml(codeml_exec, phylip_dir, tree_dir, M3_ctrl_file_template, out_dir)
    
    read_likelihoods(out_dir)
    
