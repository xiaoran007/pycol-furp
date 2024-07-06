import os
import pandas as pd
from arff import dump
from arff import loads
from Data.DatasetsLoader import Dataset
from Data.NewDatasets.processedDataset import ProcessedDataset
from Data.NewDatasetsLoader import Dataset as newDataset


class Util(object):
    def __init__(self, dataset_type):
        self.type = dataset_type
        self.path = self._setPath()

    def _setPath(self):
        if self.type == "new":
            return "./NewDatasetsEncode"
        elif self.type == "old":
            return "./DatasetsEncode"

    @staticmethod
    def save_as_arff(data, filename):
        with open(filename, 'w') as f:
            dump(data, f)

    def csv2arff(self, dataset_name, cwd):
        os.chdir(os.path.dirname(__file__))
        print(f"Processing {dataset_name} dataset...")
        if self.type == "new":
            dataset = newDataset(dataset_name, os.path.dirname(__file__))
        elif self.type == "old":
            dataset = Dataset(dataset_name)
        else:
            print("Err.")
            exit(1)
        X, y = dataset.GetDataset()
        result = pd.concat([pd.DataFrame(X), pd.Series(y, name="target")], axis=1)
        csv_filename = os.path.join(self.path, f'{dataset_name}_result.csv')
        if os.path.exists(self.path):
            pass
        else:
            os.mkdir(self.path)
        result.to_csv(csv_filename, index=False)

        arff_data = {
            'description': '',
            'relation': dataset_name,
            'attributes': [(str(col), 'REAL') for col in result.columns],
            'data': result.values.tolist()
        }

        arff_filename = os.path.join(self.path, f'{dataset_name}.arff')
        self.save_as_arff(arff_data, arff_filename)
        os.chdir(cwd)
        print(f"Processed {dataset_name} dataset.")




