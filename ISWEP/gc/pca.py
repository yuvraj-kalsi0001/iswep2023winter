## In this file we are assuming we have clusters
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read CSV file and handle empty cells and unequal length columns, then transpose the data
data = pd.read_csv('combined.csv', header=0, index_col=0, na_values=['NA', 'nan', '', '?', '-'])
data.dropna(axis=0, how='any', inplace=True)
data = data.apply(lambda x: pd.to_numeric(x, errors='coerce'))
data.dropna(axis=1, how='any', inplace=True)
data = data.T
compounds = list(data.index)

# Calculate PCA
pca = PCA(n_components=2)
pca.fit(data)
pca_data = pca.transform(data)

# Save PCA data to file
pca_df = pd.DataFrame(data=pca_data, index=compounds, columns=['PC1', 'PC2'])
pca_df.to_csv('pca_output.csv')

# Perform clustering on PCA data
kmeans = KMeans(n_clusters=2)
kmeans.fit(pca_data)
labels = kmeans.predict(pca_data)

# Write clustering results to file with compound names
cluster_df = pd.DataFrame(data=labels, index=compounds, columns=['Cluster'])
cluster_df.index.name = 'Compound'
cluster_df.to_csv('clustering_output.csv')

# Show graph for clustered data
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=labels)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
