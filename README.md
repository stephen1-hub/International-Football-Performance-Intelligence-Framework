# International Football Performance Intelligence Framework

## Project Overview

Football analysis often focuses on wins, losses, and goals scored. However, these metrics do not always explain why teams perform the way they do.

This project develops a Football Performance Intelligence Framework using international friendly match data from 2026. The objective is to identify attacking strengths, defensive foundations, finishing efficiency, team profiles, and match vulnerabilities across international teams.

The analysis answers five key business questions that coaches, analysts, federations, broadcasters, and scouting departments may find valuable.

---

## Business Questions

### 1. Which teams have the strongest attacks?

An Attack Intelligence Index (AII) was developed using:

* Goals Scored per Match
* Expected Goals (xG)
* Possession
* Shots on Target

#### Key Finding

Germany emerged as the strongest attacking team in the dataset, while Bulgaria and Brazil ranked among the most effective attacking sides.

---

### 2. Which teams are overperforming or underperforming their expected goals?

A Finishing Efficiency metric was developed:

Finishing Efficiency = Goals Scored per Match ÷ Expected Goals (xG)

#### Key Findings

**Most Clinical Teams**

* Ivory Coast
* Austria
* Belgium
* Brazil
* Bulgaria

**Most Underperforming Teams**

* South Africa
* Japan
* Serbia
* Greece
* Spain

These findings help distinguish sustainable attacking performance from short-term finishing variance.

---

### 3. Which teams have the strongest defensive foundations?

A Defensive DNA Index (DDI) was developed using:

* Goals Conceded per Match
* Expected Goals Against (xGA)
* Clean Sheet Percentage
* Minutes per Goal Conceded

#### Key Findings

Top defensive teams included:

* Australia
* Iceland
* Cape Verde Islands
* Colombia
* Ecuador

---

### 4. Which teams are balanced contenders, attack specialists, or defense specialists?

Teams were classified into four categories:

* Contenders
* Attack Specialists
* Defense Specialists
* Balanced Teams

#### Contenders

* Germany
* Mexico
* Spain
* South Korea
* Canada
* Morocco

#### Attack Specialists

* Brazil
* France
* Switzerland
* Senegal

#### Defense Specialists

* Japan
* South Africa
* Norway
* Netherlands

---

### 5. When are teams most vulnerable to conceding goals?

Goal concessions were analyzed across match periods.

#### Key Findings

The most dangerous period for teams was:

81–90 minutes → 41 goals conceded

Teams conceded more than twice as many goals after halftime compared to the opening 40 minutes.

This highlights the importance of:

* Match management
* Tactical adjustments
* Fitness
* Concentration

---

## Methodology

### Attack Intelligence Index

40% Goals per Match

25% Shots on Target

20% Expected Goals (xG)

15% Possession

---

### Defensive DNA Index

40% Goals Conceded per Match

30% Expected Goals Against (xGA)

20% Clean Sheet Percentage

10% Minutes per Goal Conceded

---

### Finishing Efficiency

Goals per Match ÷ Expected Goals (xG)

---

## Tools Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Jupyter Notebook
* Streamlit

---

## Key Skills Demonstrated

* Sports Analytics
* Feature Engineering
* KPI Development
* Business Question Framing
* Performance Benchmarking
* Data Visualization
* Football Intelligence Reporting

---

## Conclusion

The Football Performance Intelligence Framework provides a structured approach to evaluating international teams beyond traditional results.

The analysis reveals that team success is influenced by a combination of attacking quality, defensive stability, finishing efficiency, and match management.

By integrating these dimensions into a single analytical framework, stakeholders can gain deeper insights into team performance and identify strengths, weaknesses, and potential future trends.

