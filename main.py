import csv
from tqdm import tqdm
from complexity.Complexity import Complexity

dataset_paths = {
    'BankNote': 'EncodeDatasets/BankNote.arff',
    'CreditApproval': 'EncodeDatasets/CreditApproval.arff',
    'CreditRisk': 'EncodeDatasets/CreditRisk.arff',
    'Ecoli': 'EncodeDatasets/Ecoli.arff',
    'FakeBills': 'EncodeDatasets/FakeBills.arff'
}

"""
    Define meta, set numeric feature to 0 and categorical feature to 1
"""
dataset_meta = {
    'BankNote': [0, 0, 0, 0],
    'CreditApproval': [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    'CreditRisk': [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    'Ecoli': [0, 0, 0, 0, 0, 0, 0],
    'FakeBills': [0, 0, 0, 0, 0, 0]
}

"""
    Save results to csv file
"""
with open('dataset_results2.csv', 'w', newline='') as csvfile:
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

        calculations = [
            ('Feature overlap F1', dataset.F1),
            ('Feature overlap F1v', dataset.F1v),
            ('Feature overlap F2', dataset.F2),
            ('Feature overlap F3', dataset.F3),
            ('Feature overlap F4', dataset.F4),
            ('Feature overlap input_noise', dataset.input_noise),
            ('Structural overlap N1', dataset.N1),
            ('Structural overlap T1', dataset.T1),
            ('Structural overlap LSC', dataset.LSC),
            ('Structural overlap Clust', dataset.Clust),
            ('Structural overlap DBC', dataset.DBC),
            ('Structural overlap N2', dataset.N2),
            ('Structural overlap NSG', dataset.NSG),
            ('Structural overlap ICSV', dataset.ICSV),
            ('Instance-level overlap R_value', dataset.R_value),
            ('Instance-level overlap deg_overlap', dataset.deg_overlap),
            ('Instance-level overlap N3', dataset.N3),
            ('Instance-level overlap SI', dataset.SI),
            ('Instance-level overlap N4', dataset.N4),
            ('Instance-level overlap kDN', dataset.kDN),
            ('Instance-level overlap D3_value', dataset.D3_value),
            ('Instance-level overlap CM', dataset.CM),
            ('Instance-level overlap borderline', dataset.borderline),
            ('Multiresolution overlap C1', dataset.C1),
            ('Multiresolution overlap C2', dataset.C2),
            ('Multiresolution overlap purity', dataset.purity),
            ('Multiresolution overlap neighbourhood_separability', dataset.neighbourhood_separability)
        ]

        with tqdm(total=len(calculations), desc=f"Processing {dataset_name}") as pbar:
            for desc, func in calculations:
                row_data.update({desc: func()})
                pbar.update(1)

        writer.writerow(row_data)

        # print
        print(f"Processed {dataset_name}")
