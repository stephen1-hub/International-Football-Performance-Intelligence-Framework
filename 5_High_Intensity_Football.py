import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🔥 High-Intensity Football Index")

st.markdown("""
Identify the teams that play the most aggressive,
high-tempo, and high-pressure football.
""")

# Load data
df = pd.read_csv(
    "international_football_dashboard.csv"
)

# KPI Cards
col1, col2, col3 = st.columns(3)

top_team = (
    df.sort_values(
        "high_intensity_index",
        ascending=False
    )
    .iloc[0]
)

with col1:
    st.metric(
        "🔥 Highest Intensity Team",
        top_team["team"]
    )

with col2:
    st.metric(
        "🚩 Most Corners",
        round(df["corners_per_match"].max(), 2)
    )

with col3:
    st.metric(
        "🟨 Most Bookings",
        round(df["bookings_per_match"].max(), 2)
    )

st.divider()

# High Intensity Rankings
st.subheader("High-Intensity Rankings")

top_intensity = (
    df.sort_values(
        "high_intensity_index",
        ascending=False
    )
)

fig = px.bar(
    top_intensity.head(10),
    x="high_intensity_index",
    y="team",
    orientation="h",
    text="high_intensity_index",
    color="high_intensity_index"
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Style Matrix
st.subheader("Football Style Matrix")

fig2 = px.scatter(
    df,
    x="corners_per_match",
    y="bookings_per_match",
    size="high_intensity_index",
    color="high_intensity_index",
    hover_name="team",
    title="Corners vs Bookings"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# Rankings Table
st.subheader("High-Intensity Rankings Table")

st.dataframe(
    top_intensity[
        [
            "team",
            "corners_per_match",
            "bookings_per_match",
            "goals_for",
            "high_intensity_index"
        ]
    ],
    use_container_width=True
)