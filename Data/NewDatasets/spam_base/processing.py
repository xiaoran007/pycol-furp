import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 268 : 500 (Total: 768)
    minority class: "label" == 1
    majority class: "label" == 0
    meta: all 56 attributes is 0
"""


def main():
    head = list()
    for i in range(56):
        head.append(f"c{i}")
    head.append("label")
    df = pd.read_csv("./spambase.data", names=head, delimiter=',')
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

    df.loc[df['label'] == 1, 'class'] = 1
    df.loc[df['label'] != 1, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./spam_base.csv", index=False)


if __name__ == "__main__":
    main()
