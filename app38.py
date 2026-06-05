import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Football Performance Intelligence Framework",
    page_icon="⚽",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

def load_data():

    attack_df = pd.read_csv(
        "attack_intelligence_rankings.csv"
    )

    finishing_df = pd.read_csv(
        "finishing_efficiency.csv"
    )

    defense_df = pd.read_csv(
        "defensive_dna_rankings.csv"
    )

    profiles_df = pd.read_csv(
        "team_profiles.csv"
    )

    vulnerability_df = pd.read_csv(
        "team_vulnerability.csv"
    )

    phase_df = pd.read_csv(
        "match_phase_analysis.csv"
    )

    return (
        attack_df,
        finishing_df,
        defense_df,
        profiles_df,
        vulnerability_df,
        phase_df
    )

# =====================================================
# VALIDATION
# =====================================================

required_profile_cols = [
    "common_name",
    "Attack_Intelligence_Index",
    "Defensive_DNA_Index",
    "Team_Profile"
]

missing_cols = [
    col for col in required_profile_cols
    if col not in profiles_df.columns
]

if missing_cols:
    st.error(f"team_profiles.csv is missing columns: {missing_cols}")
    st.stop()

# =====================================================
# HEADER
# =====================================================

st.markdown("""
### International Friendly Match Analytics (2026)

This dashboard evaluates national team performance in international friendly matches played during 2026 leading up to the FIFA World Cup.

The analysis identifies:

• Teams with the strongest attacking structures

• Teams outperforming or underperforming expected goals (xG)

• Teams with the strongest defensive foundations

• Current contender profiles based on friendly match performance

• Match phases where teams are most vulnerable defensively

Note: Several nations may still play additional friendly matches before the FIFA World Cup. Therefore, rankings and team profiles should be viewed as a snapshot of performance based on matches played to date and may evolve as new matches are played.
""")

# =====================================================
# KPI SECTION
# =====================================================

best_attack_team = attack_df.iloc[0]["common_name"]
best_attack_score = attack_df.iloc[0]["Attack_Intelligence_Index"]

best_defense_team = defense_df.iloc[0]["common_name"]
best_defense_score = defense_df.iloc[0]["Defensive_DNA_Index"]

contenders = profiles_df[
    profiles_df["Team_Profile"] == "Contender"
].shape[0]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚔️ Best Attack",
        best_attack_team,
        f"{best_attack_score:.1f} AII"
    )

with col2:
    st.metric(
        "🛡️ Best Defense",
        best_defense_team,
        f"{best_defense_score:.1f} DDI"
    )

with col3:
    st.metric(
        "🏆 Contenders",
        contenders
    )

with col4:
    st.metric(
        "⏱️ Vulnerable Phase",
        "81–90 mins"
    )

st.markdown("---")

st.success(
    f"""
    Pre-World Cup Friendly Match Insights

    • {best_attack_team} produced the strongest attacking profile.

    • {best_defense_team} demonstrated the strongest defensive structure.

    • {contenders} teams achieved Contender status based on combined attacking and defensive metrics.

    • The 81–90 minute period emerged as the most vulnerable defensive phase across all friendly matches analysed.
    """
)
st.caption(
    "Rankings reflect international friendly matches played in 2026 up to the date of analysis and are subject to change as additional matches are played."
)

# =====================================================
# SIDEBAR
# =====================================================

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Attack Intelligence",
        "Finishing Efficiency",
        "Defensive DNA",
        "Team Profiles",
        "Match Vulnerability"
    ]
)

# =====================================================
# OVERVIEW
# =====================================================

if page == "Overview":

    st.header("Project Overview")

    st.info(
        """
        Dataset Scope

        • Competition: International Friendly Matches

        • Period: 2026 Pre-World Cup Preparation Matches

        • Objective: Evaluate attacking quality, finishing efficiency,
          defensive strength, contender profiles, and match-state vulnerability.

        • Rankings represent performance based on matches played to date
          and may change as additional friendlies are played.
        """
    )

    st.markdown("""
    ### Business Questions

    1. Which teams have the strongest attacks?
    2. Which teams are overperforming or underperforming xG?
    3. Which teams have the strongest defensive foundations?
    4. Which teams are contenders, attack specialists, or defense specialists?
    5. Which teams are most vulnerable during matches?

    ### Metrics Developed

    - Attack Intelligence Index
    - Finishing Efficiency
    - Defensive DNA Index
    - Team Profile Segmentation
    - Match Vulnerability Analysis
    """)
# =====================================================
# ATTACK INTELLIGENCE
# =====================================================

elif page == "Attack Intelligence":

    st.header("⚔️ Attack Intelligence Index")

    fig = px.bar(
        attack_df.head(20),
        x="Attack_Intelligence_Index",
        y="common_name",
        orientation="h",
        text="Attack_Intelligence_Index",
        title="Top 20 Attacking Teams"
    )

    fig.update_layout(height=700)

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        attack_df,
        use_container_width=True
    )

# =====================================================
# FINISHING EFFICIENCY
# =====================================================

elif page == "Finishing Efficiency":

    st.header("🎯 Finishing Efficiency")

    fig = px.scatter(
        finishing_df,
        x="xg_for_avg_overall",
        y="goals_scored_per_match",
        hover_name="common_name",
        size="matches_played",
        color="Finishing_Efficiency",
        title="Goals vs Expected Goals"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        finishing_df.sort_values(
            "Finishing_Efficiency",
            ascending=False
        ),
        use_container_width=True
    )

# =====================================================
# DEFENSIVE DNA
# =====================================================

elif page == "Defensive DNA":

    st.header("🛡️ Defensive DNA Index")

    fig = px.bar(
        defense_df.head(20),
        x="Defensive_DNA_Index",
        y="common_name",
        orientation="h",
        text="Defensive_DNA_Index",
        title="Top Defensive Teams"
    )

    fig.update_layout(height=700)

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        defense_df,
        use_container_width=True
    )

# =====================================================
# TEAM PROFILES
# =====================================================

elif page == "Team Profiles":

    st.header("📊 Team Profile Analysis")

    fig = px.scatter(
        profiles_df,
        x="Attack_Intelligence_Index",
        y="Defensive_DNA_Index",
        color="Team_Profile",
        hover_name="common_name",
        title="Attack vs Defense Team Profiles"
    )

    st.plotly_chart(fig, use_container_width=True)

    profile_counts = (
        profiles_df["Team_Profile"]
        .value_counts()
        .reset_index()
    )

    profile_counts.columns = ["Profile", "Teams"]

    fig2 = px.pie(
        profile_counts,
        names="Profile",
        values="Teams",
        title="Team Profile Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(
        profiles_df,
        use_container_width=True
    )

# =====================================================
# MATCH VULNERABILITY
# =====================================================

elif page == "Match Vulnerability":

    st.header("⏱️ Match Vulnerability Analysis")

    fig = px.bar(
        phase_df,
        x="Period",
        y="Goals_Conceded",
        text="Goals_Conceded",
        title="Goals Conceded by Match Period"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Late Game Vulnerability Rankings")

    st.dataframe(
        vulnerability_df.sort_values(
            "Late_Vulnerability_%",
            ascending=False
        ),
        use_container_width=True
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "2026 International Friendly Performance Intelligence Framework | Pre-FIFA World Cup Analytics Project"
)
