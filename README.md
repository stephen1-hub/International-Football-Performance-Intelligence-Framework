# ⚽ 2026 International Friendly Performance Intelligence Framework

## Overview

As teams prepare for the 2026 FIFA World Cup, international friendly matches provide valuable insights into tactical identity, attacking efficiency, defensive stability, and overall team readiness.

This project develops a Football Performance Intelligence Framework to evaluate national team performance beyond traditional metrics such as wins, losses, and goals scored.

Using 2026 international friendly match data, the framework answers five key performance questions through custom football intelligence metrics and interactive visualizations.

An interactive Streamlit dashboard was also developed to enable exploration of team performance across multiple dimensions.

---

## Project Objectives

The analysis seeks to answer:

1. Which teams have the strongest attacking structures?
2. Which teams are overperforming or underperforming expected goals (xG)?
3. Which teams possess the strongest defensive foundations?
4. Which teams profile as genuine contenders ahead of the World Cup?
5. During which match phases are teams most vulnerable defensively?

---

## Dashboard Features

The Streamlit dashboard includes:

* ⚔️ Attack Intelligence Rankings
* 🎯 Finishing Efficiency Analysis
* 🛡️ Defensive DNA Rankings
* 📊 Team Profile Segmentation
* ⏱️ Match Vulnerability Analysis
* 📈 Interactive Visualizations
* 📋 Downloadable Rankings and Tables

---

## Business Question 1: Which Teams Have the Strongest Attacks?

### Attack Intelligence Index (AII)

A custom attacking metric was developed using:

* Goals Scored per Match (40%)
* Shots on Target (25%)
* Expected Goals (xG) (20%)
* Possession (15%)

### Key Findings

Top attacking teams included:

1. Germany
2. Bulgaria
3. Brazil
4. Republic of Ireland
5. Morocco

These teams consistently generated high-quality chances while maintaining strong attacking efficiency.

---

## Business Question 2: Which Teams Are Overperforming or Underperforming xG?

### Finishing Efficiency

Finishing Efficiency was calculated as:

Goals Scored per Match ÷ Expected Goals (xG)

### Most Clinical Teams

* Ivory Coast
* Austria
* Belgium
* Brazil
* Bulgaria

### Most Underperforming Teams

* South Africa
* Japan
* Serbia
* Greece
* Spain

This analysis helps distinguish sustainable attacking quality from short-term finishing variance.

---

## Business Question 3: Which Teams Have the Strongest Defensive Foundations?

### Defensive DNA Index (DDI)

The Defensive DNA Index was developed using:

* Goals Conceded per Match (40%)
* Expected Goals Against (xGA) (30%)
* Clean Sheet Percentage (20%)
* Minutes per Goal Conceded (10%)

### Top Defensive Teams

* Australia
* Iceland
* Cape Verde Islands
* Colombia
* Ecuador

These teams demonstrated strong defensive resilience across multiple defensive indicators.

---

## Business Question 4: Which Teams Are Genuine Contenders?

Teams were segmented into four categories:

### 🏆 Contenders

* Germany
* Mexico
* Spain
* South Korea
* Canada
* Morocco

### ⚔️ Attack Specialists

* Brazil
* France
* Switzerland
* Senegal

### 🛡️ Defense Specialists

* Japan
* South Africa
* Norway
* Netherlands

### ⚖️ Balanced Teams

Teams demonstrating moderate attacking and defensive performance without clear specialization.

---

## Business Question 5: When Are Teams Most Vulnerable?

Goal concessions were analysed across match periods.

### Findings

| Match Period | Goals Conceded |
| ------------ | -------------- |
| 0–10         | 16             |
| 11–20        | 25             |
| 21–30        | 19             |
| 31–40        | 18             |
| 41–50        | 36             |
| 51–60        | 37             |
| 61–70        | 39             |
| 71–80        | 24             |
| 81–90        | 41             |

### Key Insight

The 81–90 minute period emerged as the most vulnerable phase, accounting for the highest number of goals conceded.

This highlights the importance of:

* Match management
* Tactical substitutions
* Squad depth
* Physical conditioning
* Concentration in closing stages

---

## Methodology

### Attack Intelligence Index

AII =

* 40% Goals per Match
* 25% Shots on Target
* 20% Expected Goals (xG)
* 15% Possession

### Defensive DNA Index

DDI =

* 40% Goals Conceded per Match
* 30% Expected Goals Against (xGA)
* 20% Clean Sheet Percentage
* 10% Minutes per Goal Conceded

### Finishing Efficiency

Goals per Match ÷ Expected Goals (xG)

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* Plotly
* Streamlit
* Jupyter Notebook
* GitHub

---

## Skills Demonstrated

* Football Analytics
* Sports Intelligence
* KPI Development
* Feature Engineering
* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Dashboard Development
* Performance Benchmarking
* Business Problem Solving

---

## Key Takeaways

The Football Performance Intelligence Framework demonstrates that team strength extends beyond match results.

By integrating attacking quality, defensive resilience, finishing efficiency, and vulnerability analysis, the framework provides a more complete assessment of international team performance ahead of the 2026 FIFA World Cup.

**Note:** Rankings reflect international friendly matches played in 2026 up to the date of analysis. Additional friendlies may influence team profiles and rankings before the FIFA World Cup begins.
