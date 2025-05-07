# get_indices.py
import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import json
import pandas as pd
import sys

# Tickers des indices
tickers = {
    "^GSPC": "S&P 500",
    "^DJI": "Dow Jones",
    "^IXIC": "Nasdaq",
    "^FCHI": "CAC 40",
    "^GDAXI": "DAX",
}

# Période
end = datetime.datetime.today()
start = end - datetime.timedelta(days=30)

# Téléchargement
data = {}
plt.figure(figsize=(12, 6))

for ticker, name in tickers.items():
    index = yf.Ticker(ticker)
    hist = index.history(start=start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'))

    if hist.empty:
        continue

    # Trace le graphe
    plt.plot(hist.index, hist["Close"], label=name)

    # Stocke les données à envoyer à Rust
    data[name] = {
        "dates": hist.index.strftime('%Y-%m-%d').tolist(),
        "close": hist["Close"].round(2).tolist()
    }

# Envoie les données au format JSON en premier
print(json.dumps(data))

if "--no-plot" not in sys.argv:
    plt.title("Indices boursiers (30 derniers jours)")
    plt.xlabel("Date")
    plt.ylabel("Cours de clôture")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()