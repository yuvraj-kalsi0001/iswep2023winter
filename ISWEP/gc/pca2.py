## IN this code the program calculates automatically the number of clusters

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Read CSV file and handle empty cells and unequal length columns, then transpose the data
data = pd.read_csv('combined.csv', header=0, index_col=0, na_values=['NA', 'nan', '', '?', '-'])
data.dropna(axis=0, how='any', inplace=True)
data = data.apply(lambda x: pd.to_numeric(x, errors='coerce'))
data.dropna(axis=1, how='any', inplace=True)
data = data.T

data.insert(0, 'Compound Number', range(1, 1 + len(data)))##Add a new column to the data frame to number the compounds:

data /= data.max().max()
compounds = list(data.index)

# Calculate PCA
pca = PCA(n_components=2)
pca.fit(data)
pca_data = pca.transform(data)

# Create a new data frame to store the compound information:
compounds_df = pd.DataFrame({
    'Compound Name': data.index,
    'Compound Number': data['Compound Number'],
    'PCA1': pca_data[:, 0],
    'PCA2': pca_data[:, 1],
})

#Write the compound information to a CSV file:

compounds_df.to_csv('compound_info.csv', index=False)


# Determine optimal number of clusters using the elbow method
wcss = []
for i in range(1, len(pca_data)):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(pca_data)
    wcss.append(kmeans.inertia_)
    
# Find the "elbow" in the plot to determine the optimal number of clusters
differences = np.diff(wcss)
max_difference_index = differences.argmax()
num_clusters = max_difference_index + 2 # Add 2 because we started with index 1 instead of 0

# Perform KMeans clustering on PCA data
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
labels = kmeans.fit_predict(pca_data)

# Write clustering results to file with compound names
cluster_df = pd.DataFrame(data=labels, index=compounds, columns=['Cluster'])
cluster_df.index.name = 'Compound'
cluster_df.to_csv('clustering_output.csv')

# Show graph for clustered data
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=labels)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()