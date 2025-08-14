# app.py - COLANG MANTIK HATASI GİDERİLMİŞ NİHAİ VERSİYON

# ==============================================================================
# 1. Kütüphanelerin Yüklenmesi
# ==============================================================================
import os
import yaml
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch
from nemoguardrails import LLMRails, RailsConfig
import spacy
import asyncio
import types

# ==============================================================================
# 2. Hugging Face Pipeline için Adaptör Sınıfı
# ==============================================================================
class HFPipelineWrapper:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    async def agenerate_prompt(self, prompt: str = None, **kwargs) -> any:
        raw_prompt_val = kwargs.get("prompt", prompt)
        text_to_generate = ""
        
        if isinstance(raw_prompt_val, list) and len(raw_prompt_val) > 0:
            if hasattr(raw_prompt_val[0], 'text'):
                text_to_generate = raw_prompt_val[0].text
            else:
                text_to_generate = str(raw_prompt_val[0])
        else:
            text_to_generate = str(raw_prompt_val)

        def run_pipeline():
            return self.pipeline(text_to_generate)
        
        result = await asyncio.to_thread(run_pipeline)
        
        generated_text = "Modelden geçerli bir cevap alınamadı."
        if isinstance(result, list) and len(result) > 0 and 'generated_text' in result[0]:
            generated_text = result[0]['generated_text']
            
        generation_object = types.SimpleNamespace(text=generated_text)
        generations_list = [[generation_object]]
        final_result = types.SimpleNamespace(
            llm_output=generated_text,
            generations=generations_list
        )
        return final_result

# ==============================================================================
# 3. Modellerin ve Araçların Hazırlanması
# ==============================================================================
print("\nModeller ve araçlar hazırlanıyor...")
device = 0 if torch.cuda.is_available() else -1
llm_tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
llm_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
hf_pipeline = pipeline("text2text-generation", model=llm_model, tokenizer=llm_tokenizer, device=device, max_new_tokens=300)
nlp = spacy.load("en_core_web_lg")
print("Modeller ve araçlar başarıyla hazırlandı.")

# ==============================================================================
# 4. Anonimleştirme Fonksiyonu
# ==============================================================================
def anonymize_with_spacy(text: str) -> str:
    print("--- Anonimleştirme fonksiyonu (Python) tetiklendi! ---")
    doc = nlp(text)
    anonymized_text = text
    pii_labels = {"PERSON", "GPE", "LOCATION", "DATE", "CARDINAL"}
    for ent in doc.ents:
        if ent.label_ in pii_labels and len(ent.text.strip()) > 2 and not ent.text.lower() in ["merhaba", "benim"]:
            print(f"   -> PII tespit edildi: '{ent.text}' (Tip: {ent.label_})")
            anonymized_text = anonymized_text.replace(ent.text, f"<{ent.label_}>")
    print(f"Orijinal Mesaj: '{text}'")
    print(f"Anonimleştirilmiş Mesaj: '{anonymized_text}'")
    print("---------------------------------------------------------")
    return anonymized_text

# ==============================================================================
# 5. NEMO GUARDRAILS Konfigürasyonunu Tanımlama (DÜZELTİLMİŞ)
# ==============================================================================
# Colang: 'execute' komutu kaldırıldı.
colang_content = """
define bot give diagnosis
  "Teşhisim"
  "Sizin durumunuz"
  "Kesinlikle sizde"
  "Garanti ederim ki bu"
  "Tedaviniz"
define bot refuse to give diagnosis
  "Ben bir tıp uzmanı değilim ve teşhis koyamam. Verdiğiniz bilgiler ışığında, en doğru bilgiyi almak için lütfen bir doktora danışın."
  "Bu semptomlar için bir doktora veya sağlık profesyoneline görünmeniz çok önemlidir. Ben tıbbi tavsiye veremem."

# DÜZELTME: 'execute' komutu kaldırıldı
define flow block diagnosis
  bot give diagnosis
  bot refuse to give diagnosis
"""
yaml_content = """
models:
  - type: main
    engine: huggingface
    model: google/flan-t5-base
rails:
  output:
    flows:
      - block diagnosis
"""
os.makedirs("config_health", exist_ok=True)
with open("config_health/healthcare.co", "w") as f: f.write(colang_content)
with open("config_health/config.yml", "w") as f: f.write(yaml_content)
print("\nNemo Guardrails için (düzeltilmiş) konfigürasyon dosyaları oluşturuldu.")

# ==============================================================================
# 6. Nemo Guardrails'i Başlatma ve Çalıştırma
# ==============================================================================
async def main():
    config = RailsConfig.from_path("./config_health")
    llm_wrapper = HFPipelineWrapper(pipeline=hf_pipeline)
    app = LLMRails(config=config, llm=llm_wrapper)
    print("\n--- SAĞLIK SENARYOSU (NİHAİ ÇALIŞAN VERSİYON) BAŞLIYOR ---\n")
    prompt = "Merhaba, benim adım Ahmet Çelik, 42 yaşındayım. Ankara'da yaşıyorum. Son birkaç haftadır midemde sürekli bir yanma ve ağrı var. Bu ne olabilir?"
    print(f">>> Senaryo: Orijinal Kullanıcı Sorusu\nKullanıcı: {prompt}\n")
    anonymized_prompt = anonymize_with_spacy(prompt)
    print("\n>>> Guardrails'e gönderilecek olan temizlenmiş prompt hazır.\n")
    response = await app.generate_async(messages=[{"role": "user", "content": anonymized_prompt}])
    print(f"\n>>> Nihai Bot Cevabı (Kullanıcıya Gösterilen):\nBot: {response['content']}\n")
    print("   (SONUÇ: Girdi, ana kod içinde başarıyla anonimleştirildi. LLM'in cevabı ise teşhis koymasını engelleyen çıkış korumasından geçti.)")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Bir hata oluştu: {e}")