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
            elif self.DatasetName == 'Company_Bankruptcy':
                return self.load_Company_Bankruptcy()
            elif self.DatasetName == 'derma':
                return self.load_derma()
            elif self.DatasetName == 'Employee_Promote':
                return self.load_Employee_Promote()
            elif self.DatasetName == 'flare_f':
                return self.load_flare_f()
            elif self.DatasetName == 'glass':
                return self.load_glass()
            elif self.DatasetName == 'Haberman':
                return self.load_Haberman()
            elif self.DatasetName == 'Home_Equity':
                return self.load_Home_Equity()
            elif self.DatasetName == 'ionosphere':
                return self.load_ionosphere()
            elif self.DatasetName == "iris":
                return self.load_iris()
            elif self.DatasetName == "letter":
                return self.load_letter()
            elif self.DatasetName == "libra":
                return self.load_libra()
            elif self.DatasetName == "liver":
                return self.load_liver()
            elif self.DatasetName == "new_thyroid":
                return self.load_new_thyroid()
            elif self.DatasetName == "nursery":
                return self.load_nursery()
            elif self.DatasetName == "Online_Shoppers_Intention":
                return self.load_Online_Shoppers_Intention()
            elif self.DatasetName == "pima":
                return self.load_pima()
            elif self.DatasetName == "Satimage":
                return self.load_Satimage()

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

    def load_Company_Bankruptcy(self):
        return self.load("NewDatasets/Company_Bankruptcy/Company_Bankruptcy.csv")

    def load_derma(self):
        return self.load("NewDatasets/derma/derma.csv")

    def load_Employee_Promote(self):
        return self.load("NewDatasets/Employee_Promote/Employee_Promote.csv")

    def load_flare_f(self):
        return self.load("NewDatasets/flare_f/flare_f.csv")

    def load_glass(self):
        return self.load("NewDatasets/glass/glass.csv")

    def load_Haberman(self):
        return self.load("NewDatasets/Haberman/Haberman.csv")

    def load_Home_Equity(self):
        return self.load("NewDatasets/Home_Equity/Home_Equity.csv")

    def load_ionosphere(self):
        return self.load("NewDatasets/ionosphere/ionosphere.csv")

    def load_iris(self):
        return self.load("NewDatasets/iris/iris.csv")

    def load_letter(self):
        return self.load("NewDatasets/letter/letter.csv")

    def load_libra(self):
        return self.load("NewDatasets/libra/libra.csv")

    def load_liver(self):
        return self.load("NewDatasets/liver/liver.csv")

    def load_new_thyroid(self):
        return self.load("NewDatasets/new_thyroid/new_thyroid.csv")

    def load_nursery(self):
        return self.load("NewDatasets/nursery/nursery.csv")

    def load_Online_Shoppers_Intention(self):
        return self.load("NewDatasets/Online_Shoppers_Intention/Online_Shoppers_Intention.csv")

    def load_pima(self):
        return self.load("NewDatasets/pima/pima.csv")

    def load_Satimage(self):
        return self.load("NewDatasets/Satimage/Satimage.csv")









