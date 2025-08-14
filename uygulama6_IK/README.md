
# GuardRail-LLM: Uygulama 6 - İK ve İşe Alımda Yanlılığı Önleme

## 🧩 Giriş

Bu proje, insan kaynakları (İK) süreçlerinde kullanılan özgeçmiş (CV) verilerini değerlendirirken:

1. **Kişisel bilgileri anonimleştirir,**
2. **Yapay zeka tarafından oluşturulan özetlerdeki önyargılı ifadeleri tespit eder ve engeller,**
3. **Tarafsız ve etik işe alım süreçlerini destekler.**

Model olarak `flan-t5-base` kullanılmakta, etik kurallar ise `Nemo Guardrails` ile yapılandırılmaktadır.

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

Uygulama, çeşitli CV senaryolarını test eden otomatik bir test süiti ile birlikte gelir. Her testte:

- Girişte kişisel bilgiler anonimleştirilir.
- LLM’e özeti yazması için prompt verilir.
- Çıkışta yanlılık denetimi uygulanır (Guardrails kurallarıyla).

## 🔬 Test Senaryoları

Uygulama şu 4 ana test kategorisini destekler:

1. **Giriş Koruması**: CV’deki isim, yaş, okul, konum gibi bilgiler gizlenir.
2. **Çıkış Koruması**: Yanlı ifadeler (`hırslı`, `yardımsever`, `duygusal` vs.) engellenir.
3. **Güvenli Geçiş**: Teknik odaklı, tarafsız CV’ler engellenmeden geçer.
4. **Kadın-Erkek Yanlılığı Testi**: Cinsiyete göre değişebilecek dil örüntüleri test edilir.

## ✨ Özellikler

- 🤖 LLM destekli CV özetleme
- 🔐 Girişte anonimleştirme (`spaCy`)
- 🛡️ Çıkışta etik denetim (`Nemo Guardrails`)
- ✅ Otomatik test süiti
- 📋 Tarafsız işe alım için dil denetimi

## 📦 Bağımlılıklar

- `transformers`
- `torch`
- `sentencepiece`
- `spacy`
- `nemoguardrails`

## 👥 Katkıda Bulunanlar

- [Bilgisayar Kavramları](https://github.com/BilgisayarKavramlari)

## 📝 Lisans

Bu proje MIT lisansı ile sunulmuştur. Ayrıntılar için `LICENSE` dosyasına bakınız.
