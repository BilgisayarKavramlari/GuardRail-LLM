# GuardRail-LLM: LLM'ler için Pratik Güvenlik Duvarı Uygulamaları 🛡️

> Bu repo, Büyük Dil Modelleri (Large Language Models - LLM) için güvenlik duvarları (guardrails) oluşturmanın önemini ve pratiğini göstermek amacıyla hazırlanmış bir koleksiyondur. Güvenilir, güvenli ve etik sınırlar içinde çalışan yapay zeka uygulamaları geliştirmek için "guardrail" mekanizmaları kritik bir rol oynar.

Bu proje, **[NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)** kütüphanesini kullanarak farklı güvenlik senaryoları için somut ve çalıştırılabilir örnekler sunar. Her bir klasör, belirli bir güvenlik sorununa odaklanır ve bu sorunu nasıl ele alabileceğinizi gösteren bir uygulama içerir.

## 🎯 Projenin Amacı

Büyük Dil Modelleri, inanılmaz yeteneklere sahip olsalar da kontrolsüz bırakıldıklarında istenmeyen davranışlar sergileyebilirler. Bu proje, aşağıdaki gibi yaygın sorunları kontrol altına almak için programatik çözümler sunmayı hedefler:

-   **Konu Dışına Çıkma:** Modelin belirlenen alanın dışındaki sorulara cevap vermesini engelleme.
-   **Kişisel ve Hassas Veri İşleme:** Kullanıcıların kişisel bilgilerini (`PII`) paylaşmasını veya modelin bu tür bilgileri işlemesini önleme.
-   **Prompt Injection Saldırıları:** Kötü niyetli kullanıcıların, modelin temel sistem komutlarını manipüle etmesini engelleme.
-   **Toksik ve Zararlı Dil Kullanımı:** Hem kullanıcının girdisindeki hem de modelin çıktısındaki zararlı dil kullanımını tespit edip engelleme.

## 🛠️ Kullanılan Teknolojiler

