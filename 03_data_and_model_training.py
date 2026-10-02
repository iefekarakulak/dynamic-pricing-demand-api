import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

np.random.seed(42)
num_samples = 2000

our_prices = np.random.uniform(120, 220, num_samples)
competitor_prices = our_prices + np.random.normal(0, 15, num_samples)
competitor_prices = np.clip(competitor_prices, 100, 250)
is_weekend = np.random.choice([0, 1], size=num_samples, p=[5/7, 2/7])

noise = np.random.normal(0, 15, num_samples)
units_sold = 800 - (3.8 * our_prices) + (1.5 * competitor_prices) + (40 * is_weekend) + noise
units_sold = np.clip(units_sold, 0, None).round().astype(int)

df = pd.DataFrame({
    'our_price': np.round(our_prices, 2),
    'competitor_price': np.round(competitor_prices, 2),
    'is_weekend': is_weekend,
    'units_sold': units_sold
})
df.to_csv('sales_data.csv', index=False)
print("1. [VERİ] 'sales_data.csv' oluşturuldu.")

X = df[['our_price', 'competitor_price', 'is_weekend']]
y = df['units_sold']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"2. [MODEL] R² Skoru: {r2:.4f} | Hata Payı (RMSE): {rmse:.2f} Adet")

joblib.dump(model, 'demand_model.joblib')
print("3. [KAYIT] Model 'demand_model.joblib' olarak kaydedildi!\n")
