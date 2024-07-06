import os
from Data.NewDatasets.processedDataset import ProcessedDataset
from Data.NewDatasetsLoader import Dataset as newDataset
from Data.DatasetsLoader import Datasets_list, Dataset
from Data import util


dataset_list = Datasets_list
helper = util.Util(dataset_type="old")

for dataset_name in dataset_list:
    helper.csv2arff(dataset_name, os.path.join(os.path.dirname(__file__)))
