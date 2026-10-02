import joblib
import pandas as pd

model = joblib.load('demand_model.joblib')

girdi = pd.DataFrame([{
    'our_price': 160.0,
    'competitor_price': 175.0,
    'is_weekend': 1
}])

tahmin = model.predict(girdi)[0]

print(f"✅ Model Çalışıyor!")
print(f"Tahmin Edilen Satış: {tahmin:.1f} Adet")
