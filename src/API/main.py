from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)
CORS(app)

@app.route('/api/predict_SP500', endpoint='predict_SP500')
def predict_SP500():
    ticker = "^GSPC"
    data = yf.download(ticker, period="60d", interval="1d")

    # Vérification et conversion en Series
    closing_prices = data["Close"]
    if isinstance(closing_prices, pd.DataFrame):
        closing_prices = closing_prices.iloc[:, 0]

    model = ARIMA(closing_prices, order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=7)

    future_dates = pd.date_range(closing_prices.index[-1], periods=8, freq="D")[1:]

    return jsonify({
        "historical": closing_prices.tolist(),
        "historical_dates": [d.strftime("%Y-%m-%d") for d in closing_prices.index],
        "forecast": forecast.tolist(),
        "forecast_dates": [d.strftime("%Y-%m-%d") for d in future_dates]
    })

@app.route('/api/predict_CAC40', endpoint='predict_CAC40')
def predict_CAC40():
    try:
        ticker = "^FCHI"
        data = yf.download(ticker, period="60d", interval="1d")

        closing_prices = data["Close"]
        if isinstance(closing_prices, pd.DataFrame):
            closing_prices = closing_prices.iloc[:, 0]

        model = ARIMA(closing_prices, order=(5, 1, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=7)

        future_dates = pd.date_range(closing_prices.index[-1], periods=8, freq="D")[1:]

        return jsonify({
            "historical": closing_prices.tolist(),
            "historical_dates": [d.strftime("%Y-%m-%d") for d in closing_prices.index],
            "forecast": forecast.tolist(),
            "forecast_dates": [d.strftime("%Y-%m-%d") for d in future_dates]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/predict_DAX', endpoint='predict_DAX')
def predict_DAX():
    try:
        ticker = "^GDAXI"
        data = yf.download(ticker, period="60d", interval="1d")

        closing_prices = data["Close"]
        if isinstance(closing_prices, pd.DataFrame):
            closing_prices = closing_prices.iloc[:, 0]

        model = ARIMA(closing_prices, order=(5, 1, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=7)

        future_dates = pd.date_range(closing_prices.index[-1], periods=8, freq="D")[1:]

        return jsonify({
            "historical": closing_prices.tolist(),
            "historical_dates": [d.strftime("%Y-%m-%d") for d in closing_prices.index],
            "forecast": forecast.tolist(),
            "forecast_dates": [d.strftime("%Y-%m-%d") for d in future_dates]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/predict_NASDAQ', endpoint='predict_NASDAQ')
def predict_NASDAQ():
    try:
        ticker = "^IXIC"
        data = yf.download(ticker, period="60d", interval="1d")

        closing_prices = data["Close"]
        if isinstance(closing_prices, pd.DataFrame):
            closing_prices = closing_prices.iloc[:, 0]

        model = ARIMA(closing_prices, order=(5, 1, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=7)

        future_dates = pd.date_range(closing_prices.index[-1], periods=8, freq="D")[1:]

        return jsonify({
            "historical": closing_prices.tolist(),
            "historical_dates": [d.strftime("%Y-%m-%d") for d in closing_prices.index],
            "forecast": forecast.tolist(),
            "forecast_dates": [d.strftime("%Y-%m-%d") for d in future_dates]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/predict_NEKKEI', endpoint='predict_NEKKEI')
def predict_NEKKEI():
    try:
        ticker = "^N225"
        data = yf.download(ticker, period="60d", interval="1d")

        closing_prices = data["Close"]
        if isinstance(closing_prices, pd.DataFrame):
            closing_prices = closing_prices.iloc[:, 0]

        model = ARIMA(closing_prices, order=(5, 1, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=7)

        future_dates = pd.date_range(closing_prices.index[-1], periods=8, freq="D")[1:]

        return jsonify({
            "historical": closing_prices.tolist(),
            "historical_dates": [d.strftime("%Y-%m-%d") for d in closing_prices.index],
            "forecast": forecast.tolist(),
            "forecast_dates": [d.strftime("%Y-%m-%d") for d in future_dates]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/get_indices')
def get_indices():
    tickers = {
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "CAC 40": "^FCHI",
        "DAX": "^GDAXI",
        "NIKKEI": "^N225"
    }

    result = {}  # On n’utilise plus "indices": {}

    # Récupérer les dates depuis le premier ticker
    try:
        sample_data = yf.download("^GSPC", period="60d", interval="1d")
        result["dates"] = [str(date.date()) for date in sample_data.index]
    except Exception as e:
        result["dates"] = {"error": str(e)}

    for name, symbol in tickers.items():
        try:
            data = yf.download(symbol, period="60d", interval="1d")
            if 'Close' in data.columns:
                close = data['Close']
                if hasattr(close, "tolist"):
                    result[name] = close.tolist()
                else:
                    result[name] = close.squeeze().tolist()
            else:
                result[name] = {"error": "Close column not found"}
        except Exception as e:
            result[name] = {"error": str(e)}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)