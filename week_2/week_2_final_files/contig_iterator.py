#!/usr/bin/env python

"""
Usage: ./contig_iterator.py <fastafile>
"""

import fasta
import sys
import numpy as np


contig=open(sys.argv[1])

contig_list=[]
dummy_list=[]

#Iterate the fasta input and append the list with the values of the lengths of the contig lines
for dIdent, dSeq in fasta.FASTAReader(contig):
    contig_list.append(len(dSeq))
    dummy_list.append(len(dSeq))

contig_list.sort()
dummy_list.sort()

#Find the N50 using the dummy_list as     
total=sum(dummy_list)
count=0
while count<(total/2):
    count += dummy_list[-1]
    dummy_list.remove(dummy_list[-1])

#Print interesting values for the sequence alignment
print "Max:", np.max(contig_list)
print "Min:", np.min(contig_list)
print "Mean:", str(round(np.mean(contig_list), 2))
print "Number:", len(contig_list)
print "N50:", contig_list[len(dummy_list)]