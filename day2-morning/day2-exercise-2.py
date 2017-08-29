#!/usr/bin/env python

import sys

fh = open(sys.argv[1])
perfect="MD:Z:40"

count=0
for line in fh:
    if perfect in line:
        count = count + 1
print count
    