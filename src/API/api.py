from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

@app.route('/api/get_indices')
def get_indices():
    tickers = {
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "CAC 40": "^FCHI",
        "DAX": "^GDAXI",
        "NIKKEI": "^N225"
    }

    result = {}

    for name, symbol in tickers.items():
        try:
            data = yf.download(symbol, period="1mo", interval="1d")

            # Vérifie que 'Close' est bien une colonne
            close = data["Close"]
            if hasattr(close, "tolist"):
                result[name] = close.tolist()
            else:
                result[name] = close.squeeze().tolist()
        except Exception as e:
            result[name] = {"error": str(e)}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)