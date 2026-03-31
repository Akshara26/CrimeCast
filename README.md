# 🌡️ CrimeCast: Analyzing the Impact of Temperature on Crime in Minneapolis

CrimeCast is a data-driven project that explores the relationship between **weather (temperature, snowfall)** and **crime patterns** in Minneapolis using data engineering, SQL analytics, visualization, and statistical hypothesis testing.

---

## 🚀 Overview

This project investigates whether **temperature influences crime rates** by:

- Merging real-world crime and weather datasets
- Designing a relational database
- Performing exploratory data analysis (EDA)
- Running SQL queries to answer key questions
- Conducting statistical hypothesis testing

📌 Key Insight:
There exists a **statistically significant positive relationship** between temperature and crime rates.

---

## 📊 Datasets

- **Minneapolis Crime Dataset**
- **Minneapolis Temperature Dataset**

📅 Time Range:
- Focused analysis on **2019–2022**

---

## 🧱 Pipeline

### 1. Data Preprocessing

- Removed irrelevant columns (24 → 10 features)
- Dropped null values
- Converted date formats to standard format
- Handled anomalies:
  - Replaced `"T"` (trace snowfall) → `0.0`
- Engineered new features:
  - `Month`
  - `Year`
  - `Mean_Temperature_F`
  - `Time_To_Report (days)`

📌 Final dataset created by merging on **Date**

---

### 2. Database Design

- Designed ER model linking:
  - Crime data
  - Temperature data
- Implemented using **MySQL**

---

### 3. Exploratory Data Analysis (EDA)

Analyzed trends using Python and SQL:

- Crime distribution by:
  - Neighborhood
  - Month
  - Year
- Top crime categories
- Crime trends vs:
  - Temperature
  - Snowfall

---

### 4. Key Business Questions

- Total crimes between 2019–2022  
- Most common crime types  
- Crime distribution across neighborhoods  
- Monthly crime vs temperature trends  
- Year-over-year crime growth  
- Impact of snowfall on crime  

---

### 5. Statistical Analysis (Hypothesis Testing)

Performed **Simple Linear Regression (SLR)** and ANOVA in R:

- Model: crime_count ~ Mean_Temperature_F

- Hypotheses:
- H0: Temperature has no effect on crime
- H1: Temperature significantly affects crime

📌 Result:
- p-value < 0.05 → Reject null hypothesis  
- Temperature is **statistically significant**

✔️ Confirms correlation between temperature and crime  

---

## 📈 Results & Insights

- Crime increases with temperature  
- Seasonal patterns strongly influence crime rates  
- Certain neighborhoods consistently show higher crime  
- Snowfall shows weaker correlation compared to temperature  

---

## 🧠 Key Learnings

- End-to-end data pipeline (clean → merge → analyze)
- SQL for analytical querying
- Feature engineering for time-series data
- Hypothesis testing using regression + ANOVA
- Real-world data challenges (missing values, noisy data)

---

## ⚡ Challenges

- Data inconsistencies (formats, missing values)
- Handling cyclic/time-series behavior
- Feature engineering for meaningful analysis
- Interpreting statistical results correctly

---

## 🔮 Future Improvements

- Add machine learning models for prediction
- Incorporate additional features (income, demographics)
- Build dashboard (Tableau / Power BI / Streamlit)
- Real-time crime prediction system

---

## 💻 Tech Stack

- Python (Pandas, NumPy, Seaborn, Matplotlib)
- MySQL (Database + Queries)
- R (Hypothesis Testing)
- Jupyter Notebook

---

## 📁 Project Structure
├── database_project_.py # Data preprocessing + EDA
├── hypothesis_test.R # Regression + ANOVA analysis
├── final report.pdf # Research report
├── DB-PROJECT.pptx # Presentation
├── datasets/ # Raw datasets


---

## 📌 Sample Analysis

Example regression model:

- Crime Count vs Mean Temperature  
- Positive slope → higher temperature → higher crime  

📌 From statistical testing:
- Temperature is a **significant predictor of crime**  

---

## 🏁 Conclusion

This project demonstrates how combining **data engineering, SQL analytics, and statistical modeling** can uncover meaningful real-world insights.

Understanding environmental factors like temperature can help:
- Improve law enforcement resource allocation
- Predict crime patterns
- Support smarter city planning

---

## 📎 References

- Minneapolis Crime Data  
- Weather Data Sources  
- Statistical Methods (Regression, ANOVA)

---
