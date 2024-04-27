import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 29 : 185 (Total: 214)
    minority class: "label" == 7
    majority class: "label" == 1 or 2 or 3 or 4 or 5 or 6
    meta: [0, 0, 0, 0, 0, 0, 0, 0, 0]
"""


def main():
    header = ["RI",
              "Na",
              "Mg",
              "Al",
              "Si",
              "K",
              "Ca",
              "Ba",
              "Fe",
              "label"]
    df = pd.read_csv("./glass_noHead.dat", names=header, delimiter=', ')
    print(df)
    print(df["label"].value_counts())

    # le = LabelEncoder()
    # df['LargestSpotSize'] = le.fit_transform(df['LargestSpotSize'])
    # df['SpotDistribution'] = le.fit_transform(df['SpotDistribution'])

    df.loc[df['label'] == 7, 'class'] = 1
    df.loc[df['label'] == 1, 'class'] = 0
    df.loc[df['label'] == 2, 'class'] = 0
    df.loc[df['label'] == 3, 'class'] = 0
    df.loc[df['label'] == 4, 'class'] = 0
    df.loc[df['label'] == 5, 'class'] = 0
    df.loc[df['label'] == 6, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./glass.csv", index=False)


if __name__ == "__main__":
    main()
