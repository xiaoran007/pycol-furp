import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 12414 : 45586 (Total: 58000)
    minority class: "label" == other than 1
    majority class: "label" == 1
    meta: [0, 0, 0, 0, 0, 0, 0, 0, 0]
"""


def main():
    head = list()
    for i in range(9):
        head.append(f"c{i}")
    head.append("label")
    train_df = pd.read_csv("./shuttle.trn", names=head, delimiter=' ')
    test_df = pd.read_csv("./shuttle.tst", names=head, delimiter=' ')
    df = pd.concat([train_df, test_df], ignore_index=True)
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

    df.loc[df['label'] == 1, 'class'] = 0
    df.loc[df['label'] != 1, 'class'] = 1
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./shuttle.csv", index=False)


if __name__ == "__main__":
    main()
