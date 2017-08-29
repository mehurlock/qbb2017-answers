#!/usr/bin/env python

import sys

fh = open(sys.argv[1])
biton=0
bitoff=0

for line in fh:
    if line.startswith ( "@"):
        continue
    else:
        broken=line.split("\t")
        binary=int(broken[1])
        result=binary&16
        if result>0:
            biton=biton+1
        else:
            bitoff=bitoff+1
print "Aligned forward: ", bitoff
print "Aligned reverse: ", biton
    