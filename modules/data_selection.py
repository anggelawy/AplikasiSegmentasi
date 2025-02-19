import os
import pandas as pd
from werkzeug.utils import secure_filename

# Parent class untuk pengelolaan file
class DataSelection:
    def __init__(self):
        self.data_files = {}

    def handle_upload(self, file_key, file):
        if file and file.filename:
            filepath = os.path.join('uploads', secure_filename(file.filename))
            file.save(filepath)
            self.data_files[file_key] = self.read_file(filepath)

    def read_file(self, filepath):
        try:
            if filepath.endswith('.csv'):
                return pd.read_csv(filepath)
            elif filepath.endswith('.xlsx'):
                return pd.read_excel(filepath)
        except Exception as e:
            return str(e)

