# 🏛️ NIRF Institutional Ranking Dashboard

A comprehensive **Streamlit dashboard** for analyzing and visualizing **NIRF (National Institutional Ranking Framework)** data of Indian institutions from **2017 to 2024**.

This interactive web application enables users to:
- Explore institutional ranking trends
- Predict scores using machine learning
- Discover deep insights from historical data
- Get personalized improvement suggestions for institutes

---

## 🚀 Key Features

### 📊 Data Explorer
- View and explore the merged dataset
- Column-wise insights and summaries
- Explore institute count and year-wise coverage

### 📈 Trends Analysis
- Score progression across years for selected institutes
- Bar chart of average key parameter scores (TLR, RPC, GO, OI, Perception)

### 🏆 Top Performers
- View top `N` ranked institutes by year
- Visualize top performers state-wise

### 🔍 Institute Search (2017–2024)
- Search and analyze a specific institute
- Year-wise score line chart with labels
- Average parameter scores bar chart

### 📊 Statistical Insights
- Correlation matrix (Pearson) and heatmap
- Covariance matrix
- Compare any two parameters with scatter plot
- Pearson correlation between selected parameters

### 🔮 Predict Score
- Linear Regression model trained on NIRF parameters
- Predict institute's score using sliders
- Model metrics: R² and MSE

### 📉 Institute Performance Insights
- Year-wise deep dive for any institute
- Identify weakest parameter each year
- Suggest targeted improvements based on parameter gaps

### 🎯 Smart Suggestions by Year
- Year-over-year parameter change analysis
- Auto-generated improvement suggestions for dropped scores

---

## 📂 Data Structure

Data is sourced from 8 CSV files (`Book1.csv` to `Book8.csv`), representing years:

| File Name   | Year |
|------------|------|
| Book1.csv  | 2024 |
| Book2.csv  | 2023 |
| Book3.csv  | 2022 |
| ...        | ...  |
| Book8.csv  | 2017 |

Each file includes:
- `Name`, `City`, `State`
- `Score`, `Rank`
- Parameters: `TLR`, `RPC`, `GO`, `OI`, `PERCEPTION`

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – Web interface
- **Pandas** – Data analysis
- **Seaborn**, **Matplotlib** – Visualizations
- **Scikit-learn** – ML (Regression)

---

## 💡 Future Enhancements

- Predict future **Rank** using ML classification models
- Geo-based visualizations (state-wise rankings)
- Streamlit Cloud or Render deployment
- Yearly report PDF export per institute

---


---

