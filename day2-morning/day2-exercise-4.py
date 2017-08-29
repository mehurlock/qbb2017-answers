#!/usr/bin/env python

import sys

fh = open(sys.argv[1])
count=0

for line in fh:
    if line.startswith ( "@"):
        continue
    elif count<10:
        broken=line.split("\t")
        if broken[2] != "*":
            print broken[2]
            count = count +1
    