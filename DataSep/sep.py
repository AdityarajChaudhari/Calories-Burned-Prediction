from sklearn.model_selection import train_test_split
from DataScaling.scaler import Scaler


class Seperator:

    def __init__(self):
        self.data = Scaler()

    def dep_sep(self):
        x, y = self.data.data_scaling()
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33,random_state=75)
        return x_train, x_test, y_train, y_test


