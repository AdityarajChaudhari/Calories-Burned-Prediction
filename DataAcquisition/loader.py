import pandas as pd


class DataLoader:

    def __init__(self):
        self.train_data = r'../Data/exercise.csv'
        self.test_data = r'../Data/calories.csv'

    def data_access(self):
        train_data = pd.read_csv(self.train_data.strip("u202a"))
        test_data = pd.read_csv(self.test_data.strip("u202a"))
        return train_data, test_data

