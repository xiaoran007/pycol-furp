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

    @staticmethod
    def GetSkipDatasetList():
        return ["CreditCard", "PredictTerm"]

    def _init_datasetNameList(self):
        self.datasetNameList.append("Africa")
        self.datasetNameList.append("BankNote")
        self.datasetNameList.append("CreditApproval")
        self.datasetNameList.append("CreditRisk")
        self.datasetNameList.append("CreditCard")
        self.datasetNameList.append("Ecoli")
        self.datasetNameList.append("FakeBills")
        self.datasetNameList.append("LoanPrediction")
        self.datasetNameList.append("PageBlock")
        self.datasetNameList.append("PageBlockDel")
        self.datasetNameList.append("PredictTerm")
        self.datasetNameList.append("SouthGermanCredit")
        self.datasetNameList.append("Wine")
        self.datasetNameList.append("WineRed")
        self.datasetNameList.append("Yeast")
        self.datasetNameList.append("YeastUn")

    def _init_datasetMetaDict(self):
        self.datasetMetaDict['Africa'] = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
        self.datasetMetaDict['BankNote'] = [0, 0, 0, 0]
        self.datasetMetaDict['CreditApproval'] = [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0]
        self.datasetMetaDict['CreditRisk'] = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
        self.datasetMetaDict['CreditCard'] = [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict['Ecoli'] = [0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict['FakeBills'] = [0, 0, 0, 0, 0, 0]
        self.datasetMetaDict['LoanPrediction'] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
        self.datasetMetaDict['PageBlock'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict['PageBlockDel'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict['PredictTerm'] = [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1]
        self.datasetMetaDict['SouthGermanCredit'] = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
        self.datasetMetaDict['Wine'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict['WineRed'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict['Yeast'] = [0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict['YeastUn'] = [0, 0, 0, 0, 0, 0, 0, 0]
