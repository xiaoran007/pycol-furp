import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 4071 : 42309 (Total: 46380)
    minority class: "label" == 1
    majority class: "label" == 0
    meta: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
"""


def main():
    df = pd.read_csv("./employee_promotion.csv", delimiter=',')
    print(df)
    print(df["is_promoted"].value_counts())
    df = df.dropna(axis=0)
    print(df)
    print(df["is_promoted"].value_counts())

    df = df.drop(["employee_id"], axis=1)

    le = LabelEncoder()
    df['department'] = le.fit_transform(df['department'])
    df['region'] = le.fit_transform(df['region'])
    df['education'] = le.fit_transform(df['education'])
    df['gender'] = le.fit_transform(df['gender'])
    df['recruitment_channel'] = le.fit_transform(df['recruitment_channel'])

    df.loc[df['is_promoted'] == 1, 'class'] = 1
    df.loc[df['is_promoted'] == 0, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["is_promoted"], axis=1)
    df.to_csv("./Employee_Promote.csv", index=False)


if __name__ == "__main__":
    main()
