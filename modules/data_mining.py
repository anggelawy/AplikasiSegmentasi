from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# Parent class untuk clustering
class DataMining:
    def __init__(self):
        self.clustering_results = None
        self.dbi_score = None

    def apply_clustering(self, transformed_data, num_clusters, export_path=None):
        clustering_data = transformed_data[['Recency_normalized', 'Frequency_normalized', 'Monetary_normalized']].dropna()

        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(clustering_data)

        transformed_data['Cluster'] = kmeans.labels_ + 1
        transformed_data['Cluster'] = transformed_data['Cluster'].astype(int)
        self.clustering_results = transformed_data

        # Hitung SSW (Sum of Squared Within-cluster distances)
        ssw = sum(np.sum((clustering_data[kmeans.labels_ == i] - center) ** 2) 
                  for i, center in enumerate(kmeans.cluster_centers_))

        # Hitung SSB (Sum of Squared Between-cluster distances)
        global_center = clustering_data.mean(axis=0)
        ssb = sum(len(clustering_data[kmeans.labels_ == i]) * np.sum((center - global_center) ** 2)
                  for i, center in enumerate(kmeans.cluster_centers_))

        # DBI dari rasio SSW/SSB
        modified_dbi = np.sum(ssw) / np.sum(ssb) if np.sum(ssb) != 0 else float('inf')

        self.dbi_score = round(modified_dbi, 3)

        # # Jika diberikan path, simpan hasil ke Excel
        # if export_path:
        #     transformed_data.to_excel(export_path, index=False)
        #     print(f"File berhasil disimpan: {export_path}")

        return self.clustering_results, self.dbi_score
