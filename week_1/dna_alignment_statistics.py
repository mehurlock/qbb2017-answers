#!/usr/bin/env python

"""
Usage: ./dna_alignment_statistics <dna output from fasta_converter.py> <dna output from target_extractor.py> <protein output from fasta_converter.py> <protein output from target_extractor.py>

-Iterate the input total dna file and query dna file to see where codons have been mutated
-Count the number of synonymous mutations (dS) and non-synonymous mutations (dN)
-Run statistical comparisons of the dN/dS and dN-dS
-Generate plots of interesting statistical comparisons
"""

import itertools
import sys
import fasta
import collections
import matplotlib.pyplot as plt
import numpy as py

tot_dna=open(sys.argv[1])
query_dna=open(sys.argv[2])
tot_prot=open(sys.argv[3])
query_prot=open(sys.argv[4])

empty=[]
prot_align={}
target_prot=[]

#Generate a dictionary of lists of proteins in the protein sequence alignment
count_1 = 0
for line in tot_prot:
    line=line.rstrip("\r\n")
    blank=[]
    for i in line:
        blank.append(str(i))
    prot_align[count_1]=blank
    count_1 += 1

#Generate a list of amino acids from the query protein    
for line in query_prot:
    line=line.rstrip("\r\n")
    for i in line:
        target_prot.append(str(i))

#Generate a list of codons from the query sequence    
for line in query_dna:
    line=line.rstrip("\r\n")
    for i in range(0, (len(line)/3)-1):
        codon=str(line[3*i:(3*i)+3])
        empty.append(str(codon))

#Generate a dictionary where comparisons of codons will be stored as lists of "N" ad "S"
comp_dict={}
for num in range(0, len(empty)-1):
    variable=comp_dict[num]=[]
   
count_2=0

#Iterate the total DNA file to check if codons in each homologous sequence match the relevant codon in the target sequence>
for line in tot_dna:
    line=line.rstrip("\r\n")
    for i in range(0, len(empty)-1):
        codon=str(line[3*i:(3*i)+3])
        l=[]
        if empty[i]=="---":
            continue
        elif codon=="---":
            continue
        elif codon == empty[i]:
            continue
        elif prot_align[count_2][i]!=target_prot[i]:
            comp_dict.setdefault(i, []).append("N")
        elif prot_align[count_2][i]==target_prot[i]:
            comp_dict.setdefault(i, []).append("S")
        else:
            print "Error"
    count_2 += 1

non_zero_n=[]
non_zero_s=[]

#Compile a dictionary of the difference of the number of N's and S's for each codon location from the iteration  
diff_dict={}
for key in comp_dict:
    n_count=0
    s_count=0
    for value in comp_dict[key]:
        if value == "N":
            s_count += 1
        else:
            n_count += 1
    diff_dict[key]=n_count-s_count
    non_zero_n.append(n_count+1)
    non_zero_s.append(s_count+1)

#Generate a list of amino acid number and dN-dS, respectively, for a relative plot    
final_aa=[]
final_diff=[]
total=0
for key in diff_dict:
    final_aa.append(key)
    final_diff.append(diff_dict[key])
    total += diff_dict[key]

#Calculate statistics for the dN-dS data
mean=py.mean(final_diff)
std_dev=py.std(final_diff)
std_error=std_dev/py.sqrt(len(final_diff)+1)
zscore=mean/std_dev

#Calculate zscore for every position in the dN-dS data
zscore_list=[]
for i in final_diff:
    zscore_list.append(float(i)/float(std_dev))

#Translates dN and dS lists to a combined log2(dN/dS)    
log_function=[py.log2(float(n)/float(s)) for n, s in zip(non_zero_n, non_zero_s)]

#Make a list of significant and non-significant values
signif=[]
graph_log=[]
for i in range(len(log_function)):
    signif.append(None)
    graph_log.append(None)

for i in range(len(log_function)):
    if log_function[i] > py.log2(779):
        signif[i]=log_function[i]
    elif log_function[i] < py.log2(float(1)/float(779)):
        signif[i]=log_function[i]
    else:
        graph_log[i]=log_function[i]
        
non_zero=[float(n)/float(s) for n,s in zip(non_zero_n, non_zero_s)]

mean_non=py.mean(non_zero)
std_dev_non=py.std(non_zero)
std_error_non=std_dev_non/py.sqrt(len(non_zero))
zscore_non=(mean_non)-1/std_error_non

#log2(dN/dS) plot
plt.figure()
plt.scatter(range(len(graph_log)), graph_log, alpha=.5, c="blue")
plt.scatter(range(len(signif)), signif, alpha=.7, c="red")
plt.xlabel("Codon Number")
plt.ylabel("log2(dN/dS)")
plt.title("Comparison of Codon Mutations Across Homologs of WNFCG")
plt.savefig("scatter_plot.png")
plt.close()

#zscore plot
plt.figure()
plt.scatter(range(len(zscore_list)), zscore_list, alpha=.3)
plt.xlabel("Codon Number")
plt.ylabel("zscore")
plt.title("Z-score Data for Codons Across Homologs of WNFCG")
plt.savefig("zscore.png")
plt.close

#Bar graph showing distribution of dN-dS for each codon            
plt.figure()
plt.bar(final_aa, final_diff, color='b')
plt.xlabel("Amino Acid Number")
plt.ylabel("dN-dS")
plt.title("Comparison of Codon Mutations Across Homologs of WNFCG")
plt.savefig("dN_dS_distribution.png")
plt.close()
            
            
            
            
            
            
            
            
            
            
            
            
                     
            
            
            
            