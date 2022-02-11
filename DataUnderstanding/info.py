import pandas as pd
from DataAcquisition.merge import DataMerge


class DataInfo:

    def __init__(self):
        self.data = DataMerge()

    def shape(self):
        data = self.data.merge()
        return data.shape

    def size(self):
        data = self.data.merge()
        return data.size

    def info(self):
        data = self.data.merge()
        return data.info()