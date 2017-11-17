#!/usr/bin/env python

"""
Usage: ./heatmap_generator.py <gene_expression_file.txt>

-Generate heat maps of gene expression
-Generate a dendrogram of cell differentiation
-Perform statisitcal analysis on gene expression patterns across cell types
-Generate a table of kmeans groupings that can be used to find genes of interest in the sorted dataframe
-Find genes that follow similar expression patterns to a gene of interest
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster as sp
import scipy.stats as ss
from sklearn.cluster import KMeans

#Import data as a pandas dataframe with the headers removed.
df = pd.read_csv(sys.argv[1], delimiter='\t')
data = df.as_matrix()[:,1:].astype(float)

#Calculate the linkage matrix. Second linkage matrix is optimized for dendrogram creation.
linked_data = sp.hierarchy.linkage(data,method='average',metric='euclidean')
linked_dataT = sp.hierarchy.linkage(data.T,method='average',metric='euclidean')
dend_labels = ['CFU','poly','unk','int','mys','mid']

#Generate heat map dataframe. Denote axis ticks for labeling.
heatmap_order_idx = sp.hierarchy.leaves_list(linked_data)
ordered_data = data[heatmap_order_idx, :]
xaxis=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5]

#Calculate kmeans.
kmeans = KMeans(n_clusters=7, random_state = 0)
kmeans.fit(data)
labels = kmeans.predict(data)
merged = pd.merge(df, pd.DataFrame(labels, columns=['clusters']), left_index=True, right_index=True)
merged = merged.sort_values('clusters')[[ 'CFU', 'poly', 'unk', 'int', 'mys', 'mid']]

#Extract significant differentially expressed genes.
sig_list=[]
genes=open("significant_genes.txt", 'w')
genes.write("Index Number \t Gene Name \t Expression Ratio \t P-value \n")
df = pd.read_csv(sys.argv[1], sep='\t')
for index, row in df.iterrows():
    early=np.array([row['CFU'], row['int'], row['mys']])
    emean=early.mean()
    late=np.array([row['poly'], row['unk'], row['mid']])
    lmean=late.mean()
    ratio=emean/lmean
    df.loc[index, 'mean_ratio']=ratio
    stat, p = ss.ttest_ind(early, late)
    df.loc[index, 'p_value']=p
    if p < 0.05:
        if ratio < 0.5 or ratio > 2.0:
            sig_list.append((index, row['gene'], ratio, p))
            genes.write(str(index) + '\t' + str(row['gene']) + '\t' + str(ratio) + '\t' + str(p) + '\n')

#Generate a list of genes related to the highest hit from significance analysis. Method requires knowing the grouping number containing the gene of interest from the kmeans analysis. Genes can be copied to Panther for analysis. Generates a csv file that can be used to search for the grouping of the significant gene of interest.
related_genes=[]
dfs = pd.read_csv(sys.argv[1], sep='\t')
kmeans_groups=open('kmeans_groupings.csv', 'w')
for value in range(len(labels)):
    dfs.loc[value, 'cluster'] = int(labels[value])
dfx = dfs.sort_values('cluster')
for index, row in dfx.iterrows():
    kmeans_groups.write(str(row[0]) + '\t' + str(row[7]) + '\n')
    if row[7] == 0:
        related_genes.append(row[0])
        print row[0]

#Plot heat map based on initial heat map analysis
plt.figure()
plt.title('Heatmap')
plt.pcolor(ordered_data, cmap='seismic')
ax = plt.gca()
ax.set_facecolor('black')
plt.colorbar()
plt.xticks(xaxis,dend_labels)
plt.xlabel('Cell Stage')
plt.yticks([])
plt.ylabel('Genes')
plt.savefig('hema_cell_heatmap.png')
plt.close()

#Plot kmeans heatmap
plt.figure()
plt.title('Kmeans Heatmap')
plt.pcolor(merged, cmap='seismic')
ax = plt.gca()
ax.set_facecolor('black')
plt.colorbar()
plt.xticks(xaxis, dend_labels)
plt.xlabel('Cell Stage')
plt.yticks([])
plt.ylabel('Genes')
plt.savefig('kmeans_hema_cell_heatmap.png')
plt.close()

#Plot dendrogram
plt.figure()
sp.hierarchy.dendrogram(linked_dataT, labels = dend_labels)
plt.yticks([])
plt.ylabel('Differentiation Distance')
plt.title('Hematopoietic Cell Differentiation')
plt.savefig('hema_cell_dendrogram.png')
plt.close()