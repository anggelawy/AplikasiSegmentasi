import pandas as pd
# Parent class untuk preprocessing data
class Preprocessing:
    def __init__(self):
        self.data_transformed = {}
        self.missing_records = {}
        self.rfm_results = None

    def handle_missing_data(self, data_files):
        for key, df in data_files.items():
            if isinstance(df, pd.DataFrame):
                self.missing_records[key] = df[df.isnull().any(axis=1)]
                self.data_transformed[key] = df.dropna()

    def perform_rfm_analysis(self, data_transformed):
        if 'Data Transaksi' in data_transformed:
            df = data_transformed['Data Transaksi']
            required_columns = {'Id Pelanggan', 'Tanggal invoice', 'Jumlah', 'Total Invoice'}
            if required_columns.issubset(df.columns):
                rfm = df.groupby('Id Pelanggan').agg({
                    'Tanggal invoice': 'max',
                    'Jumlah': 'count',
                    'Total Invoice': 'sum'
                }).reset_index()
                rfm.columns = ['Id Pelanggan', 'Recency', 'Frequency', 'Monetary']
                return rfm
        return None
