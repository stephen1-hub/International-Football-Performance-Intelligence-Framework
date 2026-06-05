import streamlit as st
import pandas as pd

import os
import streamlit as st

st.write("Current directory:")
st.write(os.getcwd())

st.write("Files in root:")
st.write(os.listdir("."))

if os.path.exists("pages"):
    st.success("Pages folder found")
    st.write(os.listdir("pages"))
else:
    st.error("Pages folder NOT found")

st.sidebar.success("Sidebar is working")

st.set_page_config(
    page_title="International Football Performance Intelligence Framework",
    page_icon="⚽",
    layout="wide"
)
import streamlit as st

st.write("Streamlit version:", st.__version__)

st.title("🌍 International Football Performance Intelligence Framework")

st.markdown("""
### Evaluating National Team Readiness, Playing Style and Performance Dynamics Ahead of the 2026 FIFA World Cup
""")

df = pd.read_csv(
    "international_football_dashboard.csv"
)

rankings = (
    df.sort_values(
        "football_intelligence_index",
        ascending=False
    )
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🏆 Most Complete",
        "Morocco"
    )

with col2:
    st.metric(
        "⚽ Best Attack",
        "Ivory Coast"
    )

with col3:
    st.metric(
        "🛡️ Best Defense",
        "Algeria"
    )

with col4:
    st.metric(
        "🎭 Entertainers",
        "Brazil"
    )

with col5:
    st.metric(
        "🔥 Highest Intensity",
        "Slovenia"
    )

import plotly.express as px

st.subheader("🌍 Football Intelligence Rankings")

fig = px.bar(
    rankings.head(10),
    x="football_intelligence_index",
    y="team",
    orientation="h",
    color="football_intelligence_index",
    text="football_intelligence_index"
)

fig.update_layout(
    yaxis={"categoryorder":"total ascending"}
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📊 Key Findings")

st.info("""
• Morocco emerged as the most complete team in the framework.

• Mexico ranked as the most tournament-ready nation.

• Algeria established the strongest defensive foundation.

• Brazil produced the most entertaining matches.

• Slovenia recorded the highest intensity playing style.
""")

st.subheader("⚙️ Framework Components")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    🏆 World Cup Readiness Index

    Evaluates:
    - PPG
    - Goal Difference
    - xGF
    - Clean Sheets
    """)

with col2:
    st.success("""
    🌍 Football Intelligence Index

    Combines:
    - Readiness
    - Attack
    - Defense
    - Entertainment
    - Intensity
    """)
