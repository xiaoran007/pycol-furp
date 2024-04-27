import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 50 : 100 (Total: 150)
    minority class: "label" == "Iris-setosa"
    majority class: "label" == "Iris-versicolor" or "Iris-virginica"
    meta: [0, 0, 0, 0]
"""


def main():
    head = ["sepal length",
            "sepal width",
            "petal length",
            "petal width",
            "label"]
    df = pd.read_csv("./iris.data", names=head, delimiter=',')
    print(df)
    print(df["label"].value_counts())

    # le = LabelEncoder()
    # df['REASON'] = le.fit_transform(df['REASON'])
    # df['JOB'] = le.fit_transform(df['JOB'])

    df.loc[df['label'] == "Iris-setosa", 'class'] = 1
    df.loc[df['label'] == "Iris-versicolor", 'class'] = 0
    df.loc[df['label'] == "Iris-virginica", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./iris.csv", index=False)


if __name__ == "__main__":
    main()
