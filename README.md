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
