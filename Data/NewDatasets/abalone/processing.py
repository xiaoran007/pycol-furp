import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 364: 3810 (Total: 4174)
    minority class: "Rings" >= 15
    majority class: "Rings" < 15
    meta: [1, 0, 0, 0, 0, 0, 0, 0]
"""


def main():
    header = ["Sex", "Length", "Diameter", "Height", "Whole_weight", "Shucked_weight", "Viscera_weight", "Shell_weight",
              "Rings"]
    df = pd.read_csv("./abalone_rmHead.dat", names=header)
    le = LabelEncoder()

    df['Sex'] = le.fit_transform(df['Sex'])

    df.loc[df['Rings'] >= 15, 'class'] = 1
    df.loc[df['Rings'] < 15, 'class'] = 0
    df = df.drop(["Rings"], axis=1)

    print(df)
    print(df["class"].value_counts())

    df.to_csv("./abalone.csv", index=False)


if __name__ == "__main__":
    main()
