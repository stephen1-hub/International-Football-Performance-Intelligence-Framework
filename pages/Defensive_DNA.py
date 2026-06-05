import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🛡️ Defensive DNA Framework")

st.markdown("""
Identify the national teams with the strongest defensive foundations
heading into the 2026 FIFA World Cup.
""")

# Load data
df = pd.read_csv(
    "international_football_dashboard.csv"
)

# KPI Cards
col1, col2, col3 = st.columns(3)

best_defense = (
    df.sort_values(
        "defensive_strength_score",
        ascending=False
    )
    .iloc[0]
)

with col1:
    st.metric(
        "🛡️ Best Defense",
        best_defense["team"]
    )

with col2:
    st.metric(
        "🥅 Highest Clean Sheet %",
        f"{df['clean_sheet_rate'].max():.0f}%"
    )

with col3:
    st.metric(
        "🚫 Lowest Goals Against",
        int(df["goals_against"].min())
    )

st.divider()

# Defensive Rankings
st.subheader("Top Defensive Teams")

top_defenses = (
    df.sort_values(
        "defensive_strength_score",
        ascending=False
    )
)

fig = px.bar(
    top_defenses.head(10),
    x="defensive_strength_score",
    y="team",
    orientation="h",
    text="defensive_strength_score"
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Defensive Matrix
st.subheader("Defensive DNA Matrix")

fig2 = px.scatter(
    df,
    x="goals_against_per_match",
    y="clean_sheet_rate",
    size="goal_difference",
    color="defensive_strength_score",
    hover_name="team",
    title="Goals Against vs Clean Sheet Rate"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# Rankings Table
st.subheader("Defensive Rankings")

st.dataframe(
    top_defenses[
        [
            "team",
            "goals_against",
            "goals_against_per_match",
            "clean_sheet_rate",
            "goal_difference",
            "defensive_strength_score"
        ]
    ],
    use_container_width=True
)
