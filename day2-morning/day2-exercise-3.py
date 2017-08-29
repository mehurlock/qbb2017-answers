#!/usr/bin/env python

import sys

fh = open(sys.argv[1])
one_hit="NH:i:1"

count=0
for line in fh:
    if one_hit in line:
        count = count + 1
print count
    