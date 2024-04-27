import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 81 : 225 (Total: 306)
    minority class: "label" == 2
    majority class: "label" == 1
    meta: [0, 0, 0]
"""


def main():
    header = ["Age",
              "Year",
              "nodes",
              "label"]
    df = pd.read_csv("./haberman.data", names=header, delimiter=',')
    print(df)
    print(df["label"].value_counts())

    # le = LabelEncoder()
    # df['LargestSpotSize'] = le.fit_transform(df['LargestSpotSize'])
    # df['SpotDistribution'] = le.fit_transform(df['SpotDistribution'])

    df.loc[df['label'] == 2, 'class'] = 1
    df.loc[df['label'] == 1, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./Haberman.csv", index=False)


if __name__ == "__main__":
    main()
