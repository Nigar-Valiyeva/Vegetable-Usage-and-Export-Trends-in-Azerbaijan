# Exploratory Data Analysis and Time Series Forecasting: Vegetable Supply Chain Dynamics in Azerbaijan

## Project Overview
This project provides a comprehensive data analysis and time-series forecasting of vegetable usage, supply chain distribution, and economic export dynamics in Azerbaijan from 2007 to 2024. By applying statistical correlation and forecasting models, this analysis aims to identify historical consumption patterns, manufacturing shifts, and future agricultural economic trajectories through 2029.

The data utilized in this project was sourced from the State Statistical Committee of the Republic of Azerbaijan via the national open data portal:
https://opendata.az/@dsk/uses-of-all-kinds-of-vegetables

## Key Insights & Findings:

Based on the multi-variable exploratory data analysis and predictive modeling, several key trends were identified:

**Domestic Consumption vs. Exports:** Personal consumption dominates the sector (accounting for 74.6% of total usage in 2024). Exports saw a dramatic surge between 2016 and 2017, jumping from ~5% to over 14% of the total usage share, before stabilizing.

**Industrial & Agricultural Shifts:** There was a massive spike in livestock/poultry feed allocation in 2021, mirroring a simultaneous drop in standard food manufacturing. Additionally, industrial processing saw a stark pivot in 2022, with juice manufacturing briefly eclipsing traditional canning.

**Supply Chain Inefficiencies:** Post-harvest losses have remained relatively static over the past decade, hovering consistently between 5% and 6%. Correlation heatmaps indicate that losses scale almost perfectly with personal consumption ($r = 0.95$) and livestock feed ($r = 0.90$).

**Future Projections (2025–2029):** 
1. Consumption: Polynomial curve models suggest a strong, accelerating upward trend in domestic consumption over the next five years.
 
2. Exports: While linear baselines show steady tonnage growth, exponential compounding models indicate a massive potential ceiling for export volume if current growth rates are maintained.

## Visualizations & Dashboards

**Macro Usage Trends**

This line graph illustrates the historical relationship between domestic consumption and international exports.

<img width="1384" height="584" alt="image" src="https://github.com/user-attachments/assets/a7c5f798-85f0-4c38-9362-5a33a0857350" />

**Sector Distribution Dashboard**
   
A comprehensive breakdown of where vegetables actually go, including industrial processing trends, supply chain loss percentages, feed allocation, and a 2024 distribution summary.

<img width="1398" height="1150" alt="image" src="https://github.com/user-attachments/assets/567837d0-8045-4cd7-99ab-0aa3910f66d5" />

**Variable Correlation Heatmap**

A statistical breakdown showing the relationships between manufacturing, losses, exports, and consumption.

<img width="885" height="783" alt="image" src="https://github.com/user-attachments/assets/d10f31bd-7da6-46b5-ab47-76e04eaa0412" />

**Time Series Projections (Consumption & Exports)**

Forecasting future volumes using Linear, Polynomial, and Exponential growth models.

<img width="1088" height="638" alt="image" src="https://github.com/user-attachments/assets/6f3d57e7-3df3-4839-8270-e101ed5938fb" />

<img width="1122" height="638" alt="image" src="https://github.com/user-attachments/assets/51ce266a-4990-4478-ab42-f6c4350f3108" />


## Tools & Methodology

Data Processing & Cleaning: Python (Pandas, NumPy)

Data Visualization: Matplotlib, Seaborn

Statistical Analysis: Pearson Correlation

Predictive Modeling: NumPy (Ordinary Least Squares regression for Linear Baseline, Polynomial Curve Acceleration, and Log-Linearized Exponential Growth Modeling).

