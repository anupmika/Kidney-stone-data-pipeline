# 🏥 Kidney Stone Risk Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![SQL](https://img.shields.io/badge/Spark%20SQL-4479A1?style=for-the-badge&logo=apache&logoColor=white)

---

## 📌 Project Overview

An **End-to-End Data Engineering Pipeline** built using **PySpark** and **Databricks** to analyze kidney stone risk in patients based on urine composition data.

The pipeline follows the **Medallion Architecture** — ingesting raw medical data, cleaning and transforming it, and generating actionable health insights through a live interactive dashboard.

---

## 🏗️ Architecture

```
📂 kidney-stone-dataset.csv (Kaggle)
              │
              ▼
   ┌─────────────────────┐
   │    BRONZE LAYER     │
   │  Raw CSV → Delta    │
   │  Table (as-is)      │
   └──────────┬──────────┘
              │
              ▼
   ┌─────────────────────┐
   │    SILVER LAYER     │
   │  Cleaned + Renamed  │
   │  → Delta Table      │
   └──────────┬──────────┘
              │
              ▼
   ┌─────────────────────┐
   │     GOLD LAYER      │
   │  Analytics + Spark  │
   │  SQL → Delta Table  │
   └──────────┬──────────┘
              │
              ▼
   ┌─────────────────────┐
   │     DASHBOARD       │
   │  5 Interactive      │
   │  Databricks Charts  │
   └─────────────────────┘
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Primary programming language |
| PySpark | Distributed data processing |
| Databricks | Cloud data engineering platform |
| Delta Lake | ACID-compliant data storage |
| Spark SQL | Data analytics and querying |
| Databricks Dashboard | Interactive data visualization |
| GitHub | Version control and project hosting |

---

## 📊 Dataset

| Property | Details |
|----------|---------|
| Source | Kaggle — Kidney Stone Dataset |
| Total Records | 90 patients |
| Total Features | 7 columns |
| Target Variable | stone_present (0 = No Stone, 1 = Stone) |
| Data Type | Urine composition measurements |

### Feature Description

| Original Column | Renamed Column | Description |
|----------------|----------------|-------------|
| gravity | urine_gravity | Urine specific gravity (density) |
| ph | urine_ph | Urine pH level |
| osmo | osmolarity | Urine concentration (mOsm/kg) |
| cond | conductivity | Electrical conductivity of urine |
| urea | urea_level | Urea concentration in urine |
| calc | calcium_level | Calcium concentration in urine |
| target | stone_present | 0 = No Stone, 1 = Stone Present |

---

## 🔄 Pipeline Layers

### 🥉 Bronze Layer — Raw Data Ingestion
| Step | Action |
|------|--------|
| 1 | Verified CSV file path using dbutils.fs.ls() |
| 2 | Loaded raw CSV using PySpark with header and inferSchema |
| 3 | Displayed schema and row count |
| 4 | Saved raw data as-is to Delta Table: bronze_kidney_stone |

### 🥈 Silver Layer — Data Cleaning & Transformation
| Step | Action |
|------|--------|
| 1 | Read data from bronze_kidney_stone Delta Table |
| 2 | Dropped unnamed index column (_c0) |
| 3 | Verified zero null values across all 7 columns |
| 4 | Renamed all columns for better readability |
| 5 | Saved cleaned data to Delta Table: silver_kidney_stone |

### 🥇 Gold Layer — Analytics & Insights
| Step | Action |
|------|--------|
| 1 | Read data from silver_kidney_stone Delta Table |
| 2 | Performed groupBy aggregations using Spark SQL |
| 3 | Analyzed calcium, pH, osmolarity and urea by stone status |
| 4 | Saved final analytics to Delta Table: gold_kidney_stone |

---

## 📈 Key Insights Discovered

| Metric | No Stone (0) | Stone (1) | Medical Finding |
|--------|-------------|-----------|-----------------|
| Patient Count | 45 | 45 | Perfectly balanced dataset |
| Avg Calcium Level | 2.62 | 5.41 | Stone patients have 2x higher calcium |
| Avg pH Level | 6.10 | 5.97 | Stone patients have more acidic urine |
| Avg Osmolarity | 565.29 | 639.38 | Stone patients have more concentrated urine |
| Avg Urea Level | 237.11 | 279.29 | Stone patients have higher urea levels |

---

## 📊 Dashboard Visualizations

| Chart No. | Title | Chart Type | Key Finding |
|-----------|-------|------------|-------------|
| 1 | Stone vs No Stone Distribution | Pie Chart | 50-50 patient split |
| 2 | Average Calcium Level Comparison | Bar Chart | 2x higher in stone patients |
| 3 | Average pH Level Comparison | Bar Chart | More acidic in stone patients |
| 4 | Average Urea Level Comparison | Bar Chart | Higher urea in stone patients |
| 5 | Average Osmolarity Comparison | Bar Chart | More concentrated urine in stone patients |

---

## 📁 Project Structure

```
Kidney-stone-data-pipeline/
│
├── notebooks/
│   ├── 01_Bronze_Layer.py       ← Raw data ingestion
│   ├── 02_Silver_Layer.py       ← Data cleaning & transformation
│   └── 03_Gold_Layer.py         ← Analytics & insights
│
├── dataset/
│   └── kidney-stone-dataset.csv ← Source dataset from Kaggle
│
└── README.md                    ← Project documentation
```

---

## ▶️ How to Run

| Step | Action |
|------|--------|
| 1 | Sign up at Databricks Community Edition (free) |
| 2 | Upload kidney-stone-dataset.csv to Databricks Volume |
| 3 | Create notebook 01_Bronze_Layer and run |
| 4 | Create notebook 02_Silver_Layer and run |
| 5 | Create notebook 03_Gold_Layer and run |
| 6 | Create Databricks Dashboard using gold_kidney_stone table |

---

## 🏷️ Tags

`Data Engineering` `PySpark` `Databricks` `Delta Lake` `Python` `Medallion Architecture` `Healthcare Analytics` `Kidney Stone Analysis` `Spark SQL` `Resume Project`

---

## 👩‍💻 Author

**Anupmika**
GitHub: [@anupmika](https://github.com/anupmika)
