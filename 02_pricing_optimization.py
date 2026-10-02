import random
def talep_hesapla(fiyat: float) -> int:
    """Verilen fiyata göre tahmini satılacak adet (Talep)."""
    talep = 5000 - (4 * fiyat)
    # Talep 0'ın altına düşemez
    return max(0, int(talep))


def kar_hesapla(fiyat: float, maliyet: float) -> float:
    """Verilen fiyat ve maliyete göre toplam kâr."""
    adet = talep_hesapla(fiyat)
    birim_kar = fiyat - maliyet
    toplam_kar = birim_kar * adet
    return toplam_kar


# Ürün Parametreleri
maliyet = 200  # TL

en_iyi_fiyat = 0.0
maksimum_kar = -1.0
en_iyi_satis_adedi = 0

# Fiyatı 100 TL'den (maliyet) 250 TL'ye kadar 1'er TL artırarak test edelim
for f in range(int(maliyet), 451):
    fiyat = float(f)
    guncel_kar = kar_hesapla(fiyat, maliyet)
    guncel_talep = talep_hesapla(fiyat)

    if guncel_kar > maksimum_kar:
        maksimum_kar = guncel_kar
        en_iyi_fiyat = fiyat
        en_iyi_satis_adedi = guncel_talep

print(f"--- OPTİMİZASYON SONUCU ---")
print(f"Birim Maliyet    : {maliyet:.2f} TL")
print(f"Önerilen Fiyat   : {en_iyi_fiyat:.2f} TL")
print(f"Tahmini Satış    : {en_iyi_satis_adedi} Adet")
print(f"Maksimum Kâr     : {maksimum_kar:,.2f} TL")