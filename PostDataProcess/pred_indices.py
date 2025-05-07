import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Récupérer les données de l'indice
ticker = "^GSPC"
data = yf.download(ticker, period="60d", interval="1d")  # 60 derniers jours pour plus de données
closing_prices = data["Close"]

# Visualiser les données
closing_prices.plot(figsize=(12, 6))
plt.title(f"Prix de clôture de l'indice {ticker}")
plt.show()

# ARIMA - prédiction
model = ARIMA(closing_prices, order=(5, 1, 0))  # Paramètres (p,d,q)
model_fit = model.fit()

# Faire une prédiction pour les 7 prochains jours
forecast = model_fit.forecast(steps=7)
print("Prédiction des 7 prochains jours : ", forecast)

# Afficher les prédictions
plt.plot(closing_prices.index, closing_prices, label="Historique")
plt.plot(pd.date_range(closing_prices.index[-1], periods=8, freq="D")[1:], forecast, label="Prédiction")
plt.legend()
plt.title(f"Prédiction des {ticker} pour les 7 prochains jours")
plt.show()