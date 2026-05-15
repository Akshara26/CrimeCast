import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Config ---
st.set_page_config(page_title="CrimeCast", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("dataset.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Mean_Temp'] = (df['Maximum Temperature degrees (F)'] + df['Minimum Temperature degrees (F)']) / 2
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['Season'] = df['Month'].map({
        12:'Winter',1:'Winter',2:'Winter',
        3:'Spring',4:'Spring',5:'Spring',
        6:'Summer',7:'Summer',8:'Summer',
        9:'Fall',10:'Fall',11:'Fall'
    })
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.title("🔎 Filters")
years = st.sidebar.multiselect("Select Year(s)", sorted(df['Year'].unique()), default=sorted(df['Year'].unique()))
seasons = st.sidebar.multiselect("Select Season(s)", ['Winter','Spring','Summer','Fall'], default=['Winter','Spring','Summer','Fall'])

filtered_df = df[df['Year'].isin(years) & df['Season'].isin(seasons)]

# --- Title ---
st.title("🌡️ CrimeCast: Minneapolis Crime & Weather Analysis")
st.markdown("Exploring how temperature and weather conditions influence daily crime rates in Minneapolis (2019–2022)")

# --- KPI Row ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Crimes", f"{len(filtered_df):,}")
col2.metric("Avg Daily Crimes", f"{filtered_df.groupby('Date').size().mean():.0f}")
col3.metric("Avg Temperature (F)", f"{filtered_df['Mean_Temp'].mean():.1f}°")
col4.metric("Neighborhoods", f"{filtered_df['Neighborhood'].nunique()}")

st.markdown("---")

# --- Row 1: Crime vs Temp | Crime by Season ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Crime Count vs Temperature")
    daily = filtered_df.groupby('Date').agg(Crime_Count=('Offense_Category','count'), Mean_Temp=('Mean_Temp','mean')).reset_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=daily, x='Mean_Temp', y='Crime_Count', alpha=0.5, ax=ax)
    sns.regplot(data=daily, x='Mean_Temp', y='Crime_Count', scatter=False, color='red', ax=ax)
    ax.set_xlabel("Mean Temperature (F)")
    ax.set_ylabel("Daily Crime Count")
    st.pyplot(fig)

with col2:
    st.subheader("Crime by Season")
    season_counts = filtered_df['Season'].value_counts().reindex(['Winter','Spring','Summer','Fall'])
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=season_counts.index, y=season_counts.values, hue=season_counts.index, palette='coolwarm', legend=False, ax=ax)
    ax.set_xlabel("Season")
    ax.set_ylabel("Crime Count")
    st.pyplot(fig)

st.markdown("---")

# --- Row 2: Monthly Trend | Top Neighborhoods ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Monthly Crime Trend by Year")
    monthly = filtered_df.groupby(['Year','Month']).size().reset_index(name='Crime_Count')
    fig, ax = plt.subplots(figsize=(6, 4))
    for year in monthly['Year'].unique():
        data = monthly[monthly['Year']==year]
        ax.plot(data['Month'], data['Crime_Count'], marker='o', label=str(year))
    ax.set_xticks(range(1,13))
    ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], rotation=45)
    ax.legend(title='Year')
    ax.set_ylabel("Crime Count")
    st.pyplot(fig)

with col2:
    st.subheader("Top 10 Neighborhoods by Crime")
    top_n = filtered_df['Neighborhood'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=top_n.values, y=top_n.index, hue=top_n.index, palette='viridis', legend=False, ax=ax)
    ax.set_xlabel("Crime Count")
    st.pyplot(fig)

st.markdown("---")

# --- Row 3: Offense Category ---
st.subheader("Top 10 Offense Categories")
offense_counts = filtered_df['Offense_Category'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(12, 4))
sns.barplot(x=offense_counts.values, y=offense_counts.index, hue=offense_counts.index, palette='magma', legend=False, ax=ax)
ax.set_xlabel("Count")
st.pyplot(fig)

st.markdown("---")
st.caption("Data source: Minneapolis Open Data Portal & NOAA Climate Data | Built by Akshara")