import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).parent

def load():
    df = pd.read_csv(BASE_DIR  / "titanic.csv")
    df.columns = df.columns.str.lower()
    df["class"] = df["pclass"].map({1: "First", 2: "Second", 3: "Third"})
    df["survival"] = df["survived"].map({0: "Died", 1: "Survived"})
    df["port"] = df["embarked"].map({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
    df["family_size"] = df["sibsp"] + df["parch"] + 1
    df["title"] = df["name"].str.extract(r",\s*([^\.]+)\.", expand=False)
    df["age_group"] = pd.cut(df["age"], [0, 12, 18, 35, 60, 80],
                            labels=["child", "teen", "young adult", "adult", "senior"])
    return df