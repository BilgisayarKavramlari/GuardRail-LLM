# app.py (Düzeltilmiş Hali)

import re
from faker import Faker
# Pattern sınıfını da buradan import ediyoruz
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, Pattern, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

fake = Faker('tr_TR')

# --- 1. Adım: Özel Tanıyıcı (Custom Recognizer) Oluşturma (DÜZELTİLDİ) ---

# Önce regex desenini bir 'Pattern' nesnesine atıyoruz
tckn_regex_pattern = Pattern(
    name="TCKN Pattern",
    regex=r"\b[1-9][0-9]{9}[02468]\b",
    score=0.9 # Tanıma skorunu belirliyoruz
)

# Şimdi PatternRecognizer'ı oluştururken 'patterns' argümanına bir liste içinde veriyoruz
tckn_recognizer = PatternRecognizer(
    supported_entity="TCKN",
    patterns=[tckn_regex_pattern], # 'regex=' yerine 'patterns=[...]' kullanıyoruz
    context=["TCKN", "kimlik no", "T.C. Kimlik"]
)


# --- 2. Adım: Analyzer Engine'i Yapılandırma ---
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
registry.add_recognizer(tckn_recognizer)

analyzer = AnalyzerEngine(
    registry=registry,
    supported_languages=["en"]
)

# --- 3. Adım: Anonimleştirilecek Metni Hazırlama ---
text_to_anonymize = """
Name of the patient is Ayşe Yılmaz (her T.C. Kimlik No: 12345678910), and phone number is +90 532 123 45 67.
You can access her through a.yilmaz@email-provider.com email address.
For the payment you can use the credit card: 4545-1234-5678-9012.
Also, the id of user is 'user-ayse-1985' from the records.
"""

print("--- Orijinal Metin ---")
print(text_to_anonymize)
print("-" * 30)

# --- 4. Adım: Metni Analiz Etme ---
analyzer_results = analyzer.analyze(text=text_to_anonymize, language="en")

print("--- Bulunan Hassas Veriler (PII) ---")
if analyzer_results:
    for result in analyzer_results:
        print(f"Tip: {result.entity_type}, Metin: '{text_to_anonymize[result.start:result.end]}', Skor: {result.score:.2f}")
else:
    print("Metinde hassas veri bulunamadı.")
print("-" * 30)

# --- 5. Adım: Gelişmiş Anonimleştirme Operatörlerini Tanımlama ---
anonymizer = AnonymizerEngine()

anonymized_result = anonymizer.anonymize(
    text=text_to_anonymize,
    analyzer_results=analyzer_results,
    operators={
        "DEFAULT": OperatorConfig("replace", {"new_value": "<BİLGİ GİZLENDİ>"}),
        "PERSON": OperatorConfig(
            "replace", {"new_value": fake.name()}
        ),
        "PHONE_NUMBER": OperatorConfig(
            "mask", {
                "type": "mask",
                "masking_char": "*",
                "chars_to_mask": 7,
                "from_end": True
            }
        ),
        "EMAIL_ADDRESS": OperatorConfig("redact"),
        "CREDIT_CARD_NUMBER": OperatorConfig(
            "mask", {
                "type": "mask",
                "masking_char": "*",
                "chars_to_mask": 12,
                "from_end": False
            }
        ),
        "TCKN": OperatorConfig(
            "hash", {"type": "hash"}
        )
    }
)

print("--- Gelişmiş Anonimleştirilmiş Metin ---")
print(anonymized_result.text)
print("-" * 30)