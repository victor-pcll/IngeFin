import yfinance as yf
import sys
import json

def fetch_stock(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1d", interval="1m")
    last_price = hist['Close'].iloc[-1]
    return {
        "symbol": symbol,
        "last_price": last_price
    }

if __name__ == "__main__":
    symbol = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    data = fetch_stock(symbol)
    print(json.dumps(data))  # JSON pour que Rust puisse lire