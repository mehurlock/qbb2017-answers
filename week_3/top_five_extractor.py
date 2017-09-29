#!/usr/bin/env python
"""
Usage:./top_five_extractor.py <snpEff.vcf>
"""

import sys
import matplotlib.pyplot as plt
import heapq

vcf=open(sys.argv[1])

quality={}
quality_nucleus={}
ann={}
ann_nucleus={}

for line in vcf:
    if line.startswith("#"):
        continue
    else:
        fields=line.split("\t")
        chrom=fields[0]
        pos=fields[1]
        quality[chrom + pos]=float(fields[5])
        ann[chrom + pos]=fields[7]
        if "chrM" not in chrom:
            quality_nucleus[chrom + pos]=float(fields[5])
            ann_nucleus[chrom + pos]=fields[7]
new=heapq.nlargest(5, quality, key=quality.get)
new_nucleus=heapq.nlargest(5, quality_nucleus, key=quality_nucleus.get)

for key in ann:
    if key in new:
        var=ann[key]
        fields=var.split(";")
        for item in fields:
            if "ANN" in item:
                everything=item.split(",")
                for location in everything:
                    if location.startswith("ANN="):
                        location = location[4:]
                        breakdown=location.split("|")
                        print key + ":", breakdown[1], breakdown[7]
                    else:
                        breakdown=location.split("|")
                        print key + ":", breakdown[1], breakdown[7]
                        
for key in ann_nucleus:
    if key in new_nucleus:
        var=ann_nucleus[key]
        fields=var.split(";")
        for item in fields:
            if "ANN" in item:
                everything=item.split(",")
                for location in everything:
                    if location.startswith("ANN="):
                        location = location[4:]
                        breakdown=location.split("|")
                        print key + ":", breakdown[1], breakdown[7]
                    else:
                        breakdown=location.split("|")
                        print key + ":", breakdown[1], breakdown[7]