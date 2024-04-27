import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""
    imbalance ratio minority class : majority class = 20 : 341 (Total: 361)
    minority class: "label" == 6
    majority class: "label" == 1 or 2 or 3 or 4 or 5
    meta: 0-32: 1, 33: 0
"""


def main():
    header = ["erythema",
              "scaling",
              "definite borders",
              "itching",
              "koebner phenomenon",
              "polygonal papules",
              "follicular papules",
              "oral mucosal involvement",
              "knee and elbow involvement",
              "scalp involvement",
              "family history",
              "melanin incontinence",
              "eosinophils in the infiltrate",
              "PNL infiltrate",
              "fibrosis of the papillary dermis",
              "exocytosis",
              "acanthosis",
              "hypertrichosis",
              "parakeratosis",
              "clubbing of the rete ridges",
              "elongation of the rete ridges",
              "thinning of the suprapapillary epidermis",
              "spongiform pustule",
              "munro microabcess",
              "focal hypergranulosis",
              "disappearance of the granular layer",
              "vacuolisation and damage of basal layer",
              "spongiosis",
              "saw-tooth appearance of retes",
              "follicular horn plug",
              "perifollicular parakeratosis",
              "inflammatory monoluclear inflitrate",
              "band-like infiltrate",
              "Age",
              "label"]
    df = pd.read_csv("./dermatology.data", names=header, delimiter=',')
    print(df)
    print(df["label"].value_counts())
    df = df.drop(df[df.eq('?').any(axis=1)].index)
    print(df["label"].value_counts())

    df.loc[df['label'] == 6, 'class'] = 1
    df.loc[df['label'] == 1, 'class'] = 0
    df.loc[df['label'] == 2, 'class'] = 0
    df.loc[df['label'] == 3, 'class'] = 0
    df.loc[df['label'] == 4, 'class'] = 0
    df.loc[df['label'] == 5, 'class'] = 0
    print(df["class"].value_counts())
    df = df.drop(["label"], axis=1)
    df.to_csv("./derma.csv", index=False)


if __name__ == "__main__":
    main()
