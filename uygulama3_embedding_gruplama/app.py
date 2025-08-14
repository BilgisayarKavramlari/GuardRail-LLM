import numpy as np
from sentence_transformers import SentenceTransformer, util

# --- 1. ADIM: KÜTÜPHANE OLUŞTURMA VE MODELİ YÜKLEME ---

# Türkçe ve birçok dili anlayan, güçlü bir model seçiyoruz.
# Model ilk çalıştırmada otomatik olarak indirilecektir.
print("Dil modeli yükleniyor... (Bu işlem ilk seferde birkaç dakika sürebilir)")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Ayrımcılık ve nefret söylemi olarak kabul edilecek ifadelerden bir "kütüphane" oluşturalım.
# NOT: Bu liste sadece bir örnektir ve gerçek bir sistem için çok daha kapsamlı olmalıdır.
# Farklı konuları ve ifade biçimlerini içermesi önemlidir.
NEFRET_SOYLEMI_KUTUPHANESI = [
    "belirli bir ırktan olanlar aşağılıktır",
    "farklı etnik kökenden gelenlere güvenilmez",
    "kadınlar bu işi yapamaz",
    "onların inancı tamamen saçmalık",
    "göçmenler ülkeden atılmalı",
    "bu insanlar toplum için bir tehdittir",
    "cahil topluluk",
    "zihinsel olarak yetersizler",
    "bu grup suç işlemeye daha yatkındır"
]

# "Eğitim" adımı: Kütüphanemizdeki her bir ifadenin embedding'ini bir kereliğine hesaplayıp saklıyoruz.
# Bu, her kullanıcı girdisi için tekrar tekrar hesaplama yapmamızı engeller ve sistemi hızlandırır.
print("Nefret söylemi kütüphanesi için anlamsal vektörler (embeddings) oluşturuluyor...")
kutuphane_embeddings = model.encode(NEFRET_SOYLEMI_KUTUPHANESI, convert_to_tensor=True)
print("Sistem hazır. Lütfen girdinizi yazın.")

# --- 2. ADIM: KULLANICI GİRDİSİNİ KONTROL ETME ---

def check_and_moderate(user_input: str, threshold=0.70):
    """
    Kullanıcı girdisini anlamsal olarak analiz eder ve nefret söylemi içerip içermediğini kontrol eder.
    
    Args:
        user_input (str): Kullanıcının girdiği metin.
        threshold (float): Benzerlik için kabul edilecek en düşük skor eşiği.
    
    Returns:
        (bool, str): (İçerik Sakıncalı mı?, Maskelenmiş Metin)
    """
    # Girdiyi cümlelere veya anlamlı parçalara bölmek daha iyi sonuç verir.
    # Şimdilik basitlik adına girdinin tamamını tek bir parça olarak alıyoruz.
    # Daha gelişmiş bir sistem için metni cümlelere ayırabilirsiniz.
    
    # Kullanıcı girdisinin embedding'ini hesapla
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    
    # Kullanıcı girdisi ile kütüphanedeki her bir ifade arasındaki kosinüs benzerliğini hesapla
    cosine_scores = util.cos_sim(input_embedding, kutuphane_embeddings)
    
    # En yüksek benzerlik skorunu bul
    highest_score = np.max(cosine_scores.cpu().numpy())
    
    if highest_score > threshold:
        # Eşiği geçen bir benzerlik bulundu.
        # Hangi ifadeye benzediğini bulalım (opsiyonel, loglama için yararlı)
        most_similar_index = np.argmax(cosine_scores.cpu().numpy())
        most_similar_phrase = NEFRET_SOYLEMI_KUTUPHANESI[most_similar_index]
        
        print(f"\n[UYARI] Girdi, '{most_similar_phrase}' ifadesiyle anlamsal olarak %{highest_score*100:.2f} oranında benzeşiyor.")
        
        # Girdiyi maskele
        masked_text = f"[SAKINCALI İÇERİK TESPİT EDİLDİ VE MASKELENDİ]"
        return (True, masked_text)
    else:
        # Girdi temiz
        return (False, user_input)

# --- 3. ADIM: UYGULAMAYI ÇALIŞTIRMA ---

if __name__ == "__main__":
    while True:
        try:
            user_text = input("\n> ")
            if user_text.lower() in ['exit', 'çıkış', 'q']:
                break

            is_harmful, result_text = check_and_moderate(user_text)

            if is_harmful:
                print(f"Sonuç: {result_text}")
                print("Bu girdi işlenemez ve cevap üretimi engellenmiştir.")
            else:
                print("Sonuç: Girdi temiz görünüyor.")
                # Burada normalde bir cevap üretecek olan kodunuz çalışırdı.
                # Örneğin: print(f"Yapay zeka cevabı: '{user_text}' girdinize istinaden...")

        except (KeyboardInterrupt, EOFError):
            print("\nUygulama sonlandırılıyor.")
            break