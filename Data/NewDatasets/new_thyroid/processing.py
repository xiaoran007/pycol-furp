import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 30 : 185 (Total: 215)
    minority class: "label" == 3
    majority class: "label" == 1 or 2
    meta: [0, 0, 0, 0, 0]
"""


def main():
    head = list()
    for i in range(5):
        head.append(f"c{i}")
    head.append("label")
    df = pd.read_csv("./new_thyroid_noHead.dat", names=head, delimiter=',')
    print(df)
    print(df["label"].value_counts())

    # le = LabelEncoder()
    # df['REASON'] = le.fit_transform(df['REASON'])
    # df['JOB'] = le.fit_transform(df['JOB'])

    df.loc[df['label'] == 3, 'class'] = 1
    df.loc[df['label'] != 3, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./new_thyroid.csv", index=False)


if __name__ == "__main__":
    main()
