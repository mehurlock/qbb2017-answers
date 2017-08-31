#!/usr/bin/env python

"""
Usage ./day4-homework-basic.py <samples.csv> <ctab_dir>

-Plot timecourse of FBtr0331261 for females
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples=pd.read_csv(sys.argv[1]) #no tab needed because file has commas instead
soi=df_samples["sex"]=="female"
moi=df_samples["sex"]=="male"

fpkms_female = []
fpkms_male=[]

for sample in df_samples["sample"][soi]:
    #Build complete file path
    fname=os.path.join(sys.argv[2], sample, "t_data.ctab")
    #Read current sample
    df=pd.read_csv(fname, sep="\t" )
    #Subset just Sxl rows
    roi=df["t_name"]== transcript
    #Save FPKM values to DataFrame
    fpkms_female.append(df[roi]["FPKM"].values)
    
for sample in df_samples["sample"][moi]:
    #Build complete file path
    fname=os.path.join(sys.argv[2], sample, "t_data.ctab")
    #Read current sample
    df=pd.read_csv(fname, sep="\t" )
    #Subset just Sxl rows
    roi=df["t_name"]== transcript
    #Save FPKM values to DataFrame
    fpkms_male.append(df[roi]["FPKM"].values)
    
df_replicates=pd.read_csv(sys.argv[3])
repoi_f=df_replicates["sex"]=="female"
repoi_m=df_replicates["sex"]=="male"

rep_fpkms_f=[None,None,None,None]
rep_fpkms_m=[None,None,None,None]

for replicate in df_replicates["sample"][repoi_f]:
    rfname=os.path.join(sys.argv[2], replicate, "t_data.ctab")
    df = pd.read_csv(rfname, sep = "\t")
    roi=df["t_name"]==transcript
    rep_fpkms_f.append(df[roi]["FPKM"])
    
for replicate in df_replicates["sample"][repoi_m]:
    rmname=os.path.join(sys.argv[2], replicate, "t_data.ctab")
    df = pd.read_csv(rmname, sep = "\t")
    roi=df["t_name"]==transcript
    rep_fpkms_m.append(df[roi]["FPKM"])
    
plt.figure()
plt.plot(fpkms_female, c="red", dash_joinstyle='miter')
plt.plot(fpkms_male, c="blue", dash_joinstyle='miter')
plt.plot(rep_fpkms_f, 'o', c="orange", dash_joinstyle='miter')
plt.plot(rep_fpkms_m, 'o', c="purple", dash_joinstyle='miter')
plt.xticks(range(len(fpkms_female)), df_samples["stage"], rotation=90)
plt.ylabel("Relative expression (FPKM)")
plt.xlabel("Developmental stage")
plt.title("Sxl")
plt.ylim(0,200)
art=[]
plt.legend(["females", "males", "female replicates", "male replicates"], loc="center right", bbox_to_anchor=(1.5, 0.5), frameon=False, numpoints=1)
plt.savefig("Sxl_Plot.png", additional_artists=art, bbox_inches="tight")
plt.close()