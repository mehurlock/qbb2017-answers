#!/usr/bin/env python

"""
Usage: ./CTCF_interactions.py <enrichment_heat.npz> <protein_binding_peaks.tsv> <Hi-C_primer_file.bed>
"""

import sys
import numpy

data=numpy.load(sys.argv[1])
ctcf=open(sys.argv[2])
bed=open(sys.argv[3])
ctcf_list=[]

#Pull the CTCF-binding sites within the primer sequencing range
for line in ctcf:
    if line.startswith("chrX"):
        line=line.split("\t")
        value = int(line[1])
        if value > 98831147 and value < 103425148:
            ctcf_list.append(int(line[1]))

#Pull the primer names to a dictionary based on their strands. Counter sets their position in the list for future indexing.            
plus_strand={}
minus_strand={}
plus = 0
minus = 0
for line in bed:
    if line.startswith("#"):
        continue
    else:
        line=line.split("\t")
        if line[5] == "+":
            plus_strand[plus]=line[3]
            plus += 1
        elif line[5] == "-":
            minus_strand[minus]=line[3]
            minus += 1
        else:
            print line [1] + "Error"

#Scan the primer fragments of the heat file to file to find coverage that includes CTCF-binding sites. Record the position in the iteration for later calling for primer identification.
forward_hits=[]
forward_frag=[]
reverse_hits=[]
reverse_frag=[]            
forward_count = 0
reverse_count=0
for forward in data['0.forward']:
    frag = range(forward[0], forward[1]+1)
    for value in frag:
        if value in ctcf_list:
            forward_hits.append(value)
            forward_frag.append(forward_count)
    forward_count += 1
for reverse in data['0.reverse']:
    frag = range(reverse[0], reverse[1]+1)
    for value in frag:
        if value in ctcf_list:
            reverse_hits.append(value)
            reverse_frag.append(reverse_count)
    reverse_count += 1

#Search the enrichment array to find the highest correlation pairs between forward fragments and reverse fragments. Put the highest interactions into a dictionary where the forward primer index is the key and the reverse primer key is a tuple with the enrichment value.
enrichment_pairs={}
for fkey in forward_frag:
    temp=0
    for rkey in reverse_frag:
        en = data['0.enrichment'][fkey][rkey]
        if en > temp:
            temp = en
            enrichment_pairs[fkey]=(rkey, temp)
 
#Write a file displaying the highest forward and reverse primer fragment pairs using the enrichment dictionary.           
file = open("Fragment_Interactions.txt", "w")
file.write("Primer Fragment Interaction Table \n")
file.write("Forward Primer \t Reverse Primer \n")
for key in enrichment_pairs:
    fkey=key
    rkey=enrichment_pairs[key][0]
    file.write(plus_strand[fkey] + "\t" +  minus_strand[rkey] + "\n")
file.write("\n *Note: It appears that the bed file containing the primers has some uncovered regions. This means 4 CTCF binding sites have no corresponding Hi-C reads. The primer interactions may be inaccurate.")
file.close()





