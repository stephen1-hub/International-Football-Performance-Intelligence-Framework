import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🎭 Entertainment Index")

st.markdown("""
Identify the teams most likely to produce exciting,
high-scoring matches.
""")

# Load data
df = pd.read_csv(
    "international_football_dashboard.csv"
)

# KPI Cards
col1, col2, col3 = st.columns(3)

top_team = (
    df.sort_values(
        "entertainment_score",
        ascending=False
    )
    .iloc[0]
)

with col1:
    st.metric(
        "🎭 Most Entertaining Team",
        top_team["team"]
    )

with col2:
    st.metric(
        "⚽ Highest Avg Goals",
        round(df["average_goals_per_match"].max(), 2)
    )

with col3:
    st.metric(
        "🔥 Highest BTTS %",
        f"{df['both_teams_to_score_rate'].max():.0f}%"
    )

st.divider()

# Top Entertainment Teams
st.subheader("Entertainment Rankings")

top_entertainment = (
    df.sort_values(
        "entertainment_score",
        ascending=False
    )
)

fig = px.bar(
    top_entertainment.head(10),
    x="entertainment_score",
    y="team",
    orientation="h",
    text="entertainment_score"
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Entertainment Map
st.subheader("Entertainment Map")

fig2 = px.scatter(
    df,
    x="both_teams_to_score_rate",
    y="average_goals_per_match",
    size="entertainment_score",
    color="entertainment_score",
    hover_name="team",
    title="BTTS vs Average Goals"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# Rankings Table
st.subheader("Entertainment Rankings Table")

st.dataframe(
    top_entertainment[
        [
            "team",
            "both_teams_to_score_rate",
            "average_goals_per_match",
            "entertainment_score"
        ]
    ],
    use_container_width=True
)
