#!/usr/bin/env python

"""
Usage ./day5-lunch.py <ctab> <output_name.bed>

-Plot timecourse of FBtr0331261 for females
"""

import sys

f = open(sys.argv[1])
running=[]

for line in f:
    if line.startswith("t"):
        continue
    else:
        rows = line.rstrip("\r\n").split("\t")
        strand=rows[2]
        start=rows[3]
        final=rows[4]
        if strand == "+":
            new_start = int(start) -  500
            new_final = int(start) + 500
            if new_start <0:
                new_start=0
            print rows[1] + "\t %d \t %d" % (new_start, new_final) + "\t" + rows[5]
        else:
            new_start = int(final) +500
            new_final = int(final) -500
            if new_final <0:
                new_final = 0
            print rows[1] + "\t %d \t %d" % (new_final, new_start) + "\t" + rows[5]
        
    """else:
        start -=501
        end += 499
    for i in range(0, len(rows)-1):
        final_rows=[strand, start, end]
    return final_rows

print final_rows"""


"""coi = ["chr", "promoter_start", "promoter_end", "t_name"]

coi_pos = df["strand"]=="+"
coi_neg = df["strand"]=="-"

df.loc[coi_pos, "promoter_start"] = round(df[coi_pos]["start"] - 499, 1)
df.loc[coi_pos, "promoter_end"] = df[coi_pos]["start"]+501
df.loc[coi_neg, "promoter_start"] = df[coi_neg]["end"]-501
df.loc[coi_neg, "promoter_end"] = df[coi_neg]["end"]+499

for strand in df["strand"][coi_pos]:
    df["promoter_start"] = df["start"]-499
    df["promoter_end"] = df["start"]+501
    
for stand in df["strand"][coi_neg]:
    df["promoter_start"] = df["end"]-501
    df["promoter_end"] = df["end"]+499
    
num=df._get_numeric_data()
num[num<0]=0

print df[coi].sort_values(columns="t_name")
#df[coi].to_csv(sys.argv[2], sep = "\t", index=False, header=False)"""