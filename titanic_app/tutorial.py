import streamlit as st
from utills.data import load
from utills.config import COLORS, ORDERS
from utills.figures import rasma, rasma_pie, rasma_bar

# must be the first Streamlit call
st.set_page_config(page_title="Titanic Explorer", page_icon="🚢", layout="wide")

df = load()

# ---------------------------------------------------------------- header
st.title("🚢 Titanic Explorer")
st.caption("Who was on board, and who survived? Use the filters in the sidebar to slice the data.")

# ---------------------------------------------------------------- sidebar filters
with st.sidebar:
    st.header("Filters")
    sel_classes = st.multiselect("Class", ORDERS["class"], default=ORDERS["class"], key="sb_class")
    sel_gender = st.radio("Gender", ["All", "male", "female"], horizontal=True, key="sb_gender")
    sel_ages = st.slider("Age", 0, 80, (0, 80), key="sb_age")
    show_unknown_age = st.checkbox("Include unknown age", value=True, key="sb_unknown_age")

data = df[df["class"].isin(sel_classes)]
if sel_gender != "All":
    data = data[data["sex"] == sel_gender]
age_ok = data["age"].between(*sel_ages)
if show_unknown_age:
    age_ok = age_ok | data["age"].isna()
data = data[age_ok]

with st.sidebar:
    st.divider()
    st.caption(f"Showing **{len(data):,}** of {len(df):,} passengers")

if data.empty:
    st.warning("No passengers match these filters. Try widening them in the sidebar.")
    st.stop()

# ---------------------------------------------------------------- KPI cards
overall_rate = df["survived"].mean()
rate = data["survived"].mean()

c1, c2, c3, c4 = st.columns(4)
with c1:
    with st.container(border=True):
        st.metric("Passengers", f"{len(data):,}")
with c2:
    with st.container(border=True):
        st.metric("Survival rate", f"{rate:.1%}",
                  delta=f"{(rate - overall_rate) * 100:+.1f} pts vs all")
with c3:
    with st.container(border=True):
        st.metric("Median age", f"{data['age'].median():.0f}")
with c4:
    with st.container(border=True):
        st.metric("Avg family size", f"{data['family_size'].mean():.1f}")

st.write("")

# ---------------------------------------------------------------- charts
tab1, tab2, tab3 = st.tabs(["📊 Overview", "👶 Survival by age", "🗂️ Data"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(rasma(data), width="stretch")
    with col2:
        st.plotly_chart(rasma_pie(data, COLORS), width="stretch")

with tab2:
    st.plotly_chart(rasma_bar(data, ORDERS), width="stretch")

with tab3:
    st.dataframe(data, hide_index=True, width="stretch")
    st.download_button("Download filtered data (CSV)", data.to_csv(index=False),
                       file_name="titanic_filtered.csv", mime="text/csv")

# ---------------------------------------------------------------- leftover tutorial widgets
with st.expander("Tutorial widgets (demo)"):
    st.radio("selecta number", [1, 2, 3], horizontal=True)
    st.checkbox("doos 3lia ya3m")
    with st.form("search"):
        name = st.text_input("namecontains", placeholder="e.g defense ministry")
        classes = st.multiselect("class", [1, 2, 3], default=[1, 2, 3])
        ages = st.slider("age", 0, 80, (0, 80))
        submitted = st.form_submit_button("search")
    if submitted:
        st.write(f"you searched for {name} in class {classes} and ages {ages}")
