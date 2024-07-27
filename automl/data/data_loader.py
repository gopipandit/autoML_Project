import pandas as pd

class DataLoader:
    def __init__(self,file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path)
        return data

    def preprocess_data(self,data):
        null_value = data.isnull().sum()

        return null_value