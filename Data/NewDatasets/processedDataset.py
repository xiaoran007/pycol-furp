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
        self.datasetNameList.append("derma")
        self.datasetNameList.append("Employee_Promote")
        self.datasetNameList.append("flare_f")
        self.datasetNameList.append("glass")
        self.datasetNameList.append("Haberman")
        self.datasetNameList.append("Home_Equity")
        self.datasetNameList.append("ionosphere")
        self.datasetNameList.append("iris")
        self.datasetNameList.append("letter")
        self.datasetNameList.append("libra")
        self.datasetNameList.append("liver")
        self.datasetNameList.append("new_thyroid")
        self.datasetNameList.append("nursery")
        self.datasetNameList.append("Online_Shoppers_Intention")
        self.datasetNameList.append("pima")
        self.datasetNameList.append("Satimage")
        self.datasetNameList.append("segment")
        self.datasetNameList.append("shuttle")
        self.datasetNameList.append("spam_base")
        self.datasetNameList.append("Vehicle")
        self.datasetNameList.append("vowel")

    def _init_datasetMetaDict(self):
        self.datasetMetaDict["abalone"] = [1, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict["adult"] = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1]
        self.datasetMetaDict["balance"] = [0, 0, 0, 0]
        self.datasetMetaDict["breast"] = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.datasetMetaDict["car"] = [1, 1, 1, 1, 1, 1]
        self.datasetMetaDict["cleveland"] = [0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
        self.datasetMetaDict["Company_Bankruptcy"] = self._Company_Bankruptcy()
        self.datasetMetaDict["derma"] = self._derma()
        self.datasetMetaDict["Employee_Promote"] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        self.datasetMetaDict["flare_f"] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.datasetMetaDict["glass"] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict["Haberman"] = [0, 0, 0]
        self.datasetMetaDict["Home_Equity"] = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict["ionosphere"] = self._ionosphere()
        self.datasetMetaDict["iris"] = [0, 0, 0, 0]
        self.datasetMetaDict["letter"] = self._letter()
        self.datasetMetaDict["libra"] = self._libra()
        self.datasetMetaDict["liver"] = [0, 0, 0, 0, 0, 0]
        self.datasetMetaDict["new_thyroid"] = [0, 0, 0, 0, 0]
        self.datasetMetaDict["nursery"] = [1, 1, 1, 0, 1, 1, 1, 1]
        self.datasetMetaDict["Online_Shoppers_Intention"] = self._Online_Shoppers_Intention()
        self.datasetMetaDict["pima"] = [0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict["Satimage"] = self._Satimage()
        self.datasetMetaDict["segment"] = self._segment()
        self.datasetMetaDict["shuttle"] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.datasetMetaDict["spam_base"] = self._spam_base()
        self.datasetMetaDict["Vehicle"] = self._Vehicle()
        self.datasetMetaDict["vowel"] = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    @staticmethod
    def _Company_Bankruptcy():
        meta = list()
        for i in range(93):
            meta.append(0)
        meta.append(1)
        meta.append(1)
        return meta

    @staticmethod
    def _derma():
        meta = list()
        for i in range(33):
            meta.append(0)
        meta.append(1)
        return meta

    @staticmethod
    def _ionosphere():
        meta = list()
        for i in range(34):
            meta.append(0)
        return meta

    @staticmethod
    def _letter():
        meta = list()
        for i in range(16):
            meta.append(0)
        return meta

    @staticmethod
    def _libra():
        meta = list()
        for i in range(90):
            meta.append(0)
        return meta

    @staticmethod
    def _Online_Shoppers_Intention():
        meta = list()
        for i in range(15):
            meta.append(0)
        meta.append(1)
        meta.append(1)
        return meta

    @staticmethod
    def _Satimage():
        meta = list()
        for i in range(36):
            meta.append(0)
        return meta

    @staticmethod
    def _segment():
        meta = list()
        for i in range(19):
            meta.append(0)
        return meta

    @staticmethod
    def _spam_base():
        meta = list()
        for i in range(56):
            meta.append(0)
        return meta

    @staticmethod
    def _Vehicle():
        meta = list()
        for i in range(18):
            meta.append(0)
        return meta

