from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

# Örnek bir metin oluşturalım
# İçerisinde e-posta, telefon numarası ve kişi ismi bulunsun
text_to_anonymize = "Hello my name is John Doe and my phone number is 532 123 4677 and email is someone@turkcell.com.tr ."

print("--- Orijinal Metin ---")
print(text_to_anonymize)
print("-" * 25)

# 1. Adım: Hassas Veri Analizi (Analyzer)
# AnalyzerEngine'i İngilizce dil modeliyle başlatalım
analyzer = AnalyzerEngine()

# Metindeki hassas verileri (PII) bulalım
analyzer_results = analyzer.analyze(text=text_to_anonymize, language='en')

print("--- Bulunan Hassas Veriler (PII) ---")
if analyzer_results:
    for result in analyzer_results:
        print(f"Tip: {result.entity_type}, Metin: '{text_to_anonymize[result.start:result.end]}'")
else:
    print("Metinde hassas veri bulunamadı.")
print("-" * 25)

# 2. Adım: Verileri Anonimleştirme (Anonymizer)
# AnonymizerEngine'i başlatalım
anonymizer = AnonymizerEngine()

# Anonimleştirme işlemini gerçekleştirelim
# Farklı veri tipleri için farklı anonimleştirme yöntemleri belirleyebiliriz.
# Örneğin:
# - E-postaları <E-POSTA> ile değiştirelim.
# - Telefon numaralarını <TELEFON> ile değiştirelim.
# - Kişi isimlerini ise her biri için rastgele bir takma adla (faker) değiştirelim.
anonymized_result = anonymizer.anonymize(
    text=text_to_anonymize,
    analyzer_results=analyzer_results,
    operators={
        "EMAIL_ADDRESS": OperatorConfig("replace", {"new_value": "<E-POSTA>"}),
        "PHONE_NUMBER": OperatorConfig("replace", {"new_value": "<TELEFON>"}),
        "PERSON": OperatorConfig("replace", {"new_value": "<KİŞİ>"})
    }
)

print("--- Anonimleştirilmiş Metin ---")
print(anonymized_result.text)
print("-" * 25)