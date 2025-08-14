from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_community.llms import HuggingFacePipeline  # LangChain sarmalayıcı
from nemoguardrails import LLMRails, RailsConfig

# 1) HuggingFace/Transformers modelini yükleyin (küçük ve CPU-dostu bir sohbet modeli)
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("Model ve tokenizer indiriliyor/yükleniyor...")
tok = AutoTokenizer.from_pretrained(MODEL_NAME)
mdl = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto"  # CPU'da da çalışır; GPU varsa otomatik kullanır
)

# 2) HF pipeline oluşturun (chat tarzı kısa yanıtlar için basit ayarlar)
pipe = pipeline(
    task="text-generation",
    model=mdl,
    tokenizer=tok,
    max_new_tokens=128,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

# 3) LangChain LLM sarmalayıcısı
hf_llm = HuggingFacePipeline(pipeline=pipe)

# 4) NeMo Guardrails yapılandırmasını yükleyin
config = RailsConfig.from_path("config")

# 5) LLM'i "constructor" üzerinden enjekte ederek Guardrails motorunu başlatın
rails = LLMRails(config, llm=hf_llm)

# 6) Basit etkileşim döngüsü
print("\n--- NeMo Guardrails DEMO (Transformers + HF) ---")
print("Örnek: 'merhaba' veya 'hi' yazın; Colang akışı tetiklenecektir.")
print("Çıkmak için Ctrl+C.\n")

while True:
    user_msg = input("Kullanıcı: ")
    messages = [{"role": "user", "content": user_msg}]
    bot_reply = rails.generate(messages=messages)
    print(f"Bot    : {bot_reply['content']}\n")
