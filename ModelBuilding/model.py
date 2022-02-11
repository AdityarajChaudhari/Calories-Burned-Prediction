from sklearn.ensemble import AdaBoostRegressor
from sklearn import metrics
from DataSep.sep import Seperator


class Model:

    def __init__(self):
        self.data = Seperator()

    def Adb_model(self):
        x_train, x_test, y_train, y_test = self.data.dep_sep()
        adbr = AdaBoostRegressor()
        adbr.fit(x_train, y_train)
        print("Training Score :- ", adbr.score(x_train, y_train))
        print("Testing Score :- ", adbr.score(x_test, y_test))
        y_pred = adbr.predict(x_test)
        print("MAE :- ", metrics.mean_absolute_error(y_test, y_pred))
        print("MSE :- ", metrics.mean_squared_error(y_test, y_pred))
        return adbr




