import pandas as pd

"""
    imbalance ratio minority class : majority class = 11208 : 34014 (Total: 45222)
    minority class: "label" == ">50k"
    majority class: "label" == "<=50K"
    meta: [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1]
"""


def main():
    header = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship",
              "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "label"]
    train_df = pd.read_csv("./adult_train.data", names=header, delimiter=', ')
    test_df = pd.read_csv("./adult_test.data", names=header, delimiter=', ')
    train_df_cleaned = train_df.drop(train_df[train_df.eq('?').any(axis=1)].index)
    test_df_cleaned = test_df.drop(test_df[test_df.eq('?').any(axis=1)].index)
    df = pd.concat([train_df_cleaned, test_df_cleaned])
    print(df)
    print(df["label"].value_counts())
    df.loc[df['label'] == ">50K", 'class'] = 1
    df.loc[df['label'] == ">50K.", 'class'] = 1
    df.loc[df['label'] == "<=50K", 'class'] = 0
    df.loc[df['label'] == "<=50K.", 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./adult.csv", index=False)


if __name__ == "__main__":
    main()
