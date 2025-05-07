from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

@app.route('/api/predict', methods=['GET'])
def predict():
    ticker = "^GSPC"
    data = yf.download(ticker, period="60d", interval="1d")
    closing_prices = data["Close"]

    model = ARIMA(closing_prices, order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=7)

    future_dates = pd.date_range(closing_prices.index[-1], periods=8, freq="D")[1:]

    return jsonify({
        "historical": closing_prices.tolist(),
        "historical_dates": [str(d.date()) for d in closing_prices.index],
        "forecast": forecast.tolist(),
        "forecast_dates": [str(d.date()) for d in future_dates],
    })

if __name__ == '__main__':
    app.run(debug=True)