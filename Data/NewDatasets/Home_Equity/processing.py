import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 300 : 3064 (Total: 3364)
    minority class: "BAD" == 1
    majority class: "BAD" == 0
    meta: [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
"""


def main():
    df = pd.read_csv("./hmeq.csv", delimiter=',')
    print(df)
    df = df.dropna(axis=0)
    print(df)
    print(df["BAD"].value_counts())

    le = LabelEncoder()
    df['REASON'] = le.fit_transform(df['REASON'])
    df['JOB'] = le.fit_transform(df['JOB'])

    df.loc[df['BAD'] == 1, 'class'] = 1
    df.loc[df['BAD'] == 0, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["BAD"], axis=1)
    df.to_csv("./Home_Equity.csv", index=False)


if __name__ == "__main__":
    main()
