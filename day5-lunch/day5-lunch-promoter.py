#!/usr/bin/env python

"""
Usage ./day5-lunch-promoter.py <tab_file> <ctab_file> > <output_file_name>

-Plot timecourse of FBtr0331261 for females
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
    
"""    avg.append(float(fields[4]))
    
fpkms=[]
df = pd.read_csv(sys.argv[2], sep = "\t")
fpkms = df["FPKM"].values.tolist()

model = sm.OLS(avg,fpkms)
results = model.fit()
print (results.summary())"""

"""fpkms=[]
df = pd.read_csv(sys.argv[1], sep = "\t")
fpkms = df["FPKM"].values.tolist()

print fpkms

histone_mean=[]
fh=open(sys.argv[2])

for line in fh:
    fields = line.rstrip("\r\n").split()
    histone_mean.append(fields[4])
    
print len(histone_mean)
print len(fpkms)

model = sm.OLS(histone_mean, exog = fpkms)
results = model.predict()
print results"""

