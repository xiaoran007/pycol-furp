import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 268 : 500 (Total: 768)
    minority class: "label" == 0
    majority class: "label" == other than 0
    meta: [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""


def main():
    head = list()
    for i in range(13):
        head.append(f"c{i}")
    head.append("label")
    df = pd.read_csv("./vowel_noHead.dat", names=head, delimiter=',')
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

    df.loc[df['label'] == 0, 'class'] = 1
    df.loc[df['label'] != 0, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./vowel.csv", index=False)


if __name__ == "__main__":
    main()
