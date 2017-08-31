#!/usr/bin/env python

"""
Usage: ./basic-lunch-exercise.py <ctab-1> <ctab-2> <prefix>

-Extract the FPKM values from the respective ctab files
-Generate a x vs y plot of the values
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

df_1=pd.read_csv(sys.argv[1], sep="\t")
df_2=pd.read_csv(sys.argv[2], sep="\t")

coi=["t_name", "FPKM"]
t_name_list_1=[]
t_name_list_2=[]
fpkm_list_1=[]
fpkm_list_2=[]
combined={}

for item in df_1["t_name"]:
    t_name_list_1.append(item)
for item in df_2["t_name"]:
   t_name_list_2.append(item) 
    
    
    
for item in df_1["FPKM"]:
    fpkm_list_1.append(math.log10(float(item)+1))
    
for item in df_2["FPKM"]:
    fpkm_list_2.append(math.log10(float(item)+1))
  
x = np.array(fpkm_list_1)
y = np.array(fpkm_list_2)    
    
    
    
#for i in range(0, len(fpkm_list_1)-1):
    #if int(fpkm_list_1[i]) != 0 and int(fpkm_list_2[i]) != 0:
        #combined[math.log10(int(fpkm_list_1[i]))]=math.log10(int(fpkm_list_2[i]))
    
plt.figure()
plt.scatter(fpkm_list_1, fpkm_list_2, alpha=0.2)
plt.xlim(0)
plt.ylim(0)
plt.xlabel("FPKM for SRR072893")
plt.ylabel("FPKM for SRR072915")
plt.title("Comparison of Two Reads")
plt.savefig(sys.argv[3] + ".png")
plt.close()
plt.plot(np.unique(x), np.poly1d(np.polyfit(x,y,1))(np.unique(x)))

