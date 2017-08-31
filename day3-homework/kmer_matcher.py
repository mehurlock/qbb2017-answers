#!/usr/bin/env python

"""Program that takes two fasta fasta files, searches them for a kmer of desired length, then matches those kmers among the two sequences returnin the results"""
# $kmer_matcher.py <target.fa> <query.fa> <k>

import sys
import fasta

target=open(sys.argv[1])
query=open(sys.argv[2])
k=int(sys.argv[3])

kmerdict={}

for ident, sequence in fasta.FASTAReader(target):
    sequence=sequence.upper()
    for i in range(0, len(sequence)-k):
        # need to subtract k because the kmer will bug out when it reaches the end of the gene
        kmer=sequence[i:i+k]
        if kmer not in kmerdict:
            kmerdict[kmer]=[]
            kmerdict[kmer].append((ident,i))
        else:
            kmerdict[kmer].append((ident, i))

header= ["Target Name", "Target Start", "Query Start", "Kmer"]
print ('\t'.join(map(str, header)))
ident, sequence = fasta.FASTAReader(query).next()
sequence=sequence.upper()
for i in range(0, len(sequence)-k):
        # need to subtract k because the kmer will bug out when it reaches the end of the gene
    kmer=sequence[i:i+k]
    if kmer in kmerdict:
        for item in kmerdict[kmer]:
            final_list= [item[0],item[1], "",i, "",kmer]
            print ('\t'.join(map(str, final_list)))
#for kmer, count in querydict.iteritems():
    #print kmer, count     
    
#for kmer in kmerdict:
#    if kmer in 
    
    
    
    
    
    
    
    
    
    
    
     