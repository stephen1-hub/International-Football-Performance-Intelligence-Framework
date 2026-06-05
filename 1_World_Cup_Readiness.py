import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🏆 World Cup Readiness Index")

st.markdown("""
Identify the national teams most prepared for the 2026 FIFA World Cup
based on performance, dominance, attacking quality, and defensive stability.
""")

# Load data
df = pd.read_csv("international_football_dashboard.csv")

# Remove teams with no matches
df = df[df["matches_played"] > 0]

# Top contender table
top_contenders = (
    df.sort_values(
        "contender_score",
        ascending=False
    )
)

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🥇 Most Ready Team",
        top_contenders.iloc[0]["team"]
    )

with col2:
    st.metric(
        "⚽ Highest PPG",
        round(df["points_per_game"].max(), 2)
    )

with col3:
    st.metric(
        "🎯 Best Goal Difference",
        int(df["goal_difference"].max())
    )

st.divider()

# Top 10 leaderboard
st.subheader("Top 10 World Cup Contenders")

fig = px.bar(
    top_contenders.head(10),
    x="contender_score",
    y="team",
    orientation="h",
    text="contender_score"
)

fig.update_layout(
    yaxis={'categoryorder':'total ascending'}
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Readiness scatter
st.subheader("Readiness Matrix")

fig2 = px.scatter(
    df,
    x="goal_difference",
    y="points_per_game",
    size="expected_goals_for",
    color="contender_score",
    hover_name="team",
    title="Goal Difference vs Points Per Game"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# Rankings table
st.subheader("Full Rankings")

st.dataframe(
    top_contenders[
        [
            "team",
            "matches_played",
            "points_per_game",
            "goal_difference",
            "expected_goals_for",
            "clean_sheet_rate",
            "contender_score"
        ]
    ],
    use_container_width=True
)