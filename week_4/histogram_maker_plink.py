#!/usr/bin/env python

"""
Usage: ./histogram_maker_plink.py <filtered vcf file> <plot name>

-
"""

import sys
import matplotlib.pyplot as plt

frq=open(sys.argv[1])

bins=[]

for line in frq:
    fields=line.split()
    number=fields[4]
    if number.isalpha():
        continue
    else:
        bins.append(float(number))


plt.figure()
plt.hist(bins, bins=500, range=[0,0.5])
plt.title("Histogram")
plt.xlabel("Allele Frequency")
plt.ylabel("Number of Occurances")
plt.savefig(sys.argv[2] + ".png")
plt.close()