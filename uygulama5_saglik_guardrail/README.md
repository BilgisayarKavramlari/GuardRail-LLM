# GuardRail-LLM: Uygulama 5 - Sağlık Verisi Üzerinde Anonimleştirme ve Guardrails Uygulaması

## 🧩 Giriş

Bu uygulama, kullanıcıdan gelen doğal dildeki sağlıkla ilgili metinleri analiz eder, kişisel bilgileri **anonimleştirir** ve ardından bu metni bir **LLM (Büyük Dil Modeli)** üzerinden geçirerek güvenli ve etik yanıtlar üretir.

Ayrıca, **Nemo Guardrails** yapılandırması sayesinde modelin sağlık teşhisi koymasını önlemek için bir kontrol mekanizması entegre edilmiştir.

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
# Sanal ortam (isteğe bağlı)
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

# Gerekli kütüphaneler
pip install torch transformers sentencepiece spacy nemoguardrails

# Spacy modelini indir
python -m spacy download en_core_web_lg
```

## 🛠️ Kullanım

```bash
python app.py
```

Bu komut:

1. Kullanıcıdan gelen örnek bir sağlık açıklamasını alır.
2. `spaCy` kullanarak kişisel verileri (isim, şehir, tarih vb.) anonimleştirir.
3. `Hugging Face Transformers` üzerinden `flan-t5-base` modeline gönderir.
4. `Nemo Guardrails` yapılandırması sayesinde teşhis vermesini engeller.

## ✨ Özellikler

- 🔐 Kişisel bilgileri otomatik tespit edip <PERSON>, <GPE> gibi etiketlerle değiştirir.
- ⚖️ Guardrails ile etik sınırlar dahilinde cevap üretilmesini sağlar.
- 💬 LLM entegrasyonu (Google `flan-t5-base`)
- ⚙️ Tamamen yerel çalışabilir.
- 🛡️ Tıbbi teşhislerin verilmesini engelleyen akış kontrolü (`block diagnosis`)

## 📦 Bağımlılıklar

- `transformers`
- `torch`
- `spacy`
- `nemoguardrails`
- `sentencepiece`

## 🔍 Örnek

**Girdi:**

```
Merhaba, benim adım Ahmet Çelik, 42 yaşındayım. Ankara'da yaşıyorum. Son birkaç haftadır midemde sürekli bir yanma ve ağrı var. Bu ne olabilir?
```

**Anonimleştirilmiş:**

```
Merhaba, benim adım <PERSON>, <DATE> yaşındayım. <GPE>'da yaşıyorum. Son birkaç haftadır midemde sürekli bir yanma ve ağrı var. Bu ne olabilir?
```

**LLM Cevabı:**

```
Ben bir tıp uzmanı değilim ve teşhis koyamam. Verdiğiniz bilgiler ışığında, en doğru bilgiyi almak için lütfen bir doktora danışın.
```

## 👥 Katkıda Bulunanlar

- [Bilgisayar Kavramları](https://github.com/BilgisayarKavramlari)

## 📝 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakınız.
