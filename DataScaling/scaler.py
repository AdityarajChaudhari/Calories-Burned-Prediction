import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from DataSplit.split import DataSplit


class Scaler:

    def __init__(self):
        self.data = DataSplit()

    def data_scaling(self):
        x, y = self.data.split()
        sclr = StandardScaler()
        x = pd.DataFrame(sclr.fit_transform(x),columns=x.columns)
        return x, y, sclr

    def savescaler(self):
        x, y, sclr = self.data_scaling()
        pickle.dump(sclr, open('scaler.pkl', 'wb'))








