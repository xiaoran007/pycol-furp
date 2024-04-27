import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 199 : 647 (Total: 846)
    minority class: "label" == "van"
    majority class: "label" == other than "van"
    meta: all 18 attributes is 0
"""


def main():
    head = list()
    for i in range(18):
        head.append(f"c{i}")
    head.append("label")
    head.append("sp")
    xaa = pd.read_csv("./xaa.dat", names=head, delimiter=' ')
    xab = pd.read_csv("./xab.dat", names=head, delimiter=' ')
    xac = pd.read_csv("./xac.dat", names=head, delimiter=' ')
    xad = pd.read_csv("./xad.dat", names=head, delimiter=' ')
    xae = pd.read_csv("./xae.dat", names=head, delimiter=' ')
    xaf = pd.read_csv("./xaf.dat", names=head, delimiter=' ')
    xag = pd.read_csv("./xag.dat", names=head, delimiter=' ')
    xah = pd.read_csv("./xah.dat", names=head, delimiter=' ')
    xai = pd.read_csv("./xai.dat", names=head, delimiter=' ')
    df = pd.concat([xaa, xab, xac, xad, xae, xaf, xag, xah, xai], ignore_index=True)
    print(df)
    print(df["label"].value_counts())

    df = df.drop(["sp"], axis=1)

    # le = LabelEncoder()
    # df['c0'] = le.fit_transform(df['c0'])
    # df['c1'] = le.fit_transform(df['c1'])
    # df['c2'] = le.fit_transform(df['c2'])
    # df['c4'] = le.fit_transform(df['c4'])
    # df['c5'] = le.fit_transform(df['c5'])
    # df['c6'] = le.fit_transform(df['c6'])
    # df['c7'] = le.fit_transform(df['c7'])

    df.loc[df['label'] == "van", 'class'] = 1
    df.loc[df['label'] != "van", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./Vehicle.csv", index=False)


if __name__ == "__main__":
    main()
