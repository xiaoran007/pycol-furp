import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 81 : 196 (Total: 277)
    minority class: "label" == "recurrence-events"
    majority class: "label" == "no-recurrence-events"
    meta: [1, 1, 1, 1, 1, 1, 1, 1, 1]
"""


def main():
    header = ["label", "age", "menopause", "tumor-size", "inv-nodes", "node-caps", "deg-malig", "breast", "breast-quad", "irradiat"]
    df = pd.read_csv("./breast-cancer.data", names=header, delimiter=',')
    print(df)
    print(df["label"].value_counts())
    df = df.drop(df[df.eq('?').any(axis=1)].index)
    print(df["label"].value_counts())

    le = LabelEncoder()
    df['age'] = le.fit_transform(df['age'])
    df['menopause'] = le.fit_transform(df['menopause'])
    df['tumor-size'] = le.fit_transform(df['tumor-size'])
    df['inv-nodes'] = le.fit_transform(df['inv-nodes'])
    df['node-caps'] = le.fit_transform(df['node-caps'])
    df['deg-malig'] = le.fit_transform(df['deg-malig'])
    df['breast'] = le.fit_transform(df['breast'])
    df['breast-quad'] = le.fit_transform(df['breast-quad'])
    df['irradiat'] = le.fit_transform(df['irradiat'])

    df.loc[df['label'] == "recurrence-events", 'class'] = 1
    df.loc[df['label'] == "no-recurrence-events", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./breast.csv", index=False)


if __name__ == "__main__":
    main()
