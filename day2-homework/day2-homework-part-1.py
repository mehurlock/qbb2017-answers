#!/usr/bin/env python

#File input should be the desired fly.txt file from http://www.uniprot.org/docs/fly.txt

import sys

f = open(sys.argv[1])

for line in f:
    if "DROME" in line:
        fields=line.rstrip("\r\n").split()
        if len(fields)==4:
            print fields[3], fields[2]