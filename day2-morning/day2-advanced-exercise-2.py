#!/usr/bin/env python

import sys

fh = open(sys.argv[1])
count=0

for line in fh:
    if line.startswith ( "@"):
        continue
    else:
        broken=line.split("\t")
        if broken[2]=="2L":
            if int(broken[3])>=10000 and int(broken[3])<20001:
                count=count+1
print count
    