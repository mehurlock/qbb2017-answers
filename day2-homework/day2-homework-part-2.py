#!/usr/bin/env python


#The first file input should be the results of the mapping file in part 1. The second file input should be the desired ctab file.

import sys
count=0
f = open(sys.argv[1])
my_dictionary={}

for lines in f:
    fields = lines.rstrip("\r\n").split(" ")
    my_dictionary[fields[0]]=fields[1]

g=open(sys.argv[2])

print "Corresponding Matches From The Mapping File: "
for lines_1 in g:
    for keys in my_dictionary:
        if keys in lines_1 and count<100:
            count += 1
            print keys, my_dictionary[keys]
        else:
            continue