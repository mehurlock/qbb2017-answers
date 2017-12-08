#!/usr/bin/env python

"""Usage: ./heat_map.py <taxonomy.tab> <bin_identities.tsv>

-Matches taxonomy identities to their bin numbers
-Build a dataframe that contains the data used in KRAKEN
-Generate a heat map of bacterial populations across the samples"""


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
from scipy.spatial.distance import pdist
from sklearn.cluster import KMeans

taxonomy=open(sys.argv[2])
tax_dict={}
labels=[]
for line in taxonomy:
    line=line.strip().split('\t')
    tax_dict[line[0]]=line[2]
    labels.append(line[2])

true_df = pd.read_csv(sys.argv[1], delimiter='\t')[['Genomic bins', 'SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']]
for i in range(len(true_df)):
    value = true_df['Genomic bins'][i]
    if value in tax_dict:
        true_df['Genomic bins'][i]=tax_dict[value]
        
true_df = true_df.set_index('Genomic bins')

df = pd.read_csv(sys.argv[1], delimiter='\t', )[['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']]

def clustering(dof, labels):
    flipped=np.transpose(dof.values)
    lx, ly=linkage(dof.values, method='average'), linkage(flipped, method='average')
    leafx, leafy = leaves_list(lx), leaves_list(ly)
    transformed=dof.values[leafx,:]
    label=np.array(labels)[leafx]
    return transformed, label, ly

def heatmap(intensities, y, x):
    plt.figure()
    plt.imshow(intensities, aspect='auto', interpolation='nearest')
    plt.grid(False)
    plt.colorbar(label='abundance')
    plt.title("Infant Genome Abundance")
    plt.yticks(range(len(y)), y)
    plt.xticks(range(len(x)), x, rotation='vertical')
    plt.tight_layout()
    plt.savefig('output')
    plt.close()
    
trans, trans_labels, linky = clustering(true_df, labels)
data=pd.DataFrame(trans, columns=df.columns, index=trans_labels)[['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']]
stage_labels=data.columns
heatmap(data, trans_labels, stage_labels)
    
    
    
    
    