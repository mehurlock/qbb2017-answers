#!/usr/bin/env python

"""
Usage ./day5-lunch-promoter.py <tab_file> <ctab_file> > <output_file_name>
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import statsmodels.api as sm

tab = open(sys.argv[1])

avg={}
for line in tab:
    fields = line.rstrip("\r\n").split()
    avg[fields[0]]=float(fields[5])

ctab = open(sys.argv[2])
fpkms={}
for line in ctab:
    if line.startswith("t"):
        continue
    else:
        rows=line.rstrip("\r\n").split("\t")
        fpkms[rows[5]]=float(rows[11])
avgtrue=[]
fpkmstrue=[]

for i in avg:
    avgtrue.append(float(avg[i]))
    fpkmstrue.append(float(fpkms[i]))

model = sm.OLS(avgtrue,fpkmstrue)
results = model.fit()
print (results.summary())
    
