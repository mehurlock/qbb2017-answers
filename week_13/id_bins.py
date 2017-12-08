#!/usr/bin/env python

"""Usage: ./id_bins.py <bin_file> <genome_assembly.tab>
-Generate a list of the bacterial types
-Generate a dictionary of the taxonomies within a bin and record the number of times it occurs
-Generate a tsv of the number of hits and the bacteria name"""

import sys 

bins=open(sys.argv[1])
genome=open(sys.argv[2])
name = sys.argv[1]
tax_file=open(name[0:5] + '.txt', 'w')
tax_file.write('Occurances\tTaxonomy\n')

values=[]
tax_dict={}

for line in bins:
    line=line.strip()
    if line.startswith('>'):
        values.append(line)

for line in genome:
    line = line.strip().split('\t')
    name = '>' + line[0]
    tax = line[1]
    if name in values:
        if tax not in tax_dict:
            tax_dict[tax] = 1
        else:
            tax_dict[tax] += 1

for key in tax_dict:
    tax_file.write(str(tax_dict[key]) + '\t' + str(key) + '\n')