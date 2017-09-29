#!/usr/bin/env python

"""
Usage: ./vcf_plot_maker.py <filtered vcf file. <plot name>

-Iterate a vcf file and extract the allele frequencies
-Plot the allele frequencies as a histogram for how often they happen
"""

import sys
import matplotlib.pyplot as plt

vcf=open(sys.argv[1])

blank={}
bins=[]

for line in vcf:
    if line.startswith("#"):
        continue
    else:
        fields=line.split(";")
        af=fields[3].split("=")
        number=af[1]
        if "," in number:
            value=number.split(",")
            for p in value:
                if p not in blank:
                    blank[p]=1
                    bins.append(float(p))
                else:
                    blank[p]+=1
                    bins.append(float(p))
        elif af[1] not in blank:
            blank[af[1]]=1
            bins.append(float(af[1]))
        else:
            blank[af[1]]+=1
            bins.append(float(af[1]))

plt.figure()
plt.hist(bins, bins=30, range=[0,1])
plt.title("Histogram")
plt.xlabel("Allele Frequency")
plt.ylabel("Number of Occurances")
plt.savefig(sys.argv[2] + ".png")
plt.close()