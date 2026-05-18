import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/butun-nov-trvzin-istifadlri-dt_cd_020.csv')
df = df.sort_values('Year')

df['Export_Percentage'] = np.where(
    df['İstifadələrin cəmi (ton)'] > 0, 
    (df['İxrac (ton)'] / df['İstifadələrin cəmi (ton)']) * 100, 
    0
)
df['Loss_Percentage'] = np.where(
    df['İstifadələrin cəmi (ton)'] > 0,
    (df['İtkilər (ton)'] / df['İstifadələrin cəmi (ton)']) * 100,
    0
)

sns.set_theme(style="whitegrid")
fig, ax1 = plt.subplots(figsize=(14, 6))

sns.lineplot(data=df, x='Year', y='Əhalinin şəxsi istehlak fondu (ton)', marker='o', label='Personal Consumption (tons)', ax=ax1, color='blue')
sns.lineplot(data=df, x='Year', y='İxrac (ton)', marker='s', label='Export (tons)', ax=ax1, color='green')

ax1.set_title('Vegetable Usage Trends in Azerbaijan (2007 - 2024)', fontsize=16, fontweight='bold')
ax1.set_ylabel('Amount in Tons', fontsize=12)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_xticks(df['Year'].unique())
ax1.set_xticklabels(df['Year'].unique(), rotation=45)

