import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 239 : 444 (Total: 683)
    minority class: "label" == 4
    majority class: "label" == 2
    meta: [1, 1, 1, 1, 1, 1, 1, 1, 1]
"""


def main():
    head = list()
    head.append("id")
    for i in range(9):
        head.append(f"c{i}")
    head.append("label")
    df = pd.read_csv("./breast-cancer-wisconsin.data", names=head, delimiter=',')
    df = df.drop(df[df.eq('?').any(axis=1)].index)
    df = df.drop(["id"], axis=1)
    print(df)
    print(df["label"].value_counts())

    # le = LabelEncoder()
    # df['c0'] = le.fit_transform(df['c0'])
    # df['c1'] = le.fit_transform(df['c1'])
    # df['c2'] = le.fit_transform(df['c2'])
    # df['c4'] = le.fit_transform(df['c4'])
    # df['c5'] = le.fit_transform(df['c5'])
    # df['c6'] = le.fit_transform(df['c6'])
    # df['c7'] = le.fit_transform(df['c7'])

    df.loc[df['label'] == 4, 'class'] = 1
    df.loc[df['label'] != 4, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./wisconsin.csv", index=False)


if __name__ == "__main__":
    main()
