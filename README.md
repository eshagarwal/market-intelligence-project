# 📊 Market Intelligence Project – Electric Vehicle Industry Analysis

## Overview

This project simulates a real-world **data analytics and market research workflow**.  
The goal was to collect, clean, and analyze data about electric vehicle manufacturers and models, and generate insights using Python and Excel.

The project demonstrates the complete data pipeline from **data collection → cleaning → analysis → reporting**.

## 🚀 Features

- Web scraping using Python
- Data cleaning with Pandas
- Dataset creation for company analysis
- Excel pivot tables and charts
- Market trend analysis
- Structured reporting

## 🛠 Technologies Used

- Python
- Pandas
- BeautifulSoup
- Excel
- CSV
- Git / GitHub

## 📥 Data Collection

Data was collected from Wikipedia using a Python web scraping script.

Script: [scripts/web_scraper.py](./scripts/web_scraper.py)

Output: [data/raw_companies.csv](./data/raw_companies.csv)

This step demonstrates:

- Automation
- Web data extraction
- Data collection

## 🧹 Data Cleaning

Raw data was processed using Pandas.

Tasks performed:

- Removed duplicates
- Handled missing values
- Standardized manufacturer names
- Prepared structured dataset

Script: [scripts/data_cleaning.py](./scripts/data_cleaning.py)

Output: [data/cleaned_companies.csv](./data/cleaned_companies.csv)

## 🏢 Company Intelligence Dataset

Data was grouped by manufacturer to create a company-level dataset.

Metrics created:

- Number of models per company
- Country distribution
- Industry classification

Output: [data/company_intelligence.csv](./data/company_intelligence.csv)

## 📈 Excel Analysis

The processed dataset was imported into Excel for further analysis using pivot tables and charts.

Analysis performed:

- Companies by country (geographic distribution)
- Number of models per company
- Top EV manufacturers by model count
- Summary statistics of the dataset

Excel file: [analysis/market_analysis.xlsx](./analysis/market_analysis.xlsx)

## 📊 Visualizations

Charts were created in Excel to present the analysis in a clear and report-style format.

Visualizations include:

- Bar chart – EV companies by country
- Horizontal bar chart – number of models per manufacturer
- Top manufacturers chart (Top 10 companies)
- Summary metrics for dataset overview

These visualizations simulate real-world business reporting and market analysis workflows.

## 📑 Report Summary

Key insights from the analysis:

- Japan, Germany, and the United States have the highest number of EV manufacturers in the dataset.
- Stellantis, General Motors, and Mercedes-Benz Group have the highest number of EV models.
- The dataset contains over 150 vehicle models across more than 60 manufacturers.
- Excel pivot tables were used to generate structured reports similar to real business analytics tasks.

## ▶ How to Run

Create virtual environment
```
python -m venv venv
source venv/bin/activate
```

Install dependencies
```
pip install pandas beautifulsoup4 requests
```

Run scraper
```
python scripts/web_scraper.py
```

Run cleaning
```
python scripts/data_cleaning.py
```

## ✅ Skills Demonstrated

- Data collection
- Web scraping
- Data cleaning
- Data analysis
- Excel pivot tables
- Data visualization
- Reporting
- Automation with Python

## 🔮 Future Improvements

- Add Power BI / Looker dashboard
- Add more data sources
- Automate report generation
- Build interactive dashboard