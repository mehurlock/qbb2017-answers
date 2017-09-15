#!/usr/bin/env python

"""
Usage: ./target_dna_extractor <dna output from fasta_converter.py> <protein output from Fasta_converter.py>

-Extracts query dna sequence from a list of sequences adapted from a FASTA file
"""

import itertools
import sys

total_dna=open(sys.argv[1])
total_prot=open(sys.argv[2])
query_dna=open("query_dna.out", "w")
query_prot=open("query_prot.out", "w")

for i in range(1,2):
    line_d = total_dna.next().strip()
    query_dna.write(line_d)
    
for i in range(1, 2):
    line_p=total_prot.next().strip()
    query_prot.write(line_p)