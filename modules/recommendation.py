import pandas as pd
# Parent class untuk rekomendasi pelanggan
class Recommendation:
    def __init__(self):
        self.recommendations = None
        self.merged_data = None

    def generate_recommendations(self, clustering_results, questionnaire_data):
        # **Nama khusus hanya untuk cluster 1-3**
        cluster_names = {
            1: 'Pelanggan Loyal',
            2: 'Pelanggan Baru',
            3: 'Pelanggan Sesekali'
        }

        # **Semua cluster yang bukan 1, 2, atau 3 disebut "Tidak Ada"**
        cluster_labels = {c: cluster_names.get(c, 'Tidak Ada') for c in clustering_results['Cluster'].unique()}

        # **Buat summary jumlah pelanggan per cluster**
        cluster_summary = clustering_results['Cluster'].value_counts().reset_index()
        cluster_summary.columns = ['Cluster', 'Jumlah Pelanggan']
        cluster_summary['Segment'] = cluster_summary['Cluster'].map(cluster_labels)
        self.recommendations = cluster_summary

        # **Gabungkan dengan data kuisioner jika ada**
        if isinstance(questionnaire_data, pd.DataFrame):
            self.merged_data = pd.merge(
                questionnaire_data.dropna(),
                clustering_results[['Id Pelanggan', 'Cluster']],
                on='Id Pelanggan',
                how='left'
            )
            self.merged_data['Segment'] = self.merged_data['Cluster'].map(cluster_labels)

        return self.recommendations, self.merged_data
    