from complexity.Complexity import Complexity
from Data.NewDatasets.processedDataset import ProcessedDataset
from Data.NewDatasetsLoader import Dataset
import json
import os

a = ProcessedDataset()
d_list = a.datasetNameList


def skip():
    skip_list = list()
    for i in d_list:
        _, y = Dataset(i, os.path.dirname(__file__)).GetDataset()
        print(f"dataset: {i}, len: {len(y)}")
        if len(y) > 15000:
            skip_list.append(i)

    print(skip_list)


def run():
    with open("./Data/NewDatasets/datasetCheck.json", "r") as f:
        checked_list = json.load(f)
    for i in d_list:
        if i in checked_list:
            print(f"dataset: {i} pass")
            continue
        if i in ['adult', 'Employee_Promote', 'letter', 'shuttle']:
            continue
        try:
            path = f"./Data/NewDatasets/{i}/{i}.csv"
            print(f"start: {i}")
            complexity = Complexity(path, meta=a.datasetMetaDict[i],
                                    distance_func="default", file_type="csv")
            cm = complexity.CM()
            with open("./Data/NewDatasets/datasetCheck.json", "w") as f:
                checked_list.append(i)
                json.dump(checked_list, f)
            print(f"dataset: {i} pass, c1: {cm}")
        except Exception as e:
            print(f"dataset: {i} fail")
            print(e)
            break


run()

