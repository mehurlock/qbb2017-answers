#!/usr/bin/env python

import sys

fh = open(sys.argv[1])
count=0
total=0

for line in fh:
    if line.startswith ( "@"):
        continue
    else:
        broken=line.split("\t")
        if broken[4] != "*":
            mapq=int(broken[4])
            total=total+mapq
            count=count+1
            avg=total/count
print avg
    