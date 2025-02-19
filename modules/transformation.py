# Parent class untuk transformasi data
class Transformation:
    def __init__(self):
        self.transformed_data = None

    def normalize_rfm(self, rfm_results):
        if rfm_results is not None:
            rfm = rfm_results.copy()
            for col in ['Recency', 'Frequency', 'Monetary']:
                rfm[f'{col}_normalized'] = ((rfm[col] - rfm[col].min()) / (rfm[col].max() - rfm[col].min())).round(3)
            self.transformed_data = rfm
        return self.transformed_data

