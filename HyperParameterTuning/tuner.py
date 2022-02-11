import numpy as np
from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import RandomizedSearchCV
from ModelBuilding.model import Model
from DataSep.sep import Seperator


class Tuner:

    def __init__(self):
        self.data = Seperator()
        self.model = Model()

    def adb_tuner(self):
        x_train, x_test, y_train, y_test = self.data.dep_sep()
        adbr = self.model.Adb_model()
        params = {
            'n_estimators': [i for i in range(1,1000,50)],
            'learning_rate': [float(i) for i in np.linspace(0.1,1,10)],
            'loss': ['linear', 'exponential', 'square']
        }
        adb_model = RandomizedSearchCV(estimator=adbr, param_distributions=params, cv=10, n_iter=50, n_jobs=6, verbose=True, random_state=75)
        adb_model.fit(x_train, y_train)
        adb_model_best = adb_model.best_params_
        finalreg = AdaBoostRegressor(n_estimators=adb_model_best['n_estimators'], learning_rate=adb_model_best['learning_rate'], loss=adb_model_best['loss'])
        finalreg.fit(x_train,y_train)
        return finalreg



