# 🌱 Cocoa Futures Analysis

## Project Overview
An advanced data analysis project that investigates the relationship between agroclimatological factors (particularly El Niño-Southern Oscillation) and cocoa futures market volatility. The project combines NASA POWER DAV Tool data with financial market data to predict cocoa price movements.

## 🎯 Key Features
- **Climate-Market Correlation Analysis**: Examines how weather patterns affect cocoa futures prices
- **NASA POWER DAV Integration**: Utilizes satellite-derived agroclimatological data
- **Price Spread Analysis**: Studies COCO Wisdom Tree and CCc1 spread dynamics
- **Interactive Visualizations**: Plotly-based charts for market trend analysis
- **Multi-Source Data Integration**: Combines climate, market, and agricultural data

## 📊 Data Sources
- **NASA POWER DAV Tool**: Agroclimatological measurements
  - Temperature metrics (T2M, T2M_MAX, T2M_MIN)
  - Soil conditions (TS, GWETPROF)
  - Precipitation data (PRECTOTCORR)
- **Market Data**
  - Daily cocoa futures prices
  - Trading volumes
  - Price spreads
- **Agricultural Data**
  - Cocoa production forecasts
  - Supply chain metrics

## 📈 Analysis Components
- `Cocoa_Spreads.ipynb`: Analysis of price spreads between contracts
- `NASA_Data.ipynb`: Processing and analysis of climate data
- `DataCheckpoint_Group142-FA24.ipynb`: Data processing and integration
- `EDACheckpoint_Group142-FA24.ipynb`: Exploratory data analysis
- `FinalProject_Group142-FA24.ipynb`: Comprehensive analysis and findings

## 🔍 Key Findings
- Correlation between El Niño patterns and market volatility
- Impact of temperature and rainfall on cocoa production
- Price spread behavior during climate events
- Supply chain disruptions related to weather patterns

## 📁 Repository Structure
- `Raw_DB/`: Raw market and climate data
- `NASA_DB/`: Processed NASA POWER DAV data
- `Merged_DB/`: Integrated datasets
- `Data_Analysis/`: Analysis scripts and notebooks
- `Contract_DB/`: Futures contract data
- `Images/`: Visualizations and charts

## 🛠️ Technologies Used
- Python
- Pandas & NumPy
- Plotly & Seaborn
- Refinitiv API
- NASA POWER DAV Tool

## 🔗 Dependencies
Required Python packages:
```bash
pandas
numpy
plotly
seaborn
matplotlib
refinitiv-data
```

## 👥 Contributors
- Jack Weston
- Spandan Das
- Seema Rida
- Louis Alejandro Soumah

## 📄 License
This project is available under the MIT License. 
