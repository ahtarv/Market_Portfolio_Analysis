#exploratory data analysis , this file tells us what this data does over time, what this data can do for us. 
#this script will load processed data, generate specific plots
#save them to reports/figures/
#as for the questions asked int his section, it is 
#how volatile returns over time
#do returns cluster
#how stable are correlations between assets
#are return distributions "normal"

import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

#now here we have the paths for the data
#using __file__ so paths work regardless of which directory you run the script from
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
FIGURES = PROJECT_ROOT / "reports" / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)


#oh yeah load data too

# prices.csv has a two-row header from yfinance ("Price" + asset names)
prices = pd.read_csv(DATA_RAW / "prices.csv", header=[0, 1], index_col=0, parse_dates=True)
prices.columns = prices.columns.get_level_values(1)   # keep only asset-name row
prices = prices.apply(pd.to_numeric, errors="coerce")

returns = pd.read_csv(DATA_PROCESSED / "returns.csv", index_col=0, parse_dates=True)
returns = returns.apply(pd.to_numeric, errors="coerce")

#now lets start with price evaluation
plt.figure(figsize=(10,5))
prices.plot(ax=plt.gca())
plt.title("Asset price evolution")
plt.ylabel("Price(Indexed)")
plt.tight_layout()
plt.savefig(FIGURES/ "price_evolution.png")
plt.close()

#now lets do rolling volitility

rolling_vol = returns.rolling(window=30).std()
#so what rolling volitality is that lets say i take a stock over a period of 20 days, we check how much that stock fluctuates
plt.figure(figsize=(10,5))
sns.heatmap(returns.corr(), annot = True, cmap = "coolwarm", fmt = ".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(FIGURES/ "correlation_heatmap.png")
plt.close()

#return distributions
plt.figure(figsize=(10,5))
returns.hist(bins=50, layout=(2,2))
plt.suptitle("Return Distributions", y=1.02)
plt.tight_layout()
plt.savefig(FIGURES/ "return_distributions.png")
plt.close()

