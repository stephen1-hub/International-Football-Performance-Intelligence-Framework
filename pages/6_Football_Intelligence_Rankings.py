import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🌍 Football Intelligence Rankings")

st.markdown("""
The Football Intelligence Index combines readiness,
attacking efficiency, defensive strength,
entertainment value, and playing intensity
into a single performance framework.
""")

# Load data
df = pd.read_csv(
    "data/international_football_dashboard.csv"
)

# Rankings
rankings = (
    df.sort_values(
        "football_intelligence_index",
        ascending=False
    )
)

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🏆 Most Complete Team",
        rankings.iloc[0]["team"]
    )

with col2:
    st.metric(
        "🥈 Runner-Up",
        rankings.iloc[1]["team"]
    )

with col3:
    st.metric(
        "🥉 Third Place",
        rankings.iloc[2]["team"]
    )

st.divider()

# Top 10 Rankings
st.subheader("Football Intelligence Rankings")

fig = px.bar(
    rankings.head(10),
    x="football_intelligence_index",
    y="team",
    orientation="h",
    text="football_intelligence_index",
    color="football_intelligence_index"
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Complete Teams Matrix
st.subheader("Complete Team Matrix")

fig2 = px.scatter(
    rankings,
    x="contender_score",
    y="football_intelligence_index",
    size="defensive_strength_score",
    color="attacking_efficiency",
    hover_name="team",
    title="Readiness vs Football Intelligence"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# Rankings Table
st.subheader("Top 15 Teams")

st.dataframe(
    rankings[
        [
            "team",
            "football_intelligence_index",
            "contender_score",
            "attacking_efficiency",
            "defensive_strength_score",
            "entertainment_score",
            "high_intensity_index"
        ]
    ].head(15),
    use_container_width=True
)

st.divider()

# Key Insights
st.subheader("Executive Insights")

st.success("""
Morocco emerged as the most complete team in the framework,
demonstrating strong performance across readiness,
attacking efficiency, defensive stability,
entertainment, and intensity.
""")
