#!/usr/bin/env python

import sys
import numpy as py
import matplotlib.pyplot as plt

input_file=open(sys.argv[1])

plt.figure()
count=1
for line in input_file:
    fields=line.split("\t")
    if any(c.isalpha() for c in fields[0]) == False:
        start, end = int(fields[0]), int(fields[1])
        plt.plot([start, end], [count, count + abs(end-start)])
        count += abs(end-start)   

plt.xlim(0, 100000)
plt.ylim(0, 100000)
plt.savefig("dotplot_" + sys.argv[2] +".png")
plt.close()       