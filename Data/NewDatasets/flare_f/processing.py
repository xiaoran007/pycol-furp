import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 147 : 919 (Total: 1066)
    minority class: "label" == "B"
    majority class: "label" == "H" or "D" or "C" or "E" or "F"
    meta: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
"""


def main():
    header = ["LargestSpotSize",
              "SpotDistribution",
              "Activity",
              "Evolution",
              "Prev24Hour",
              "HistComplex",
              "BecomeHist",
              "Area",
              "C-class",
              "M-class",
              "X-class",
              "label"]
    df = pd.read_csv("./flare_noHead.dat", names=header, delimiter=', ')
    print(df)
    print(df["label"].value_counts())

    le = LabelEncoder()
    df['LargestSpotSize'] = le.fit_transform(df['LargestSpotSize'])
    df['SpotDistribution'] = le.fit_transform(df['SpotDistribution'])

    df.loc[df['label'] == "B", 'class'] = 1
    df.loc[df['label'] == "H", 'class'] = 0
    df.loc[df['label'] == "D", 'class'] = 0
    df.loc[df['label'] == "C", 'class'] = 0
    df.loc[df['label'] == "E", 'class'] = 0
    df.loc[df['label'] == "F", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./flare_f.csv", index=False)


if __name__ == "__main__":
    main()
