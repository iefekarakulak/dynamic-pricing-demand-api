import joblib
import pandas as pd

# 1. Modeli ikili dosyadan belleğe çağırıyoruz
model = joblib.load('demand_model.joblib')

# 2. Modele bir senaryo soruyoruz:
# Fiyatımız: 160 TL, Rakip: 175 TL, Gün: Hafta Sonu (1)
girdi = pd.DataFrame([{
    'our_price': 160.0,
    'competitor_price': 175.0,
    'is_weekend': 1
}])

# 3. Model tahmini yapıyor
tahmin = model.predict(girdi)[0]

print(f"✅ Model Çalışıyor!")
print(f"Tahmin Edilen Satış: {tahmin:.1f} Adet")