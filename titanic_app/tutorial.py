import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / "data" / "titanic.csv")
####################################################
st.title("Mostafa Qora3a")
st.write("hello from titanic app")
st.radio("selecta number",[1,2,3])
checked=st.checkbox("doos 3lia ya3m")
with st.form("search"):
    name=st.text_input("namecontains",placeholder="e.g defense ministry")
    classes=st.multiselect("class",[1,2,3],default=[1,2,3])
    ages=st.slider("age",0,80,(0,80))
    submitted=st.form_submit_button("search")
if submitted :
    st.write (f"you searched for {name} in class {classes} and ages {ages}")    
    ###########################################################################



df = pd.read_csv(BASE_DIR / "data" / "titanic.csv")
df.columns = df.columns.str.lower()
df["class"] = df["pclass"].map({1: "First", 2: "Second", 3: "Third"})
df["survival"] = df["survived"].map({0: "Died", 1: "Survived"})
df["port"] = df["embarked"].map({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
df["family_size"] = df["sibsp"] + df["parch"] + 1
df["title"] = df["name"].str.extract(r",\s*([^\.]+)\.", expand=False)
df["age_group"] = pd.cut(df["age"], [0, 12, 18, 35, 60, 80],
                         labels=["child", "teen", "young adult", "adult", "senior"])

ORDERS = {"class": ["First", "Second", "Third"], "survival": ["Died", "Survived"],
          "age_group": ["child", "teen", "young adult", "adult", "senior"]}
COLORS = {"Died": "#D95D4A", "Survived": "#0F766E"}


st.title("Mostafa Qora3a")

#st.image("utils/titanic.jpg")
st.caption("wowowowoawa")

show_data=st.checkbox("3lia ya3m")
if show_data:
   st.dataframe(df,hide_index=True)


classes = st.multiselect("Select class", df["class"].unique(),default=df["class"].unique())
gender=st.radio("Select gender",["male","female"], horizontal=True)
data=df[(df["class"].isin(classes)) & (df["sex"]==gender)]


c1,c2=st.columns(2)
with c1 :
    fig = px.histogram(data, x="family_size", nbins=11, labels={"family_size": "Family size (incl. the passenger)"},
                   title="How big were the families on board?")
    fig.update_layout(bargap=0.1, yaxis_title="Passengers")
    st.plotly_chart(fig)

with c2 :
    outcome = data["survival"].value_counts().reset_index()

    fig2 = px.pie(outcome, names="survival", values="count", hole=0.5, color="survival",
             color_discrete_map=COLORS, title="Died vs survived")

    st.plotly_chart(fig2)