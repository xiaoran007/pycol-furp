class ProcessedDataset(object):
    def __init__(self):
        self.datasetNameList = list()
        self.datasetMetaDict = dict()
        self._init_datasetNameList()
        self._init_datasetMetaDict()

    def GetDatasetList(self):
        return self.datasetNameList

    def GetDatasetMeta(self, dataset_name):
        if dataset_name not in self.datasetNameList:
            print('Err.')
        else:
            return self.datasetMetaDict[dataset_name]


    def _init_datasetNameList(self):
        self.datasetNameList.append("abalone")
        self.datasetNameList.append("adult")
        self.datasetNameList.append("balance")
        self.datasetNameList.append("breast")
        self.datasetNameList.append("car")
        self.datasetNameList.append("cleveland")
        self.datasetNameList.append("Company_Bankruptcy")

    def _init_datasetMetaDict(self):
        self.datasetMetaDict["abalone"] = [1, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict["adult"] = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1]
        self.datasetMetaDict["balance"] = [0, 0, 0, 0]
        self.datasetMetaDict["breast"] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.datasetMetaDict["car"] = [1, 1, 1, 1, 1, 1]
        self.datasetMetaDict["cleveland"] = [0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
        self.datasetMetaDict["Company_Bankruptcy"] = self._Company_Bankruptcy()

    @staticmethod
    def _Company_Bankruptcy():
        meta = list()
        for i in range(93):
            meta.append(0)
        meta.append(1)
        meta.append(1)
        return meta

