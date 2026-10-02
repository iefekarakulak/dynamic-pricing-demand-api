# 📈 Dinamik Fiyatlandırma ve Talep Tahminleme API

Bu proje, perakende ve e-ticaret süreçlerinde **talep elastikiyeti** ve **fiyat optimizasyonunu** simüle eden makine öğrenmesi tabanlı uçtan uca bir veri bilimi mikroservisidir.

## 🚀 Projenin Amacı ve Yaklaşımı
* **Fiyat & Talep Analitiği:** Baz fiyat, rakip fiyatları ve indirim oranlarını analiz ederek optimum talebi ve kârı tahmin eder.
* **Makine Öğrenmesi:** `Scikit-Learn` ve `RandomForestRegressor` ile non-lineer talep modellemesi ve eğitimi yapılmıştır.
* **Canlı API:** Model sonuçlarını dış sistemlere sunmak için `FastAPI` tabanlı RESTful mimari kurgulanmıştır.

## 🛠️ Modüler Proje Mimarisi
* **`01_database.py`:** SQLite ilişkisel veri tabanı şeması ve ürün yönetim operasyonları.
* **`02_pricing_optimization.py`:** Kâr maksimizasyonu ve analitik optimum fiyat arama algoritması.
* **`03_data_and_model_training.py`:** Sentetik veri üretimi, özellik mühendisliği (Feature Engineering) ve model eğitimi.
* **`04_test_prediction.py`:** Eğitilmiş `.joblib` modeli üzerinden çıkarım (inference) ve senaryo testi.
* **`05_api_service.py`:** Canlı FastAPI tahmin (`/predict-demand`) ve ürün yönetimi (`/products`) uç noktaları.

## ⚙️ Kullanılan Teknolojiler
`Python` | `FastAPI` | `Scikit-learn` | `Pandas` | `NumPy` | `SQLite`
