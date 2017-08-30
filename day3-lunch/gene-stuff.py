#!/usr/bin/env python

import sys

totalspan = 0
genecnt = 0

for line in sys.stdin:
    line =line.rstrip()
    mylen = int(line)
    totalspan += mylen
    genecnt += 1
    print "There are %d genes, with a total span of %d, average gene length is %f" % (genecnt, totalspan, totalspan/genecnt)