ax2 = ax1.twinx()
sns.lineplot(data=df, x='Year', y='Export_Percentage', marker='^', linestyle='--', color='red', label='Export % of Total', ax=ax2)
ax2.set_ylabel('Export Percentage (%)', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')
ax1.get_legend().remove()

plt.tight_layout()
plt.savefig('vegetable_usage_fixed_ticks.png')
plt.close()

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

sns.lineplot(data=df, x='Year', y='tərəvəz konservləri istehsalına (ton)', marker='o', label='Canning', ax=axes[0, 0], color='teal')
sns.lineplot(data=df, x='Year', y='tərəvəz şirələrinin istehsalına (ton)', marker='s', label='Juice', ax=axes[0, 0], color='orange')
axes[0, 0].set_title('Vegetable Industrial Processing Trends', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Tons')
axes[0, 0].set_xticks(df['Year'].unique()[::2])
axes[0, 0].tick_params(axis='x', rotation=45)

sns.barplot(data=df, x='Year', y='Loss_Percentage', ax=axes[0, 1], palette='Reds_d')
axes[0, 1].set_title('Vegetable Supply Chain Losses (% of Total)', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Loss Percentage (%)')
axes[0, 1].set_xticks(range(len(df['Year'])))
axes[0, 1].set_xticklabels(df['Year'].unique(), rotation=45)

sns.lineplot(data=df, x='Year', y='Mal-qara və quş yemi üçün (ton)', marker='^', label='Livestock/Poultry Feed', ax=axes[1, 0], color='purple')
sns.lineplot(data=df, x='Year', y='Qida məhsullarının istehsalı üçün (ton)', marker='d', label='Food Product Mfg', ax=axes[1, 0], color='brown')
axes[1, 0].set_title('Feed Allocation vs. Food Manufacturing', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Tons')
axes[1, 0].set_xticks(df['Year'].unique()[::2])
axes[1, 0].tick_params(axis='x', rotation=45)

latest_year_data = df[df['Year'] == 2024].iloc[0]
categories = ['Seed', 'Feed', 'Food Mfg', 'Personal Cons.', 'Export', 'Losses']
volumes = [
    latest_year_data['Toxum üçün (ton)'],
    latest_year_data['Mal-qara və quş yemi üçün (ton)'],
    latest_year_data['Qida məhsullarının istehsalı üçün (ton)'],
    latest_year_data['Əhalinin şəxsi istehlak fondu (ton)'],
    latest_year_data['İxrac (ton)'],
    latest_year_data['İtkilər (ton)']
]

axes[1, 1].pie(volumes, labels=categories, autopct='%1.1f%%', startangle=140, pctdistance=0.85, colors=sns.color_palette('pastel', 6))
centre_circle = plt.Circle((0,0), 0.70, fc='white')
axes[1, 1].add_artist(centre_circle)
axes[1, 1].set_title("Where Did Azerbaijan's Vegetables Go in 2024?", fontsize=12, fontweight='bold')

plt.subplots_adjust(
    left=0.1,      
    right=0.9,     
    bottom=0.1,    
    top=0.9,      
    wspace=0.35,   
    hspace=0.35    
)

plt.suptitle('Vegetable Usage Trends Dashboard', fontsize=20, fontweight='bold', color='#006d77', y=0.98)
plt.savefig('vegetable_insights_dashboard.png', bbox_inches='tight')
plt.close()

research_cols = [
    'Əhalinin şəxsi istehlak fondu (ton)', 'İxrac (ton)', 'İtkilər (ton)',
    'tərəvəz konservləri istehsalına (ton)', 'tərəvəz şirələrinin istehsalına (ton)',
    'Mal-qara və quş yemi üçün (ton)'
]

english_labels = [
    'Personal Cons.', 'Exports', 'Losses', 
    'Canning Mfg', 'Juice Mfg', 'Livestock Feed'
]

correlation_matrix = df[research_cols].corr()
correlation_matrix.columns = english_labels
correlation_matrix.index = english_labels

plt.figure(figsize=(10, 8))
sns.set_theme(style="white")

mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

sns.heatmap(
    correlation_matrix, 
    mask=mask, 
    annot=True,             
    fmt=".2f",              
    cmap='coolwarm',        
    vmin=-1, vmax=1,        
    square=True,            
    linewidths=.5,          
    cbar_kws={"shrink": .8} 
)

plt.title('Heatmap: Variable Correlations', fontsize=16, fontweight='bold', pad=20, color='#006d77')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.savefig('correlation_heatmap.png', bbox_inches='tight')
plt.close()

X = df['Year'].values
y = df['Əhalinin şəxsi istehlak fondu (ton)'].values

linear_coeffs = np.polyfit(X, y, 1)
poly_coeffs = np.polyfit(X, y, 2)
log_y = np.log(y)
exp_coeffs = np.polyfit(X, log_y, 1)

future_timeline = np.arange(2007, 2031)

y_linear_pred = np.polyval(linear_coeffs, future_timeline)
y_poly_pred = np.polyval(poly_coeffs, future_timeline)
y_exp_pred = np.exp(np.polyval(exp_coeffs, future_timeline))

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(13, 6.5))

sns.scatterplot(x=X, y=y, color='#006d77', s=120, label='Actual Historical Data', ax=ax, zorder=5)
sns.lineplot(x=future_timeline, y=y_linear_pred, color='#8d99ae', linewidth=1.8, linestyle=':', label='Linear Baseline (Underestimation Bias)', ax=ax)
sns.lineplot(x=future_timeline, y=y_poly_pred, color='#d90429', linewidth=2.5, label='Polynomial Curve (Captures Acceleration)', ax=ax)
sns.lineplot(x=future_timeline, y=y_exp_pred, color='#ffb703', linewidth=2, linestyle='--', label='Exponential Growth Model (Compounding Growth)', ax=ax)

ax.axvspan(2024, 2030, color='#edf6f9', alpha=0.6, label='Forecast Window')
ax.set_title('Time Series Projections for Consumption', fontsize=16, fontweight='bold', pad=20, color='#1a2a3a')
ax.set_ylabel('Consumption Volume (Metric Tons)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_xticks(range(2007, 2031, 2))
ax.tick_params(axis='x', rotation=45)
ax.legend(loc='upper left', frameon=True)

plt.savefig('nonlinear_forecast.png', bbox_inches='tight')
plt.close()

X = df['Year'].values
y = df['İxrac (ton)'].values

linear_coeffs = np.polyfit(X, y, 1)
poly_coeffs = np.polyfit(X, y, 2)
log_y = np.log(np.where(y <= 0, 1, y))
exp_coeffs = np.polyfit(X, log_y, 1)

future_timeline = np.arange(2007, 2031)

y_linear_pred = np.polyval(linear_coeffs, future_timeline)
y_poly_pred = np.polyval(poly_coeffs, future_timeline)
y_exp_pred = np.exp(np.polyval(exp_coeffs, future_timeline))

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(13, 6.5))

sns.scatterplot(x=X, y=y, color='#1b4332', s=120, label='Actual Historical Exports', ax=ax, zorder=5)
sns.lineplot(x=future_timeline, y=y_linear_pred, color='#8d99ae', linewidth=1.8, linestyle=':', label='Linear Baseline (Constant Tonnage Growth)', ax=ax)
sns.lineplot(x=future_timeline, y=y_poly_pred, color='#d90429', linewidth=2.5, label='Polynomial Curve (Captures Changing Momentum)', ax=ax)
sns.lineplot(x=future_timeline, y=y_exp_pred, color='#ffb703', linewidth=2, linestyle='--', label='Exponential Growth Model (Compounding Rate)', ax=ax)

ax.axvspan(2024, 2030, color='#edf6f9', alpha=0.6, label='Forecast Horizon')
ax.set_title('Time Series Projections: Vegetable Export Dynamics', fontsize=16, fontweight='bold', pad=20, color='#1a2a3a')
ax.set_ylabel('Export Volume (Metric Tons)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_xticks(range(2007, 2031, 2))
ax.tick_params(axis='x', rotation=45)
ax.legend(loc='upper left', frameon=True)

plt.savefig('exports_nonlinear_forecast.png', bbox_inches='tight')
plt.close()
