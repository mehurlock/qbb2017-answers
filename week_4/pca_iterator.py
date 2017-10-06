#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy

pca=open(sys.argv[1])

pc1=[]
pc2=[]

for line in pca:
    line=line.split(" ")
    pc1.append(line[2])
    pc2.append(line[3])
    
plt.figure()
plt.scatter(pc1, pc2)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Plot")
plt.tight_layout()
plt.savefig(sys.argv[2] + ".png")
plt.close()