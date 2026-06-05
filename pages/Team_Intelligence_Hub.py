import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("🔍 Team Intelligence Hub")

st.markdown("""
Explore the complete football intelligence profile
of any national team.
""")

# Load data
df = pd.read_csv(
    "international_football_dashboard.csv"
)

# Team Selector
selected_team = st.selectbox(
    "Select Team",
    sorted(df["team"].unique())
)

team_data = (
    df[df["team"] == selected_team]
    .iloc[0]
)

# ==========================
# KPI Cards
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Football Intelligence",
        round(team_data["football_intelligence_index"], 3)
    )

with col2:
    st.metric(
        "Contender Score",
        round(team_data["contender_score"], 3)
    )

with col3:
    st.metric(
        "Attacking Efficiency",
        round(team_data["attacking_efficiency"], 2)
    )

st.divider()

# ==========================
# Radar Chart
# ==========================

st.subheader("Football Intelligence Profile")

categories = [
    "Readiness",
    "Attack",
    "Defense",
    "Entertainment",
    "Intensity"
]

values = [
    team_data["contender_score"],
    team_data["attacking_efficiency"],
    team_data["defensive_strength_score"],
    team_data["entertainment_score"],
    team_data["high_intensity_index"]
]

fig = go.Figure()

fig.add_trace(
    go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        name=selected_team
    )
)

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================
# Archetype Engine
# ==========================

st.subheader("Team Archetype")

scores = {
    "Attack": team_data["attacking_efficiency"],
    "Defense": team_data["defensive_strength_score"],
    "Entertainment": team_data["entertainment_score"],
    "Intensity": team_data["high_intensity_index"],
    "Readiness": team_data["contender_score"]
}

primary_strength = max(
    scores,
    key=scores.get
)

if primary_strength == "Attack":
    archetype = "⚽ Attacking Powerhouse"

elif primary_strength == "Defense":
    archetype = "🛡️ Defensive Specialist"

elif primary_strength == "Entertainment":
    archetype = "🎭 Entertainers"

elif primary_strength == "Intensity":
    archetype = "🔥 High-Intensity Pressers"

else:
    archetype = "🏆 Tournament Contender"

st.success(
    f"Primary Identity: {archetype}"
)

st.divider()

# ==========================
# Strengths & Weaknesses
# ==========================

st.subheader("Strengths & Weaknesses")

highest_metric = max(scores, key=scores.get)
lowest_metric = min(scores, key=scores.get)

col1, col2 = st.columns(2)

with col1:
    st.success(
        f"Greatest Strength: {highest_metric}"
    )

with col2:
    st.warning(
        f"Biggest Improvement Area: {lowest_metric}"
    )

st.divider()

# ==========================
# Team Summary
# ==========================

st.subheader("Performance Summary")

summary_df = pd.DataFrame({
    "Metric": [
        "Football Intelligence",
        "Readiness",
        "Attack",
        "Defense",
        "Entertainment",
        "Intensity"
    ],
    "Score": [
        team_data["football_intelligence_index"],
        team_data["contender_score"],
        team_data["attacking_efficiency"],
        team_data["defensive_strength_score"],
        team_data["entertainment_score"],
        team_data["high_intensity_index"]
    ]
})

st.dataframe(
    summary_df,
    use_container_width=True
)
