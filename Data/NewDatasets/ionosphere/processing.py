import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 126 : 225 (Total: 351)
    minority class: "label" == "b"
    majority class: "label" == "g"
    meta: all 34 attributes is 0
"""


def main():
    head = list()
    for i in range(34):
        head.append(f"c{i}")
    head.append("label")
    df = pd.read_csv("./ionosphere.data", names=head, delimiter=',')
    print(df)
    print(df["label"].value_counts())

    # le = LabelEncoder()
    # df['REASON'] = le.fit_transform(df['REASON'])
    # df['JOB'] = le.fit_transform(df['JOB'])

    df.loc[df['label'] == "b", 'class'] = 1
    df.loc[df['label'] == "g", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./ionosphere.csv", index=False)


if __name__ == "__main__":
    main()
