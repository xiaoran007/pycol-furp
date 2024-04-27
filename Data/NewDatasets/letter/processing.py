import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 789 : 19211 (Total: 20000)
    minority class: "label" == "A"
    majority class: "label" == other than "A"
    meta: all 16 attributes is 0
"""


def main():
    head = ["label"]
    for i in range(16):
        head.append(f"c{i}")
    df = pd.read_csv("./letter-recognition.data", names=head, delimiter=',')
    print(df)
    print(df["label"].value_counts())

    # le = LabelEncoder()
    # df['REASON'] = le.fit_transform(df['REASON'])
    # df['JOB'] = le.fit_transform(df['JOB'])

    df.loc[df['label'] == "A", 'class'] = 1
    df.loc[df['label'] != "A", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./letter.csv", index=False)


if __name__ == "__main__":
    main()
