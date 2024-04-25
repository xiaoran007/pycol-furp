import os
import pandas as pd
from arff import dump
from arff import loads
from Data.DatasetsLoader import Dataset


class Util(object):
    def __init__(self):
        pass

    @staticmethod
    def save_as_arff(data, filename):
        with open(filename, 'w') as f:
            dump(data, f)

    def csv2arff(self, csv_filename, arff_filename):
        pass


datasets_list = ['Africa', 'BankNote', 'CreditApproval', 'CreditRisk', 'CreditCard', 'Ecoli', 'FakeBills',
                 'LoanPrediction', 'PageBlock', 'PageBlockDel', 'PredictTerm', 'SouthGermanCredit', 'Wine', 'WineRed',
                 'Yeast', 'YeastUn']

# Define the base directory where datasets are stored
base_directory = "Datasets"


def save_as_arff(data, filename):
    with open(filename, 'w') as f:
        dump(data, f)


def load_and_save_datasets():
    for dataset_name in datasets_list:
        print(f"Processing {dataset_name} dataset...")
        dataset = Dataset(dataset_name)
        X, y = dataset.GetDataset()
        result = pd.concat([pd.DataFrame(X), pd.Series(y, name="target")], axis=1)
        csv_filename = os.path.join('./EncodeDatasetsNew', f'{dataset_name}_result.csv')
        result.to_csv(csv_filename, index=False)  # Export to CSV
        # Save as ARFF (you can use your previously defined method to save as ARFF)

        arff_data = {
            'description': '',
            'relation': dataset_name,
            'attributes': [(str(col), 'REAL') for col in result.columns],
            'data': result.values.tolist()
        }

        # Save as ARFF
        arff_filename = os.path.join('./EncodeDatasetsNew', f'{dataset_name}.arff')
        save_as_arff(arff_data, arff_filename)


if __name__ == "__main__":
    load_and_save_datasets()
