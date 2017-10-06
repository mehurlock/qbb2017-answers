#!/usr/bin/env python

import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math

segment_file=open(sys.argv[1])
file_name=sys.argv[1]

p_value_sig=[]
p_value_insig=[]

lines=-1
for i in segment_file:
    fields=i.split()
    if fields[8] != "NA" and fields[8] != "P":
        lines += 1

for i in range(lines+5):
    p_value_sig.append(None)
    p_value_insig.append(None)
    
count = 0
segment_file.seek(0)
for i in segment_file:
    fields=i.split()
    c=fields[0]
    f=fields[8]
    if f == "P" or f == "NA" or f == "ADD":
        continue
    elif float(f) <= 10e-5:
        p_value_sig[count] = -np.log10(float(f))
        count += 1

    else:
        p_value_insig[count] = -np.log10(float(f))
        count += 1

plt.figure()
plt.scatter(range(len(p_value_sig)), p_value_sig, s=5, c="red")
plt.scatter(range(len(p_value_sig)), p_value_insig, s=5, c="blue")
plt.title(str(file_name[12:-13]))
plt.xlabel("Chromosome")
plt.ylabel(r'$-log_{10}$(P)')
plt.savefig(str(file_name[12:-13]) + "_manhattan_plot.png")
plt.close()















