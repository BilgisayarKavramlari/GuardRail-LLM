
# GuardRail-LLM: Uygulama TEST - Anonimleştirme + Guardrails + Test Süiti

## 🧩 Giriş

Bu proje, kullanıcı sağlık verilerini içeren doğal dil girdilerini:

1. **Anonimleştirir** (`spaCy` ile),
2. **LLM ile yanıtlar üretir** (`flan-t5-base` modeli üzerinden),
3. **Guardrails ile güvenlik denetiminden geçirir** (teşhis/tavsiye içeriğini engeller),
4. Ve **kapsamlı test senaryolarıyla otomatik olarak doğrular**.

Uygulama, hem giriş koruması (anonimleştirme), hem çıkış koruması (etik sınırlama), hem de güvenli geçiş senaryolarını kontrol eden örneklerle test edilmektedir.

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
# Sanal ortam (isteğe bağlı)
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

# Gerekli kütüphaneler
pip install torch transformers sentencepiece spacy nemoguardrails

# Spacy modeli indir
python -m spacy download en_core_web_lg
```

## 🛠️ Kullanım

```bash
python app.py
```

Bu komut tüm sistemi başlatır ve otomatik olarak kapsamlı test süitini çalıştırır. Her bir senaryoda:

- Girdi anonimleştirilir,
- LLM'e gönderilir,
- Guardrails kurallarına uygun çıkış değerlendirilir.

## 🔬 Test Senaryoları

Testler 4 kategoriye ayrılır:

1. **Giriş Koruması Testleri**: Kişisel bilgilerin doğru şekilde gizlendiğini kontrol eder.
2. **Çıkış Koruması Testleri**: Teşhis/tavsiye isteyen içeriklerin engellendiğini kontrol eder.
3. **Güvenli Geçiş Testleri**: Bilgilendirici içeriklerin serbest geçip geçmediğini doğrular.
4. **Sınır Durumlar (Edge Cases)**: Karmaşık/örtük ifadelerle sistemin doğru davranıp davranmadığını test eder.

Her test açıklamalı şekilde çıktı verir.

## ✨ Özellikler

- 🔐 Kişisel veri tespiti ve etik anonimleştirme
- 🛡️ Guardrails akışları ile teşhis engelleme
- ✅ Otomatik test süiti
- 💬 flan-t5-base modeli ile doğal dil yanıt üretimi
- 📦 Hugging Face, spaCy ve Nemo Guardrails uyumlu

## 📦 Bağımlılıklar

- `transformers`
- `torch`
- `spacy`
- `sentencepiece`
- `nemoguardrails`

## 👥 Katkıda Bulunanlar

- [Bilgisayar Kavramları](https://github.com/BilgisayarKavramlari)

## 📝 Lisans

Bu proje MIT lisansı ile yayınlanmıştır. Ayrıntılar için `LICENSE` dosyasına bakınız.
