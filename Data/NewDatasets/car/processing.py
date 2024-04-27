import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 384 : 1344 (Total: 1728)
    minority class: "label" == "acc"
    majority class: "label" == "unacc" or "good" or "v-good"
    meta: [1, 1, 1, 1, 1, 1]
"""


def main():
    header = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "label"]
    df = pd.read_csv("./car.data", names=header, delimiter=',')
    print(df)
    print(df["label"].value_counts())

    le = LabelEncoder()
    df['buying'] = le.fit_transform(df['buying'])
    df['maint'] = le.fit_transform(df['maint'])
    df['doors'] = le.fit_transform(df['doors'])
    df['persons'] = le.fit_transform(df['persons'])
    df['lug_boot'] = le.fit_transform(df['lug_boot'])
    df['safety'] = le.fit_transform(df['safety'])

    df.loc[df['label'] == "acc", 'class'] = 1
    df.loc[df['label'] == "unacc", 'class'] = 0
    df.loc[df['label'] == "good", 'class'] = 0
    df.loc[df['label'] == "vgood", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./car.csv", index=False)


if __name__ == "__main__":
    main()
