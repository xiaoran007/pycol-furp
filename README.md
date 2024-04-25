# pycol-furp
pycol

## Environment Setup
```shell
conda create -n pycol python=3.9
conda activate pycol
conda install jupyter pandas imbalanced-learn scikit-learn statsmodels liac-arff tqdm
```

## Note
* Package Complexity.py is modified from the paper code.

## TODO
* Implement processing.py for each dataset, in each folder, clean dataset and set minority and majority class. (example see abalone, adult and balance folder)
* Implement high-level data load API for new dataset in NewDatasetLoader.py
* Implement Evaluation code for new dataset, example see main.py and test.py.