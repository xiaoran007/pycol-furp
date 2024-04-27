import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 330 : 1980 (Total: 2310)
    minority class: "label" == "SKY"
    majority class: "label" == other than "SKY"
    meta: all 19 attributes is 0
"""


def main():
    head = list()
    head.append("label")
    for i in range(19):
        head.append(f"c{i}")
    train_df = pd.read_csv("./data_noHead.dat", names=head, delimiter=',')
    test_df = pd.read_csv("./test_noHead.dat", names=head, delimiter=',')
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

    df.loc[df['label'] == "SKY", 'class'] = 1
    df.loc[df['label'] != "SKY", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./segment.csv", index=False)


if __name__ == "__main__":
    main()
