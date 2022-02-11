import pickle
from HyperParameterTuning.tuner import Tuner


class ModelSaver:

    def __init__(self):
        self.model = Tuner()
        self.mode = 'wb'
        self.path = "model.pkl"

    def save(self):

        try:
            adb_model = self.model.adb_tuner()
            path = self.path
            mode = self.mode
            pickle.dump(adb_model,open(path, mode))

        except Exception as e:
            raise e

m = ModelSaver()
m.save()



