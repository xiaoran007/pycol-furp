import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 220 : 6599 (Total: 6819)
    minority class: "Bankrupt?" == "1"
    majority class: "Bankrupt?" == "0"
    meta: 0-92: 0, 93-94: 1
"""


def main():
    df = pd.read_csv("./data.csv", delimiter=',')
    print(df)
    print(df["Bankrupt?"].value_counts())
    df = df.dropna(axis=0)
    print(df["Bankrupt?"].value_counts())

    df[" Liability-Assets Flag-C"] = df[" Liability-Assets Flag"]
    df[" Net Income Flag-C"] = df[" Net Income Flag"]

    df.loc[df['Bankrupt?'] == 1, 'class'] = 1
    df.loc[df['Bankrupt?'] == 0, 'class'] = 0

    print(df["class"].value_counts())
    df = df.drop(["Bankrupt?"], axis=1)
    df = df.drop([" Liability-Assets Flag"], axis=1)
    df = df.drop([" Net Income Flag"], axis=1)
    df.to_csv("./Company_Bankruptcy.csv", index=False)


if __name__ == "__main__":
    main()
