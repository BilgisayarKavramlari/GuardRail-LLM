# GuardRail-LLM: Uygulama 2 - Gelişmiş Metin Anonimleştirici (Custom TCKN Destekli)

## 🧩 Giriş

Bu uygulama, Microsoft Presidio kütüphanesi kullanılarak hassas bilgileri otomatik olarak tespit eder ve gelişmiş anonimleştirme teknikleri uygular. Özellikle Türkiye Cumhuriyeti Kimlik Numarası (TCKN) için özel bir tanıyıcı (custom recognizer) tanımlanmıştır.

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
pip install presidio-analyzer presidio-anonymizer faker
```

## 🛠️ Kullanım

Python dosyasını çalıştırarak analiz ve anonimleştirme işlemini başlatabilirsiniz:

```bash
python app.py
```

Uygulama aşağıdaki adımları gerçekleştirir:

1. **TCKN için özel bir regex tanımlayıcı oluşturur.**
2. **Analyzer Engine'e özel tanıyıcıyı ekler.**
3. **Verilen metindeki tüm PII (kişisel bilgi) ögelerini analiz eder.**
4. **Belirli veri tipleri için gelişmiş anonimleştirme teknikleri uygular.**

## ✨ Özellikler

- 🆔 T.C. Kimlik No (TCKN) için özel tanıyıcı
- 🔐 Gelişmiş anonimleştirme:
  - Maskleme (`mask`)
  - Silme (`redact`)
  - Değiştirme (`replace`)
  - Hashleme (`hash`)
- 🤖 Faker kütüphanesi ile rastgele isim oluşturma
- 📊 Tüm analiz sonuçlarını skorlarıyla birlikte gösterme

## 📦 Bağımlılıklar

- [presidio-analyzer](https://pypi.org/project/presidio-analyzer/)
- [presidio-anonymizer](https://pypi.org/project/presidio-anonymizer/)
- [faker](https://pypi.org/project/Faker/)

## 🔍 Örnek

**Girdi Metni:**

```
Hastanın adı Ayşe Yılmaz (T.C. Kimlik No: 12345678910), telefon numarası +90 532 123 45 67'dir.
Kendisine a.yilmaz@email-provider.com adresinden ulaşılabilir.
Ödeme için kullanılan kredi kartı: 4545-1234-5678-9012.
Ayrıca, sistemdeki kullanıcı ID'si 'user-ayse-1985' olarak kayıtlıdır.
```

**Olası Çıktı:**

```
Hastanın adı Mehmet Demir (T.C. Kimlik No: f5a1d12c3e6f...), telefon numarası +90 532 1** ** **67'dir.
Kendisine <redacted> adresinden ulaşılabilir.
Ödeme için kullanılan kredi kartı: ****-****-****-9012.
Ayrıca, sistemdeki kullanıcı ID'si '<BİLGİ GİZLENDİ>' olarak kayıtlıdır.
```

## 👥 Katkıda Bulunanlar

- [Bilgisayar Kavramları](https://github.com/BilgisayarKavramlari)

## 📝 Lisans

Bu proje açık kaynaklıdır ve MIT lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.
