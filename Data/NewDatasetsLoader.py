import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import NewDatasets.processedDataset as prosedDataset


class Dataset:
    def __init__(self, dataset_name):
        self.DatasetName = dataset_name
        self.processedDatasetList = prosedDataset.ProcessedDataset().GetDatasetList()

    def GetDataset(self):
        if self.DatasetName not in self.processedDatasetList:
            print('Err.')
        else:
            if self.DatasetName == 'abalone':
                return self.load_abalone()
            elif self.DatasetName == 'adult':
                return self.load_adult()
            elif self.DatasetName == 'balance':
                return self.load_balance()
            elif self.DatasetName == 'breast':
                return self.load_breast()
            elif self.DatasetName == 'car':
                return self.load_car()
            elif self.DatasetName == 'cleveland':
                return self.load_cleveland()

    @staticmethod
    def load(file_path):
        dataset = pd.read_csv(file_path)
        X = dataset.drop(["class"], axis=1)
        y = dataset["class"]
        y.astype('int')

        X = MinMaxScaler().fit_transform(X)

        return X, y

    def load_abalone(self):
        return self.load("NewDatasets/abalone/abalone.csv")

    def load_adult(self):
        return self.load("NewDatasets/adult/adult.csv")

    def load_balance(self):
        return self.load("NewDatasets/balance/balance.csv")

    def load_breast(self):
        return self.load("NewDatasets/breast/breast.csv")

    def load_car(self):
        return self.load("NewDatasets/car/car.csv")

    def load_cleveland(self):
        return self.load("NewDatasets/cleveland/cleveland.csv")









