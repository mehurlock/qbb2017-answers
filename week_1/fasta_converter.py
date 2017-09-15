#!/usr/bin/env python

"""
Usage: ./fasta_converter <dna_alignment.fa> <protein_alignment.fa>

-Take a DNA alignment and insert blank codons based on an input protein alignement file
"""

import itertools
import sys
import fasta

dnaFile=open(sys.argv[1])
aminoFile=open(sys.argv[2])
alignFile=open("alignment_nuc.out", "w")
aFile=open("prot.out", "w")

for (dnaIdent, dnaSeq), (aminoIdent, aminoSeq) in itertools.izip(fasta.FASTAReader(dnaFile), fasta.FASTAReader(aminoFile)):
    for amino in aminoSeq:
        if amino == "-":
            alignFile.write("---")
            aFile.write(amino)
        else:
            alignFile.write(dnaSeq[:3])
            dnaSeq=dnaSeq[3:]
            aFile.write(amino)
    alignFile.write("\n")
    aFile.write("\n")
