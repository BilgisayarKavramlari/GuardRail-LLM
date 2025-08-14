# Gerekli kütüphaneleri içe aktaralım
from transformers import pipeline
from transformers_interpret import SequenceClassificationExplainer

# -----------------------------------------------------------------------------
# 1. MODELİ YÜKLEME
# Hugging Face'den Türkçe duygu analizi için önceden eğitilmiş bir model yüklüyoruz.
# Bu model, verilen metni 'positive' veya 'negative' olarak sınıflandırır.
# -----------------------------------------------------------------------------
print("Adım 1: Türkçe duygu analizi modeli yükleniyor...")
model_name = "google/flan-t5-base"
sentiment_classifier = pipeline("sentiment-analysis", model=model_name)

# ARA ÇIKTI 1: Modelin doğru yüklenip yüklenmediğini kontrol edelim.
# Modelin ne işe yaradığını görmek için basit bir test yapalım.
test_text = "Bu film gerçekten harikaydı."
prediction = sentiment_classifier(test_text)
print(f"\nModel Testi -> Metin: '{test_text}'")
print(f"Modelin Tahmini: {prediction}")
# BEKLENEN ÇIKTI: [{'label': 'positive', 'score': ...}]

# -----------------------------------------------------------------------------
# 2. AÇIKLANACAK METNİ TANIMLAMA
# Şimdi modelin karar mekanizmasını inceleyeceğimiz asıl cümleyi tanımlayalım.
# -----------------------------------------------------------------------------
text_to_explain = "Bu restorandaki yemekler harikaydı ve servis çok hızlıydı."
print(f"\nAdım 2: Açıklanacak metin: '{text_to_explain}'")

# -----------------------------------------------------------------------------
# 3. AÇIKLAYICI (EXPLAINER) OLUŞTURMA
# transformers-interpret kütüphanesinden açıklayıcı nesnesini oluşturuyoruz.
# Bu nesne, modelin içindeki tokenizer ve model bilgisini alır.
# -----------------------------------------------------------------------------
print("\nAdım 3: Açıklayıcı (Explainer) nesnesi oluşturuluyor...")
cls_explainer = SequenceClassificationExplainer(
    sentiment_classifier.model,
    sentiment_classifier.tokenizer
)

# -----------------------------------------------------------------------------
# 4. AÇIKLAMA HESAPLAMASINI ÇALIŞTIRMA
# Açıklayıcıya metnimizi vererek her bir kelimenin modelin kararına
# olan etkisini (attribution score) hesaplatıyoruz.
# Bu skorlar, kelimelerin "pozitif" kararına ne kadar katkı sağladığını gösterir.
# -----------------------------------------------------------------------------
print("\nAdım 4: Metin için kelime etki skorları (attributions) hesaplanıyor...")
word_attributions = cls_explainer(text_to_explain)

# ARA ÇIKTI 2: Ham Etki Skorları
# Bu, her bir kelime (token) ve onun sayısal etki skorunu içeren bir listedir.
# Pozitif skorlar, kelimenin tahmin edilen sınıfa (bu örnekte 'positive') katkı yaptığını,
# negatif skorlar ise o sınıftan uzaklaştırdığını gösterir.
print("\nHesaplanan Ham Etki Skorları:")
print(word_attributions)
# BEKLENEN ÇIKTI: [('[CLS]', 0.0), ('Bu', -0.04), ('restoran', 0.1), ('##daki', 0.05),
# ('yemekler', 0.4), ('harikaydı', 1.2), ('ve', -0.1), ('servis', 0.3),
# ('çok', 0.5), ('hızlıydı', 0.9), ('[SEP]', 0.0)] (Sayılar yaklaşık değerlerdir)

# ARA ÇIKTI 3: Modelin bu metin için nihai kararı nedir?
predicted_label = cls_explainer.predicted_label_name
print(f"\nAçıklayıcıya göre modelin nihai kararı: {predicted_label.upper()}")
# BEKLENEN ÇIKTI: POSITIVE

# -----------------------------------------------------------------------------
# 5. GÖRSELLEŞTİRME
# En etkili kısım! Hesaplanan skorları metin üzerinde renklerle görselleştiriyoruz.
# Yeşil renk: Pozitif katkı (tahmini güçlendirir)
# Kırmızı renk: Negatif katkı (tahmini zayıflatır)
# Rengin tonu, katkının büyüklüğünü gösterir.
# -----------------------------------------------------------------------------
print("\nAdım 5: Görselleştirme oluşturuluyor...")
# Bu komut, Jupyter Notebook'ta çalıştırıldığında çıktıyı doğrudan hücrede gösterir.
# Eğer script olarak çalıştırıyorsanız, bir HTML dosyasına kaydedebilirsiniz.
cls_explainer.visualize("sentiment_explanation.html", true_label=predicted_label)
print("\nAçıklama 'sentiment_explanation.html' dosyasına kaydedildi. Bu dosyayı tarayıcıda açabilirsiniz.")