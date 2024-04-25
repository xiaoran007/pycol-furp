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









