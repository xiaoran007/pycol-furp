import os
from Data.NewDatasets.processedDataset import ProcessedDataset
from Data.NewDatasetsLoader import Dataset
from Data import util


dataset_list = ProcessedDataset().datasetNameList
helper = util.Util()

for dataset_name in dataset_list:
    helper.csv2arff(dataset_name, os.path.join(os.path.dirname(__file__)))
