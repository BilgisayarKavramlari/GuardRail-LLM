# GuardRail-LLM: Uygulama 3 - Anlamsal Nefret Söylemi Tespiti (Etkileşimli Sürüm)

## 🧩 Giriş

Bu uygulama, kullanıcının canlı olarak yazdığı metinleri analiz eder ve içerikte **nefret söylemi** olup olmadığını tespit eder. Tespit algoritması, metinleri yüzeysel anahtar kelimelerle değil, **anlamsal benzerlik** yoluyla değerlendirir.

Model olarak `paraphrase-multilingual-MiniLM-L12-v2` kullanılır; bu model Türkçe dahil birçok dili desteklemektedir.

## 📚 İçindekiler

- [Giriş](#-giriş)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Özellikler](#-özellikler)
- [Bağımlılıklar](#-bağımlılıklar)
- [Örnek](#-örnek)
- [Katkıda Bulunanlar](#-katkıda-bulunanlar)
- [Lisans](#-lisans)

## 🚀 Kurulum

```bash
# Sanal ortam oluşturma (isteğe bağlı)
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

# Gerekli kütüphaneleri yükleme
pip install sentence-transformers numpy
```

> İlk çalıştırmada model internetten indirilecektir. (yaklaşık 90 MB)

## 🛠️ Kullanım

Uygulama çalıştırıldığında komut satırında etkileşimli bir şekilde kullanıcı girdisi beklenir:

```bash
python app.py
```

Çıkmak için `exit`, `çıkış` veya `q` yazabilirsiniz.

## ✨ Özellikler

- 🧠 Anlamsal benzerlik ile nefret söylemi analizi
- 🌐 Çok dilli model (Türkçe desteği dahil)
- 🚫 Sakıncalı içerikler otomatik olarak maskelenir
- 🔍 Benzerlik skoru ve eşleşen ifade kullanıcıya bildirilir
- ⚡ Önceden hesaplanmış kütüphane embedding'leri ile hızlı işlem

## 📦 Bağımlılıklar

- [sentence-transformers](https://www.sbert.net/)
- [numpy](https://numpy.org/)

## 🔍 Örnek

**Girdi:**

```
Göçmenler ülkeden atılmalı.
```

**Çıktı:**

```
[UYARI] Girdi, 'göçmenler ülkeden atılmalı' ifadesiyle anlamsal olarak %98.21 oranında benzeşiyor.
Sonuç: [SAKINCALI İÇERİK TESPİT EDİLDİ VE MASKELENDİ]
Bu girdi işlenemez ve cevap üretimi engellenmiştir.
```

## 👥 Katkıda Bulunanlar

- [Bilgisayar Kavramları](https://github.com/BilgisayarKavramlari)

## 📝 Lisans

Bu proje MIT lisansı ile açık kaynak olarak sunulmuştur. Detaylar için `LICENSE` dosyasına bakabilirsiniz.
