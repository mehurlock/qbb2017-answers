#!/usr/bin/env python

"""
Usage ./day5-lunch.py <ctab> <output_name.bed>

-Plot timecourse of FBtr0331261 for females
"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep="\t")

coi = ["chr", "promoter_start", "promoter_end", "t_name"]

coi_pos = df["strand"]=="+"
coi_neg = df["strand"]=="-"

"""df.loc[coi_pos, "promoter_start"] = round(df[coi_pos]["start"] - 499, 1)
df.loc[coi_pos, "promoter_end"] = df[coi_pos]["start"]+501
df.loc[coi_neg, "promoter_start"] = df[coi_neg]["end"]-501
df.loc[coi_neg, "promoter_end"] = df[coi_neg]["end"]+499
"""
for strand in df["strand"][coi_pos]:
    df["promoter_start"] = df["start"]-499
    df["promoter_end"] = df["start"]+501
    
for stand in df["strand"][coi_neg]:
    df["promoter_start"] = df["end"]-501
    df["promoter_end"] = df["end"]+499
    
num=df._get_numeric_data()
num[num<0]=0

df[coi].to_csv(sys.argv[2], sep = "\t", index=False, header=False)