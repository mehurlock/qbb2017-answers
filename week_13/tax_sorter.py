#!/usr/bin/env python

"""Usage: ./tax_sorter.py <id_bins_output.tsv>

-Import the data from the id_bins.py script as a data frame
-Sort the data frame by the strain with the highest number of hits (descending)
-Output the new list ordered with the highest hit on top"""

import pandas as pd
import sys

bins = open(sys.argv[1])
name = sys.argv[1]

df = pd.read_csv(bins, sep='\t')
sdf=df.sort_values('Occurances', ascending=False)
sdf=sdf.reset_index(drop=True)
target = sdf['Taxonomy'][0].split(';')
print name[0:5] +'\t'+ str(sdf['Occurances'][0]) + '\t' + target[-1] + '\n'