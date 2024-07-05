import os
import pandas as pd
from arff import dump
from arff import loads
from Data.DatasetsLoader import Dataset
from Data.NewDatasets.processedDataset import ProcessedDataset
from Data.NewDatasetsLoader import Dataset as newDataset


class Util(object):
    def __init__(self):
        pass

    @staticmethod
    def save_as_arff(data, filename):
        with open(filename, 'w') as f:
            dump(data, f)

    def csv2arff(self, dataset_name, cwd):
        os.chdir(os.path.dirname(__file__))
        print(f"Processing {dataset_name} dataset...")
        dataset = newDataset(dataset_name, os.path.dirname(__file__))
        X, y = dataset.GetDataset()
        result = pd.concat([pd.DataFrame(X), pd.Series(y, name="target")], axis=1)
        csv_filename = os.path.join('./NewDatasetsEncode', f'{dataset_name}_result.csv')
        result.to_csv(csv_filename, index=False)

        arff_data = {
            'description': '',
            'relation': dataset_name,
            'attributes': [(str(col), 'REAL') for col in result.columns],
            'data': result.values.tolist()
        }

        arff_filename = os.path.join('./NewDatasetsEncode', f'{dataset_name}.arff')
        self.save_as_arff(arff_data, arff_filename)
        os.chdir(cwd)
        print(f"Processed {dataset_name} dataset.")




