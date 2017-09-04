#!/usr/bin/env python

"""
Usage ./day5-lunch.py <ctab> > <output_name.bed>
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
            print rows[1] + "\t %d \t %d" % (new_final, new_start) + "\t" + rows[5]x