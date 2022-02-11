from DataPreProcessing.Preprocessor import Preprocessing


class DataSplit:

    def __init__(self):
        self.data = Preprocessing()

    def split(self):
        data = self.data.drop_corr_features()
        x = data.drop('Calories', axis=1)
        y = data['Calories']
        return x, y

