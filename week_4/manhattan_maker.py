#!/usr/bin/env python

import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math

gwas_output_list=["gwas_output.Cadmium_Chloride.assoc.linear",
"gwas_output.Caffeine.assoc.linear",
"gwas_output.Calcium_Chloride.assoc.linear",
"gwas_output.Cisplatin.assoc.linear",
"gwas_output.Cobalt_Chloride.assoc.linear",
"gwas_output.Congo_red.assoc.linear",
"gwas_output.Copper.assoc.linear",
"gwas_output.Cycloheximide.assoc.linear",
"gwas_output.Diamide.assoc.linear",
"gwas_output.E6_Berbamine.assoc.linear",
"gwas_output.Ethanol.assoc.linear",
"gwas_output.Formamide.assoc.linear",
"gwas_output.Galactose.assoc.linear",
"gwas_output.Hydrogen_Peroxide.assoc.linear",
"gwas_output.Hydroquinone.assoc.linear",
"gwas_output.Hydroxyurea.assoc.linear",
"gwas_output.Indoleacetic_Acid.assoc.linear",
"gwas_output.Lactate.assoc.linear",
"gwas_output.Lactose.assoc.linear",
"gwas_output.Lithium_Chloride.assoc.linear",
"gwas_output.Magnesium_Chloride.assoc.linear",
"gwas_output.Magnesium_Sulfate.assoc.linear",
"gwas_output.Maltose.assoc.linear",
"gwas_output.Mannose.assoc.linear",
"gwas_output.Menadione.assoc.linear",
"gwas_output.Neomycin.assoc.linear",
"gwas_output.Paraquat.assoc.linear",
"gwas_output.Raffinose.assoc.linear",
"gwas_output.SDS.assoc.linear",
"gwas_output.Sorbitol.assoc.linear",
"gwas_output.Trehalose.assoc.linear",
"gwas_output.Tunicamycin.assoc.linear",
"gwas_output.Xylose.assoc.linear",
"gwas_output.YNB.assoc.linear",
"gwas_output.YNB:ph3.assoc.linear",
"gwas_output.YNB:ph8.assoc.linear",
"gwas_output.YPD.assoc.linear",
"gwas_output.YPD:15C.assoc.linear",
"gwas_output.YPD:37C.assoc.linear",
"gwas_output.YPD:4C.assoc.linear",
"gwas_output.Zeocin.assoc.linear",
"gwas_output.log",
"gwas_output.nosex",
"gwas_output.x4-Hydroxybenzaldehyde.assoc.linear",
"gwas_output.x4NQO.assoc.linear",
"gwas_output.x5-Fluorocytosine.assoc.linear",
"gwas_output.x5-Fluorouracil.assoc.linear",
"gwas_output.x6-Azauracil.assoc.linear"]

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















