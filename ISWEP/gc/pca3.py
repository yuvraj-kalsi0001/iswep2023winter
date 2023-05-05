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

# Standardize the data by dividing each element by the largest value
max_value = data.values.max()
data = data / max_value

data = data.T
compounds = list(data.index)

# Create a list of compound numbers based on the order of the compounds in the transposed data
compound_numbers = list(range(1, len(compounds) + 1))

# Calculate PCA
pca = PCA(n_components=2)
pca.fit(data)
pca_data = pca.transform(data)

# Save PCA data to file, including compound numbers
pca_df = pd.DataFrame(data=pca_data, index=compounds, columns=['PC1', 'PC2'])
pca_df.index.name = 'Compound'
pca_df['CompoundNumber'] = compound_numbers
pca_df.to_csv('pca_output.csv')

# Perform clustering on PCA data
kmeans = KMeans(n_clusters=2)
kmeans.fit(pca_data)
labels = kmeans.predict(pca_data)

# Write clustering results to file with compound names, numbers, and coordinates
results_df = pd.DataFrame(data=pca_data, index=compounds, columns=['PC1', 'PC2'])
results_df['CompoundNumber'] = compound_numbers
results_df['Cluster'] = labels
results_df.to_csv('results.csv', index_label='Compound')

# Show graph for clustered data, with compound numbers displayed
fig, ax = plt.subplots()
scatter = ax.scatter(pca_data[:, 0], pca_data[:, 1], c=labels)
for i, txt in enumerate(compound_numbers):
    ax.annotate(txt, (pca_data[i, 0], pca_data[i, 1]))
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