-   **[NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails):** LLM'ler için programlanabilir, denetlenebilir ve kontrol edilebilir güvenlik duvarları eklemek için kullanılan ana açık kaynak kütüphane.
-   **[LangChain](https://www.langchain.com/):** LLM uygulamaları geliştirmeyi basitleştiren bir framework.
-   **[Hugging Face Modelleri](https://huggingface.co/):** Temel dil modeli olarak `flan-t5` modeli kullanılmıştır.

## 📂 Proje Yapısı

Proje, her biri farklı bir güvenlik duvarı konseptini ele alan modüler bir yapıda tasarlanmıştır. Her bir modül kendi klasöründe yer alır ve kendi `config` ve `app.py` dosyalarını içerir.

- `Uygulama 1 : Anonymizer`
  - _Temel bir anonimleştirme sürecini içerir._
- `Uygulama 2 : Anonymizer İleri`
  - _İleri Anonimleştirme tekniklerini içerir._
- `Uygulama 3 : Konu Kontrolü`
  - _Embedding kullanılarak bir içeriğin uygunluğu kontrol edilir._
- `Uygulama 4 : GuardRails Giriş`
  - _Temel bir akış ve guardrails çalışma mantığı sunar._
- `Uygulama 5 : Sağlık Uygulaması`
  - _Gelişmiş bir uygulama örneği olarak sağlık alanındaki vaka örneklerini içerir._
- `Uygulama 6 : İnsan Kaynakları ve Kişisel Veriler`
  - _Gelişmiş bir uygulama örneği olarak insan kaynakları alanındaki vaka örneklerini içerir._
- `Uygulama 7 : İçerik Üretimim`
  - _Gelişmiş bir uygulama örneği olarak içerik üretimi sırasındaki potansiyel tehditlere yönelik vaka örneklerini içerir._
- `Uygulama 8 : RAG ile birlikte kullanım`
  - _Bir LLM projesinde RAG (Retrieval Augmented Genration ) ile birlikte GuardRails yapısının nasıl kullanılabileceğini göstermektedir._

## 🚀 Kurulum ve Başlangıç

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/BilgisayarKavramlari/GuardRail-LLM.git](https://github.com/BilgisayarKavramlari/GuardRail-LLM.git)
    cd GuardRail-LLM
    ```

2.  **Sanal Ortam Oluşturun (Önerilir):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows için: venv\Scripts\activate
    ```

3.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Modüllerin Çalıştırılması:**
    Hemen her proje klasöründe tek bir app.py dosyası oluşturulmaya çalışıldı. Dizine girince bu dosyayı çalıştırmanız durumunda uygulama çalışacaktır. 

    ```powershell
    python app.py
    ```

## Proje Yapısı
<pre>
GuardRail-LLM/
├─ uygulama1_anonymizer/
├─ uygulama2_anonymizer_ileri/
├─ uygulama3_embedding_gruplama/
├─ uygulama4_guardrail_ai/
├─ uygulama5_saglik_guardrail/
├─ uygulama6_IK/
├─ uygulama7_Icerik/
├─ uygulama8_RAG/
├─ requirements.txt
└─ README.md
</pre>

* uygulama1_anonymizer: Temel PII/PHI tespiti ve anonimleştirme (ör. Presidio).

* uygulama2_anonymizer_ileri: Gelişmiş anonimleştirme ve maskeleme stratejileri.

* uygulama3_embedding_gruplama: Embedding üretimi ve kümelenmesi/gruplaması (vektör-tabanlı yaklaşım).

* uygulama4_guardrail_ai: Guardrails AI / NeMo Guardrails ile I/O korumaları.

* uygulama5_saglik_guardrail: Sağlık alanına özel guardrail örnekleri (uyarılar, danış yönlendirmesi vb.).

* uygulama6_IK: İK (HR) senaryolarında güvenli üretim.

* uygulama7_Icerik: İçerik denetimi / moderasyon örnekleri.

* uygulama8_RAG: RAG (Retrieval-Augmented Generation) ile guardrail entegrasyonu.

Yukarıdaki kısa açıklamalar klasör adlarına dayalı özetlerdir; ayrıntı ve çalıştırma adımları için ilgili alt uygulamanın README’sine bakınız.

## Alt Uygulamalar

Aşağıdaki bağlantılar her alt klasöre ve (varsa) kendi `README.md` dosyalarına yönlendirir:

- **Uygulama 1 – Anonymizer (Temel)**
  - Klasör: [`./uygulama1_anonymizer/`](./uygulama1_anonymizer/)
  - README: [`./uygulama1_anonymizer/README.md`](./uygulama1_anonymizer/README.md)

- **Uygulama 2 – Anonymizer (İleri)**
  - Klasör: [`./uygulama2_anonymizer_ileri/`](./uygulama2_anonymizer_ileri/)
  - README: [`./uygulama2_anonymizer_ileri/README.md`](./uygulama2_anonymizer_ileri/README.md)

- **Uygulama 3 – Embedding Gruplama**
  - Klasör: [`./uygulama3_embedding_gruplama/`](./uygulama3_embedding_gruplama/)
  - README: [`./uygulama3_embedding_gruplama/README.md`](./uygulama3_embedding_gruplama/README.md)

- **Uygulama 4 – Guardrail AI / NeMo Guardrails Entegrasyonu**
  - Klasör: [`./uygulama4_guardrail_ai/`](./uygulama4_guardrail_ai/)
  - README: [`./uygulama4_guardrail_ai/README.md`](./uygulama4_guardrail_ai/README.md)

- **Uygulama 5 – Sağlık Guardrail**
  - Klasör: [`./uygulama5_saglik_guardrail/`](./uygulama5_saglik_guardrail/)
  - 1. Örnek Ana Akış : README: [`./uygulama5_saglik_guardrail/README.md`](./uygulama5_saglik_guardrail/README.md)
  - 2. Örnek (TEST Senaryoları) README: [`./uygulama5_saglik_guardrail/README_test.md`](./uygulama5_saglik_guardrail/README_test.md)

- **Uygulama 6 – İK (HR) Senaryoları**
  - Klasör: [`./uygulama6_IK/`](./uygulama6_IK/)
  - README: [`./uygulama6_IK/README.md`](./uygulama6_IK/README.md)

- **Uygulama 7 – İçerik/Moderasyon**
  - Klasör: [`./uygulama7_Icerik/`](./uygulama7_Icerik/)
  - README: [`./uygulama7_Icerik/README.md`](./uygulama7_Icerik/README.md)

- **Uygulama 8 – RAG (Retrieval-Augmented Generation)**
  - Klasör: [`./uygulama8_RAG/`](./uygulama8_RAG/)
  - README: [`./uygulama8_RAG/README.md`](./uygulama8_RAG/README.md)

> Not: Bir alt uygulamada `README.md` henüz yoksa, çalıştırma talimatları doğrudan klasör içindeki dosyalarda yer alıyor olabilir.


## Guardrail Türlerine Kısa Bakış
* Kural Tabanlı (Rule-Based): Regex, anahtar kelime listeleri, şablonlar.
Artı: Hızlı, yorumlanabilir. Eksi: Bağlamı kavraması sınırlı (kırılganlık).

* Model Tabanlı (Model-Based): Odaklı sınıflandırma/algılama modelleri (toksisite, PII/PHI, jailbreak vb.) ile giriş/çıkış denetimi.
Artı: Bağlam duyarlı. Eksi: Ek gecikme ve maliyet.

* Vektör/Embedding Tabanlı: Semantik benzerlik ile konu/alan dışına çıkışı engelleme (örn. cosine similarity).
Artı: Konu/niyet yakınlığını yakalar. Eksi: İnce ayrımlarda kaçırma.

* Şema/Gramer Zorlaması (Structured/Constrained Output): JSON Schema/CFG ile biçimsel geçerlilik garantisi.
Artı: “Daima geçerli JSON” vb. Eksi: İçeriksel doğruluğu tek başına garanti etmez.

* Decoding-Time Güvenlik (Safety-Aware Decoding): Üretim sırasında güvenlik/ödül modelleriyle token uzayını filtreleme.
Artı: İnference-time yönlendirme. Eksi: Gecikme artışı.

* Prompt Güvenliği & Enjeksiyon Savunması: Enjeksiyon/jailbreak tespiti, güvenilmeyen içeriğin izolasyonu.
Artı: Ajan/araç çağırma senaryolarında kritik. Eksi: Sürekli bakım gerekir.

* DLP/PII/PHI Koruması: Girdi/çıktıda kişisel/sağlık verilerinin tespiti ve anonimleştirilmesi.
Artı: Uyumluluk ve veri sızıntı riskinin düşürülmesi. Eksi: Dil/alan özelleştirmesi gerekebilir.

* HITL & Politika-olarak-Kod: Düşük güven-yüksek risk durumlarında insan devri; RBAC/ABAC ile eylem düzeyinde yetkilendirme.
Artı: Denetlenebilirlik. Eksi: Operasyonel yük.

Bu desenlerin birden fazlasını birlikte kullanarak savunma-içi-savunma (defense-in-depth) mimarisi önerilir.