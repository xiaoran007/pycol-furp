import os
from complexity.Complexity import Complexity
from Data.Datasets.processedDataset import ProcessedDataset
from Data.DatasetsLoader import Dataset
import Data
import pandas as pd


processed_dataset = ProcessedDataset()
dataset_names = processed_dataset.GetDatasetList()

def test1():
    complexity = Complexity("./Data/NewDatasets/abalone/abalone.csv", meta=[1, 0, 0, 0, 0, 0, 0, 0], distance_func="default", file_type="csv")


    print(complexity.T1())

    print(complexity.R_value())
    print(complexity.D3_value())
    print(complexity.CM())
    print(complexity.kDN())
    print(complexity.MRCA())
    print(complexity.DBC())
    print(complexity.SI())
    print(complexity.input_noise())
    print(complexity.borderline())
    print(complexity.deg_overlap())

    print(complexity.ICSV())
    print(complexity.NSG())

    print(complexity.C1())
    print(complexity.C2())
    print(complexity.Clust())
    print(complexity.purity())
    print(complexity.neighbourhood_separability())
    print(complexity.N1())
    print(complexity.N2())
    print(complexity.N3())
    print(complexity.N4())
    print(complexity.LSC())


    #print(complexity.T1())



    print(complexity.F1())
    print(complexity.F1v())
    print(complexity.F2())
    print(complexity.F3())
    print(complexity.F4())


def test2():
    for dataset_name in dataset_names:
        if dataset_name in processed_dataset.GetSkipDatasetList():
            continue
        try:
            dataset = Complexity(f"./Data/DatasetsEncode/{dataset_name}.arff",
                                 processed_dataset.datasetMetaDict[dataset_name], distance_func="default", file_type="arff")
            print(f"pass: {dataset_name}")
        except:
            print(f"error: {dataset_name}")


def test3():
    dataset_name = "CreditApproval"
    dataset = Complexity(f"./Data/DatasetsEncode/{dataset_name}.arff", processed_dataset.datasetMetaDict[dataset_name], distance_func="default", file_type="arff")
    os.chdir(os.path.dirname(Data.__file__))
    X, y = Dataset(dataset_name).GetDataset()
    print(X)
    print(pd.DataFrame(X))


test2()
