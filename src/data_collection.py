#so lets begin

import yfinance as yf
import pandas as pd
import numpy as np
from pathlib import Path
#so this is we importing everything we need

DATA_RAW = Path("data/raw") #us storing raw data
DATA_PROCESSED = Path("data/processed") #us storing processed data

DATA_RAW.mkdir(parents=True, exist_ok = True)
DATA_PROCESSED.mkdir(parents=True, exist_ok = True)
#here we are checking the folders

ASSETS = {
    "NIFTY50": "^NSEI",
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "HDFCBANK": "HDFCBANK.NS"
}

START_DATE = "2015-01-01"
END_DATE = "2026-02-24"

#this here we define the start date and the end date

#and here we have the functions

def fetch_prices(ticker: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(ticker,
        start = start,
        end = end,
        auto_adjust = True,
        progress=False
    )
    return df[["Close"]]
    #this is where we fetch prices

def compute_log_returns(price_df: pd.DataFrame) -> pd.DataFrame:
    return np.log(price_df/price_df.shift(1))
#here we compute the log using Data Frames

#next we have the pipeline

def main():
    price_frames = []

    for asset_name, ticker in ASSETS.items():
        df = fetch_prices(ticker, START_DATE, END_DATE)
        df.rename(columns = {"Close": asset_name}, inplace = True)
        price_frames.append(df)

    prices = pd.concat(price_frames, axis=1).dropna()
    returns = compute_log_returns(prices).dropna()

    prices.to_csv(DATA_RAW / "prices.csv")
    returns.to_csv(DATA_PROCESSED / "returns.csv")

    print("Data collection complete.")
    print(f"Saved {prices.shape[0]} rows of price data")
    print(f"Saved {returns.shape[0]} rows of returns data")

if __name__ == "__main__":
    main()
