import csv
from tqdm import tqdm
from complexity.Complexity import Complexity

dataset_paths = {
    'Africa': 'EncodeDatasets/Africa.arff',
    'BankNote': 'EncodeDatasets/BankNote.arff',
    'CreditApproval': 'EncodeDatasets/CreditApproval.arff',
    'CreditRisk': 'EncodeDatasets/CreditRisk.arff',
    #     'CreditCard': 'EncodeDatasets/CreditCard.arff',
    'Ecoli': 'EncodeDatasets/Ecoli.arff',
    'FakeBills': 'EncodeDatasets/FakeBills.arff',
    'LoanPrediction': 'EncodeDatasets/LoanPrediction.arff',
    'PageBlock': 'EncodeDatasets/PageBlock.arff',
    'PageBlockDel': 'EncodeDatasets/PageBlockDel.arff',
    #     'PredictTerm': 'EncodeDatasets/PredictTerm.arff',
    'SouthGermanCredit': 'EncodeDatasets/SouthGermanCredit.arff',
    'Wine': 'EncodeDatasets/Wine.arff',
    'WineRed': 'EncodeDatasets/WineRed.arff',
    'Yeast': 'EncodeDatasets/Yeast.arff',
    'YeastUn': 'EncodeDatasets/YeastUn.arff'
}

# 自己定义meta，就不用理arff文件中原本的REAL了，会重新分配 numeric 和 REAL(把category variable 给 encoding 后存为 REAL)
dataset_meta = {
    'Africa': [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    'BankNote': [0, 0, 0, 0],
    'CreditApproval': [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    'CreditRisk': [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    #    'CreditCard': [0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    'Ecoli': [0, 0, 0, 0, 0, 0, 0],
    'FakeBills': [0, 0, 0, 0, 0, 0],
    'LoanPrediction': [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    'PageBlock': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'PageBlockDel': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    'PredictTerm': [0,1,1,1,1,0,1,1,1,0,1,0,0,0,0,1],
    'SouthGermanCredit': [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    'Wine': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'WineRed': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Yeast': [0, 0, 0, 0, 0, 0, 0, 0],
    'YeastUn': [0, 0, 0, 0, 0, 0, 0, 0]
}

# 创建一个CSV文件来保存结果
with open('dataset_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['Dataset', 'Feature overlap F1', 'Feature overlap F1v', 'Feature overlap F2', 'Feature overlap F3',
                  'Feature overlap F4', 'Feature overlap input_noise', 'Structural overlap N1', 'Structural overlap T1',
                  'Structural overlap LSC', 'Structural overlap Clust', 'Structural overlap DBC',
                  'Structural overlap N2', 'Structural overlap NSG', 'Structural overlap ICSV',
                  'Instance-level overlap R_value', 'Instance-level overlap deg_overlap', 'Instance-level overlap N3',
                  'Instance-level overlap SI', 'Instance-level overlap N4', 'Instance-level overlap kDN',
                  'Instance-level overlap D3_value', 'Instance-level overlap CM', 'Instance-level overlap borderline',
                  'Multiresolution overlap C1', 'Multiresolution overlap C2', 'Multiresolution overlap purity',
                  'Multiresolution overlap neighbourhood_separability']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for dataset_name, dataset_path in tqdm(dataset_paths.items(), desc="Processing Datasets"):
        dataset = Complexity(dataset_path, dataset_meta[dataset_name], distance_func="default", file_type="arff")

        row_data = {
            'Dataset': dataset_name
        }

        sub_progressbar = tqdm(total=27, desc="Sub Processing")
        row_data.update({'Feature overlap F1': dataset.F1()})
        sub_progressbar.update(1)
        row_data.update({'Feature overlap F1v': dataset.F1v()})
        sub_progressbar.update(1)
        row_data.update({'Feature overlap F2': dataset.F2()})
        sub_progressbar.update(1)
        row_data.update({'Feature overlap F3': dataset.F3()})
        sub_progressbar.update(1)
        row_data.update({'Feature overlap F4': dataset.F4()})
        sub_progressbar.update(1)
        row_data.update({'Feature overlap input_noise': dataset.input_noise()})
        sub_progressbar.update(1)
        row_data.update({'Structural overlap N1': dataset.N1()})
        sub_progressbar.update(1)
        row_data.update({'Structural overlap T1': dataset.T1()})
        sub_progressbar.update(1)
        row_data.update({'Structural overlap LSC': dataset.LSC()})
        sub_progressbar.update(1)
        row_data.update({'Structural overlap Clust': dataset.Clust()})
        sub_progressbar.update(1)
        row_data.update({'Structural overlap DBC': dataset.DBC()})
        sub_progressbar.update(1)
        row_data.update({'Structural overlap N2': dataset.N2()})
        sub_progressbar.update(1)
        row_data.update({'Structural overlap NSG': dataset.NSG()})
        sub_progressbar.update(1)
        row_data.update({'Structural overlap ICSV': dataset.ICSV()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap R_value': dataset.R_value()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap deg_overlap': dataset.deg_overlap()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap N3': dataset.N3()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap SI': dataset.SI()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap N4': dataset.N4()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap kDN': dataset.kDN()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap D3_value': dataset.D3_value()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap CM': dataset.CM()})
        sub_progressbar.update(1)
        row_data.update({'Instance-level overlap borderline': dataset.borderline()})
        sub_progressbar.update(1)
        row_data.update({'Multiresolution overlap C1': dataset.C1()})
        sub_progressbar.update(1)
        row_data.update({'Multiresolution overlap C2': dataset.C2()})
        sub_progressbar.update(1)
        row_data.update({'Multiresolution overlap purity': dataset.purity()})
        sub_progressbar.update(1)
        row_data.update({'Multiresolution overlap neighbourhood_separability': dataset.neighbourhood_separability()})
        sub_progressbar.update(1)
        sub_progressbar.close()

        writer.writerow(row_data)

        # print
        print(f"Processed {dataset_name}")
