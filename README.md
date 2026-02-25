# Market & Portfolio Analytics in Python

## Motivation
This project analyzes historical equity market data to study how market regimes and volatility impact
risk, returns, and the reliability of time-series forecasts.

## Data
- Daily price data for NIFTY 50 index and selected large-cap equities
- Time period: 2013–2025
- Source: Yahoo Finance (via yfinance)

## Methodology
- Data cleaning and return computation
- Exploratory data analysis (EDA)
- Risk and performance metrics
- Volatility-based regime analysis
- Time-series forecasting and evaluation

## Key Questions
- How do risk and return characteristics change across market regimes?
- Are forecasts equally reliable in high- and low-volatility environments?
- What metrics best describe downside risk during market stress?

## Limitations
- Yahoo Finance data quality constraints
- Simplified regime definitions
- No transaction costs or liquidity modeling

## Future Work
- GARCH-based volatility modeling
- Portfolio optimization under regime constraints
- Macro-factor integration
