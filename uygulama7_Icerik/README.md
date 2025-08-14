# GuardRail-LLM: Uygulama 7 - İçerik Üretimi ve Moderasyon Senaryosu

## 🧩 Giriş

Bu proje, büyük dil modelleri (LLM) ile içerik üretimi yapılırken, oluşturulan çıktının etik, güvenli ve doğruluk ilkelerine uygun olup olmadığını kontrol etmek için geliştirilmiştir. Moderasyon sisteminde üç aşamalı bir koruma uygulanır:

1. **Kendine zarar verme niyeti tespiti**
2. **Dezenformasyon kontrolü**
3. **Toksik içerik filtreleme (Python aksiyonu ile)**

LLM olarak `flan-t5-base`, toksisite sınıflandırıcısı olarak `unitary/toxic-bert`, kontrol sistemi olarak ise `Nemo Guardrails` kullanılmıştır.

## 📚 İçindekiler

- [Giriş](#-giriş)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Test Senaryoları](#-test-senaryoları)
- [Özellikler](#-özellikler)
- [Bağımlılıklar](#-bağımlılıklar)
- [Katkıda Bulunanlar](#-katkıda-bulunanlar)
- [Lisans](#-lisans)

## 🚀 Kurulum

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

pip install torch transformers sentencepiece spacy nemoguardrails
python -m spacy download en_core_web_lg
```

## 🛠️ Kullanım

```bash
python app.py
```

Bu komut sistemi başlatır ve aşağıdaki test senaryolarını otomatik olarak çalıştırır.

## 🔬 Test Senaryoları

| Test | Açıklama | Beklenen Sonuç |
|------|----------|----------------|
| Test 1 | Güvenli içerik üretimi | Koruma devreye girmemeli |
| Test 2 | Toksik içerik üretimi | Python aksiyonu ile engellenmeli |
| Test 3 | Dezenformasyon | Guardrails kuralları ile engellenmeli |
| Test 4 | Kendine zarar verme | Hemen yardım mesajı verilmeli |

## ✨ Özellikler

- 💬 İçerik üretimi için LLM (Flan-T5)
- 🧠 Python destekli aksiyon ile toksisite kontrolü
- 🛡️ Katmanlı Guardrails koruması (intihar, yanlış bilgi, saldırganlık)
- ⚙️ Otomatik test süiti
- ✅ Gerçek zamanlı çıktı moderasyonu

## 📦 Bağımlılıklar

- `transformers`
- `torch`
- `sentencepiece`
- `spacy`
- `nemoguardrails`
- `unitary/toxic-bert` (transformers üzerinden yüklenir)

## 👥 Katkıda Bulunanlar

- [Bilgisayar Kavramları](https://github.com/BilgisayarKavramlari)

## 📝 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.
