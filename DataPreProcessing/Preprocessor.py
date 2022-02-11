import numpy as np
from DataAcquisition.merge import DataMerge


class Preprocessing:

    def __init__(self):
        self.data = DataMerge()

    def drop_col(self):
        data = self.data.merge()
        data.drop('User_ID',axis=1,inplace=True)
        return data

    def feature_transform(self):
        data = self.drop_col()
        data['Gender'] = np.where(data['Gender']=='male', 1, 0)
        return data

    def drop_corr_features(self):
        data = self.feature_transform()
        data.drop(['Height','Body_Temp'],axis=1,inplace=True)
        return data


