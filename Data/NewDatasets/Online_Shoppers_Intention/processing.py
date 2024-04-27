import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 1908 : 10422 (Total: 12330)
    minority class: "Revenue" == True
    majority class: "Revenue" == False
    meta: 0-14: 0, 15-16: 1
"""


def main():
    # head = list()
    # for i in range(8):
    #     head.append(f"c{i}")
    # head.append("label")
    df = pd.read_csv("./online_shoppers_intention_o.csv", delimiter=',')
    print(df)
    print(df["Revenue"].value_counts())

    le = LabelEncoder()
    df['VisitorType'] = le.fit_transform(df['VisitorType'])
    df['Weekend'] = le.fit_transform(df['Weekend'])
    df['Month'] = le.fit_transform(df['Month'])
    # df['c2'] = le.fit_transform(df['c2'])
    # df['c4'] = le.fit_transform(df['c4'])
    # df['c5'] = le.fit_transform(df['c5'])
    # df['c6'] = le.fit_transform(df['c6'])
    # df['c7'] = le.fit_transform(df['c7'])

    df.loc[df['Revenue'] == True, 'class'] = 1
    df.loc[df['Revenue'] != True, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["Revenue"], axis=1)
    df.to_csv("./Online_Shoppers_Intention.csv", index=False)


if __name__ == "__main__":
    main()
