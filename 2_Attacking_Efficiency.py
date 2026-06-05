import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("⚽ Attacking Efficiency Analysis")

st.markdown("""
Identify teams that score more (or fewer) goals than their
underlying attacking process suggests.
""")

df = pd.read_csv(
    "international_football_dashboard.csv"
)

df = df[df["total_expected_goals"] > 0]

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    top_team = df.sort_values(
        "attacking_efficiency",
        ascending=False
    ).iloc[0]

    st.metric(
        "🔥 Most Clinical Team",
        top_team["team"]
    )

with col2:
    st.metric(
        "⚽ Highest Goals Scored",
        int(df["goals_for"].max())
    )

with col3:
    st.metric(
        "🎯 Highest xG",
        round(df["total_expected_goals"].max(), 2)
    )

st.divider()

# Scatter Plot
fig = px.scatter(
    df,
    x="total_expected_goals",
    y="goals_for",
    size="attacking_efficiency",
    color="attacking_efficiency",
    hover_name="team",
    title="Goals Scored vs Expected Goals"
)

# Reference line
max_val = max(
    df["total_expected_goals"].max(),
    df["goals_for"].max()
)

fig.add_shape(
    type="line",
    x0=0,
    y0=0,
    x1=max_val,
    y1=max_val
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Top Overperformers
st.subheader("Top 10 Attacking Overperformers")

top_attack = (
    df.sort_values(
        "attacking_efficiency",
        ascending=False
    )
    [["team",
      "goals_for",
      "total_expected_goals",
      "attacking_efficiency"]]
)

st.dataframe(
    top_attack.head(10),
    use_container_width=True
)