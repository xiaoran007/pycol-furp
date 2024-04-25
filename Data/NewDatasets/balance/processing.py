import pandas as pd

"""
    imbalance ratio minority class : majority class = 49 : 576 (Total: 625)
    minority class: "label" == "B"
    majority class: "label" == "L" or "R"
    meta: [0, 0, 0, 0]
"""


def main():
    header = ["label", "Left-Weight", "Left-Distance", "Right-Weight", "Right-Distance"]
    df = pd.read_csv("./balance-scale.data", names=header, delimiter=',')
    print(df)
    print(df["label"].value_counts())
    df.loc[df['label'] == "B", 'class'] = 1
    df.loc[df['label'] == "L", 'class'] = 0
    df.loc[df['label'] == "R", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./balance.csv", index=False)


if __name__ == "__main__":
    main()
