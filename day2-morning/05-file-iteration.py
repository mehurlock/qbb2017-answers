#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

count=0
for line in fh:
    #Start and end are in columns 3 and 4
    if line.startswith ( "@"):
        continue
    else:
        count = count + 1
print count
    #fields = line.split("\t")
    #print int(fields[4]) - int(fields[3])
    