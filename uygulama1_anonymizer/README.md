# GuardRail-LLM: Uygulama 1 - Metin Anonimleştirici

## 🧩 Giriş

Bu uygulama, Microsoft tarafından geliştirilen **Presidio** kütüphanesini kullanarak verilen metinlerdeki hassas kişisel bilgileri (PII) otomatik olarak tespit eder ve belirlenen kurallar çerçevesinde anonimleştirir. Tipik kullanım senaryoları arasında e-posta adresleri, telefon numaraları ve kişi isimleri gibi bilgiler yer almaktadır.

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

# Gerekli paketlerin yüklenmesi
pip install presidio-analyzer presidio-anonymizer
```

## 🛠️ Kullanım

Python dosyasını doğrudan çalıştırabilirsiniz:

```bash
python app.py
```

Uygulama şu adımları izler:

1. Verilen metin içindeki hassas bilgileri (isim, e-posta, telefon) tespit eder.
2. Her bir veri türü için özel anonimleştirme kuralı uygular.
   - E-posta adresleri → `<E-POSTA>`
   - Telefon numaraları → `<TELEFON>`
   - Kişi isimleri → `<KİŞİ>`

## ✨ Özellikler

- 📌 Hassas veri analizi (PII detection)
- 🔐 Otomatik anonimleştirme
- ⚙️ Esnek anonimleştirme kuralları tanımlama
- 🗣️ Çoklu dil desteği (uygulama İngilizce dil modeli ile çalışmaktadır)

## 📦 Bağımlılıklar

- [presidio-analyzer](https://pypi.org/project/presidio-analyzer/)
- [presidio-anonymizer](https://pypi.org/project/presidio-anonymizer/)

> Not: Presidio, NLP tabanlı modellerle çalışır ve bazı veri türleri için model dosyalarını indirmenizi gerektirebilir.

## 🔍 Örnek

**Girdi Metni:**

```
Merhaba, benim adım John Doe. Bana yardim@ornek.com adresinden veya 555-123-4567 numaralı telefondan ulaşabilirsiniz.
```

**Çıktı:**

```
Merhaba, benim adım <KİŞİ>. Bana <E-POSTA> adresinden veya <TELEFON> numaralı telefondan ulaşabilirsiniz.
```

## 👥 Katkıda Bulunanlar

- [Bilgisayar Kavramları](https://github.com/BilgisayarKavramlari)

## 📝 Lisans

Bu proje açık kaynaklıdır ve MIT lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.
