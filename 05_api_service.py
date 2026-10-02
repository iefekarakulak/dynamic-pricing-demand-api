import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import database

# 1. Veritabanını Başlat ve Modeli Yükle
database.init_db()
model = joblib.load('demand_model.joblib')

app = FastAPI(
    title="Dinamik Fiyatlandırma ve Talep Tahmin API",
    description="Matematiksel optimizasyon ve yapay zeka destekli fiyat motoru",
    version="1.0.0"
)

# 2. Pydantic Veri Şemaları
class ProductCreate(BaseModel):
    name: str
    base_cost: float

class DemandRequest(BaseModel):
    product_id: int
    target_price: float
    competitor_price: float
    is_weekend: int

# 3. API Endpoint'leri
@app.get("/")
def home():
    return {"mesaj": "Dinamik Fiyatlandırma API Aktif! Dokümantasyon için /docs adresine gidin."}

@app.post("/products", summary="Yeni Ürün Ekle")
def create_product(product: ProductCreate):
    new_id = database.add_product(product.name, product.base_cost)
    return {"id": new_id, "name": product.name, "base_cost": product.base_cost}

@app.post("/predict-demand", summary="Fiyata Göre Talep Tahmin Et")
def predict_demand(data: DemandRequest):
    product = database.get_product(data.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı")
    
    # Modeli çağırma
    input_df = pd.DataFrame([{
        'our_price': data.target_price,
        'competitor_price': data.competitor_price,
        'is_weekend': data.is_weekend
    }])
    
    tahmin_adet = float(model.predict(input_df)[0])
    birim_maliyet = product[2]
    birim_kar = data.target_price - birim_maliyet
    toplam_kar = birim_kar * tahmin_adet
    
    return {
        "urun_adi": product[1],
        "bizim_fiyat": data.target_price,
        "tahmini_satilan_adet": round(tahmin_adet, 1),
        "tahmini_toplam_kar": round(toplam_kar, 2)
    }

@app.get("/optimize-price/{product_id}", summary="Maksimum Kârı Veren Optimum Fiyatı Bul")
def optimize_price(product_id: int, competitor_price: float, is_weekend: int = 0):
    product = database.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı")
    
    maliyet = product[2]
    en_iyi_fiyat = maliyet
    maksimum_kar = -float('inf')
    en_iyi_talep = 0
    
    # Maliyetten başlayarak 250 TL'ye kadar 1'er TL artırarak tara
    for p in range(int(maliyet), 251):
        fiyat = float(p)
        input_df = pd.DataFrame([{
            'our_price': fiyat,
            'competitor_price': competitor_price,
            'is_weekend': is_weekend
        }])
        
        tahmini_talep = float(model.predict(input_df)[0])
        kar = (fiyat - maliyet) * tahmini_talep
        
        if kar > maksimum_kar:
            maksimum_kar = kar
            en_iyi_fiyat = fiyat
            en_iyi_talep = tahmini_talep
            
    return {
        "urun_adi": product[1],
        "birim_maliyet": maliyet,
        "rakip_fiyati": competitor_price,
        "optimum_fiyat": en_iyi_fiyat,
        "beklenen_satis_adedi": round(en_iyi_talep, 1),
        "maksimum_kar": round(maksimum_kar, 2)
    }