#loading data
import pandas as pd
import numpy as np

whisky = pd.read_csv('whiskies.txt')
# print(whisky.head())
whisky['region'] = pd.read_csv('regions.txt') #Add region column

print(whisky.head())
whisky.iloc[0:10] #rows
whisky.iloc[5:10, 0:5]
whisky.columns
flavor = whisky.iloc[:, 2:14] # flavors subset
# print(flavor)

#----------------------------------------- exploring correlations
# Pearson correlation by default
corr_flavors = pd.DataFrame.corr(flavor)
# same as
cor = flavor.corr()
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.pcolor(cor) # instead of Seaborn heatmap function
plt.colorbar()
# plt.savefig('corr_flavor.pdf')

# correlation among whiskies across flavors --> transpose
corr_whisky = flavor.transpose().corr()
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()
plt.axis('tight')
# plt.savefig('corr_whisky.pdf')

#----------------------------------------- clustering whisky by flavor profile
# spectral co-clustering from scikit-learn
# --> both variables are clustered simultaneously
# using eigenvalues and eigenvectors
# reordering will create groups/clusters

from sklearn.cluster.bicluster import SpectralCoclustering
model=SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
# entries are True of False, each row identifies a cluster, from 0 to 5
# each column identifies a row in the matrix

import numpy as np
np.sum(model.rows_, axis=1)

np.sum(model.rows_, axis=0) # should be 1 group per column
model.row_labels_