import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 35 : 262 (Total: 297)
    minority class: "label" == "2"
    majority class: "label" == "0" or "1" or "3" or "4"
    meta: [0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
"""


def main():
    header = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "label"]
    df = pd.read_csv("./processed.cleveland.data", names=header, delimiter=',')
    print(df)
    print(df["label"].value_counts())
    df = df.drop(df[df.eq('?').any(axis=1)].index)
    print(df["label"].value_counts())

    df.loc[df['label'] == 2, 'class'] = 1
    df.loc[df['label'] == 0, 'class'] = 0
    df.loc[df['label'] == 1, 'class'] = 0
    df.loc[df['label'] == 3, 'class'] = 0
    df.loc[df['label'] == 4, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./cleveland.csv", index=False)


if __name__ == "__main__":
    main()
