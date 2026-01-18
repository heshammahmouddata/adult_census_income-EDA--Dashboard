import streamlit as st
import plotly.express as px
import pandas as pd

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Adult Income Dashboard",
    layout="wide"
)

# Load data

data = pd.read_csv("data_clean.csv")


# -----------------------------
# Sidebar

st.sidebar.title("Adult Census Income Dashboard")
st.sidebar.image("census.jpg", use_container_width=True)

st.sidebar.markdown("### Overview")
st.sidebar.write(
    "This dashboard analyzes key demographic and employment factors "
    "that influence whether income exceeds $50K per year."
)

st.sidebar.markdown("---")


# Filters

st.sidebar.markdown("### Filters")

sex_filter = st.sidebar.selectbox(
    "Sex",
    options=["All"] + sorted(data["sex"].unique())
)

education_filter = st.sidebar.selectbox(
    "Education",
    options=["All"] + sorted(data["education"].unique())
)

workclass_filter = st.sidebar.selectbox(
    "Workclass",
    options=["All"] + sorted(data["workclass"].unique())
)

# Apply filters
filtered_data = data.copy()

if sex_filter != "All":
    filtered_data = filtered_data[filtered_data["sex"] == sex_filter]

if education_filter != "All":
    filtered_data = filtered_data[filtered_data["education"] == education_filter]

if workclass_filter != "All":
    filtered_data = filtered_data[filtered_data["workclass"] == workclass_filter]

st.sidebar.markdown("---")
st.sidebar.markdown(
    "Made by [Hesham Mahmoud](https://www.linkedin.com/in/hesham-mahmoud-ml/)"
)


# Main Title

st.title("Adult Income Analysis Dashboard")
st.write(f"Dataset size after filtering: **{filtered_data.shape[0]} rows**")

# -----------------------------
# Chart 1: Income Distribution (Pie)

fig_income = px.pie(
    filtered_data,
    names="income",
    title="Income Distribution"
)
st.plotly_chart(fig_income, use_container_width=True)

# -----------------------------
# Chart 2: Age & Hours vs Income (One chart)

fig_age_hours = px.scatter(
    filtered_data,
    x="age",
    y="hours.per.week",
    color="income",
    opacity=0.7,
    title="Age and Working Hours vs Income"
)
st.plotly_chart(fig_age_hours, use_container_width=True)

# -----------------------------
# Chart 3: Education vs Income
# -----------------------------
fig_edu = px.histogram(
    filtered_data,
    x="education",
    color="income",
    barmode="group",
    title="Education vs Income"
)
st.plotly_chart(fig_edu, use_container_width=True)

# -----------------------------
# Chart 4: Sex vs Income
# -----------------------------
fig_sex = px.histogram(
    filtered_data,
    x="sex",
    color="income",
    barmode="group",
    title="Sex vs Income"
)
st.plotly_chart(fig_sex, use_container_width=True)

# -----------------------------
# Chart 5: Workclass vs Income
# -----------------------------
fig_work = px.histogram(
    filtered_data,
    x="workclass",
    color="income",
    barmode="group",
    title="Workclass vs Income"
)
st.plotly_chart(fig_work, use_container_width=True)
