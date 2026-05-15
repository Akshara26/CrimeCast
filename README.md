# 🌡️ CrimeCast: Predicting Crime from Weather in Minneapolis

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter) ![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql) ![R](https://img.shields.io/badge/R-Statistical%20Analysis-276DC3?logo=r) ![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn)

**Dataset Period:** 2019 – 2022  
**Location:** Minneapolis, Minnesota  

---

## 📌 Project Overview

CrimeCast investigates whether weather conditions, particularly temperature and snowfall, can predict daily crime rates in Minneapolis. Using real-world crime and weather datasets, this project combines data engineering, exploratory data analysis, statistical hypothesis testing, and machine learning to uncover patterns that matter.

> **Key Finding:** Temperature is the single strongest predictor of daily crime, accounting for over 60% of feature importance in a Random Forest model, and explaining 48% of variance in daily crime counts (R² = 0.484).


---

## 📊 Dataset

| Dataset | Source |
|---|---|
| Minneapolis Crime Data | Minneapolis Open Data Portal |
| Minneapolis Weather Data | NOAA Climate Data |

**Time Range:** 2019 – 2022 | **Final Dataset Size:** 1,460 daily records after merging

---

## 🧱 Project Pipeline

### 1. Data Preprocessing
- Removed irrelevant columns (24 → 10 features)
- Dropped null values and standardized date formats
- Replaced trace snowfall values (`"T"`) with `0.0`
- Engineered features: `Mean_Temperature_F`, `Month`, `Year`, `Season`, `Is_Weekend`, `Time_To_Report`
- Merged crime and weather datasets on `Date`

### 2. Exploratory Data Analysis
- Crime distribution by Neighborhood, Month, Season, and Offense Category
- Crime vs Temperature scatter plots with regression lines
- Monthly crime trends by year (2019–2022)
- Year-over-year crime growth analysis

### 3. Predictive Modeling
Trained two models to predict **daily crime count** from weather and calendar features:

| Model | R² Score | RMSE |
|---|---|---|
| Linear Regression | **0.484** | 23.90 |
| Random Forest | 0.404 | 25.69 |

**Features used:** Mean Temperature, Precipitation, Snowfall, Month, Day of Week, Is Weekend, Season

**Top Feature (Random Forest):** `Mean_Temp` with importance score of **0.61**

### 4. Statistical Hypothesis Testing (R)
- Model: `crime_count ~ Mean_Temperature_F` (Simple Linear Regression + ANOVA)
- **H₀:** Temperature has no effect on crime
- **H₁:** Temperature significantly affects crime
- **Result:** p-value < 0.05 → Reject null hypothesis ✅

---

## 📈 Key Findings

- **Temperature is the #1 predictor** of daily crime — by a large margin over all other features
- **Crime peaks in summer** (July–August) and drops sharply in winter across all 4 years
- **2020 saw the largest spike** in crime (+14.0% YoY), likely influenced by external social factors
- **Willard-Hay and Midtown Phillips** are consistently the highest-crime neighborhoods
- **Snowfall and precipitation** have minimal predictive power compared to temperature
- **Weekday vs weekend** patterns show minor but consistent differences in crime volume

---

## 🚀 Live Dashboard
👉 [View Interactive Dashboard](https://akshara26-crimecast.streamlit.app)

---

## 💻 Tech Stack

| Tool | Purpose |
|---|---|
| Python (Pandas, NumPy) | Data cleaning & feature engineering |
| Seaborn, Matplotlib | Data visualization |
| scikit-learn | Machine learning models |
| MySQL | Relational database design |
| R (lm, ANOVA) | Hypothesis testing |
| Jupyter Notebook | Analysis & presentation |

---

## 🗂️ Repository Structure

```
CrimeCast/
├── database project .ipynb       # Main analysis notebook
├── DB project hypothesis test.R  # R statistical analysis
├── dataset_csv                   # Merged crime + weather dataset
├── hypothesis_test_data          # Data used for R analysis
├── requirements.txt              # Python dependencies
└── README.md
```

---

## ⚙️ How to Run

```bash
# Clone the repository
git clone https://github.com/Akshara26/CrimeCast.git
cd CrimeCast

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Open notebook
jupyter notebook "database project .ipynb"
```

---

## 📎 References

- [Minneapolis Open Data Portal](https://opendata.minneapolismn.gov/)
- [NOAA Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/)
