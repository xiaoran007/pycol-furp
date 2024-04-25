class ProcessedDataset(object):
    def __init__(self):
        self.datasetNameList = list()
        self.datasetNameList.append("abalone")
        self.datasetNameList.append("adult")
        self.datasetNameList.append("balance")

    def GetDatasetList(self):
        return self.datasetNameList



