# -----------------------------------------------------------------------------
# Türkçe Duygu Analizi + Açıklanabilirlik (transformers-interpret) - ÇALIŞAN SÜRÜM
# -----------------------------------------------------------------------------
# Gereksinimler:
#   pip install transformers torch transformers-interpret
# Not: GPU şart değil; CPU ile de çalışır.
# -----------------------------------------------------------------------------

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from transformers_interpret import SequenceClassificationExplainer

def main():
    print("Adım 1: Türkçe duygu analizi modeli yükleniyor...")
    # Seq2Seq (T5) yerine, sınıflandırma kafasıyla eğitilmiş BERT tabanlı model kullanın:
    model_name = "savasy/bert-base-turkish-sentiment-cased"

    # Model ve tokenizer'ı açıkça yükleyelim (pipeline içi de yükleyebilirdi, burada şeffaflık için ayrı)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Güvenli tarafta olmak için pad token kontrolü (BERT'te zaten vardır):
    if tokenizer.pad_token_id is None and tokenizer.eos_token_id is not None:
        # Çok nadir senaryolar için emniyet: pad token yoksa eos'u pad olarak ata
        tokenizer.pad_token = tokenizer.eos_token

    # Sentiment pipeline
    sentiment_classifier = pipeline(
        task="sentiment-analysis",
        model=model,
        tokenizer=tokenizer,
        device=-1,                  # CPU (GPU varsa 0 yapabilirsiniz)
        return_all_scores=False
    )

    # ARA ÇIKTI 1: Hızlı bir test
    test_text = "Bu film gerçekten harikaydı."
    prediction = sentiment_classifier(test_text)
    print(f"\nModel Testi -> Metin: '{test_text}'")
    print(f"Modelin Tahmini: {prediction}")

    # Adım 2: Açıklanacak metin
    text_to_explain = "Bu restorandaki yemekler harikaydı ve servis çok hızlıydı."
    print(f"\nAdım 2: Açıklanacak metin: '{text_to_explain}'")

    # Adım 3: Açıklayıcı (Explainer)
    print("\nAdım 3: Açıklayıcı (Explainer) nesnesi oluşturuluyor...")
    cls_explainer = SequenceClassificationExplainer(
        model=sentiment_classifier.model,
        tokenizer=sentiment_classifier.tokenizer
    )

    # Adım 4: Attribusyonları hesapla
    print("\nAdım 4: Metin için kelime etki skorları (attributions) hesaplanıyor...")
    word_attributions = cls_explainer(text_to_explain)  # varsayılan: modelin tahmin ettiği sınıf için açıklar

    print("\nHesaplanan Ham Etki Skorları (token, katkı):")
    # İlk 30 tokenı yazdırmak daha okunaklı:
    for tok, score in word_attributions[:30]:
        print(f"{tok:<20s}\t{score:+.4f}")

    predicted_label = cls_explainer.predicted_label_name
    print(f"\nAçıklayıcıya göre modelin nihai kararı: {predicted_label}")

    # Adım 5: Görselleştirme (HTML dosyası)
    print("\nAdım 5: Görselleştirme oluşturuluyor...")
    output_html = "sentiment_explanation.html"
    cls_explainer.visualize(output_html, true_label=predicted_label)
    print(f"\nAçıklama '{output_html}' dosyasına kaydedildi. Tarayıcıda açabilirsiniz.")

if __name__ == "__main__":
    main()
