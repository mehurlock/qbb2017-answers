#!/usr/bin/env python

import sys

fh = open(sys.argv[1])

count=0
for line in fh:
    
    if line.startswith ( "@"):
        continue
    else:
        count = count + 1
print count
    