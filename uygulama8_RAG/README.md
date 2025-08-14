# GuardRail-LLM: Uygulama 9 - RAG Senaryosu (Nihai Çalışan Versiyon)

## 🧩 Giriş

Bu uygulama, **Retrieval-Augmented Generation (RAG)** tekniğini kullanarak kullanıcıdan gelen soruları yerel bir bilgi tabanı üzerinden yanıtlayan bir yapay zeka senaryosudur. Aynı zamanda **Nemo Guardrails** kullanılarak bilgi tabanından gelen yanıtların güvenliği sağlanır.

Model olarak `flan-t5-base` kullanılmıştır. Zararlı içeriklerin (örneğin, "kesin teşhis", "garanti tedavi" gibi ifadeler) model çıktısına yansıması `Python aksiyonları` ile filtrelenir.

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

pip install torch transformers sentencepiece nemoguardrails
```

## 🛠️ Kullanım

```bash
python app.py
```

Bu komut sistemi başlatır ve test senaryolarını otomatik olarak çalıştırır. Bilgi tabanı içeriği Guardrails ile süzülerek sadece güvenli dokümanlar LLM'e iletilir.

## 🔍 Test Senaryoları

| Test | Soru | Beklenen Sonuç |
|------|------|----------------|
| Test 1 | Baş ağrısı nedenleri nelerdir? | Güvenli bilgi ile yanıt üretilmeli |
| Test 2 | Mide yanması hakkında bilgi verir misin? | Tehlikeli içerikler filtrelenmeli |

## ✨ Özellikler

- 📚 Yerel bilgi tabanı üzerinden RAG uygulaması
- 🛡️ Zararlı içerik filtreleme (`filter_rag_context` aksiyonu)
- 🔐 Guardrails ile güvenli cevap üretimi
- 💬 flan-t5-base LLM entegrasyonu
- ✅ Otomatik test süiti ile doğrulama

## 📦 Bağımlılıklar

- `transformers`
- `torch`
- `sentencepiece`
- `nemoguardrails`

## 👥 Katkıda Bulunanlar

- [Bilgisayar Kavramları](https://github.com/BilgisayarKavramlari)

## 📝 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.
