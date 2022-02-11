import pandas as pd
from DataAcquisition.loader import DataLoader


class DataMerge:

    def __init__(self):
        self.data = DataLoader()

    def merge(self):
        train_data, test_data = self.data.data_access()
        data = pd.concat((train_data, test_data),axis=1)
        return data

