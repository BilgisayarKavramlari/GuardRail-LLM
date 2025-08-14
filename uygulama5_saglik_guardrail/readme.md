# Guardrail Kurulum ve İlk Örnek

## 1. Projenin amacı:
Bu proje, kullanıcılardan gelen sağlıkla ilgili soruları yanıtlayan bir yapay zeka asistanı oluşturmayı hedefler. Sistemin temel amacı, sadece bilgi sağlamak değil, aynı zamanda bunu etik ve güvenli bir çerçeve içinde yapmaktır. Bu çerçeve, iki ana prensip üzerine kuruludur:

Kullanıcı Gizliliğini Koruma: Kullanıcıların paylaştığı isim, yaş, konum gibi kişisel ve hassas sağlık bilgilerinin (PHI/PII) yapay zeka modeline asla ulaşmamasını sağlamak.

Güvenlik ve Zararı Önleme: Yapay zeka asistanının, kesin tıbbi teşhisler koymasını, yanlış veya tehlikeli tavsiyeler vermesini ve aşırı iddialı bir dil kullanmasını aktif olarak engellemek. Her durumda kullanıcıyı bir sağlık profesyoneline yönlendirmek.

## 2. Kullanılan Teknolojiler

Çerçeve (Framework): Nemo Guardrails (v0.9.0) - Etik ve güvenlik kurallarını tanımlamak ve uygulamak için kullanılan ana sistem.

Dil Modeli (LLM): google/flan-t5-large - Kullanıcının anonimleştirilmiş sorularını anlamak ve bilgilendirici cevaplar üretmek için kullanılan temel yapay zeka modeli. Hugging Face Transformers kütüphanesi üzerinden çalıştırılır.

Veri Gizliliği Aracı: Presidio (Microsoft) - Metin içindeki kişisel ve hassas verileri (isim, yaş, konum vb.) tespit edip anonimleştirmek için kullanılan uzman kütüphane.

Kural Dili: Colang ve YAML - Nemo Guardrails'in davranışsal kurallarını, akışlarını ve konfigürasyonunu tanımlamak için kullanılan diller.

## 3. Sistemin Çalışma Akışı

Sistem, kullanıcıdan gelen bir isteği son cevaba dönüştürürken katmanlı bir güvenlik yaklaşımı izler:

Adım: Kullanıcı İsteği (Prompt)

Kullanıcı, içinde kişisel bilgiler de barındırabilen tıbbi bir soru sorar.

Örnek: "Merhaba, benim adım Ahmet Çelik, 42 yaşındayım... Midemde yanma var. Bu ne olabilir?"

Adım: Giriş Koruması - Otomatik Anonimleştirme (Input Rail)

Kullanıcının bu isteği doğrudan LLM'e gönderilmez.

Önce, Nemo Guardrails'in tetiklediği özel bir Python aksiyonu (anonymize_user_prompt) devreye girer.

Bu aksiyon, Presidio kütüphanesini kullanarak metindeki "Ahmet Çelik", "42", "Ankara" gibi kişisel verileri tespit eder ve bunları <PERSON>, <AGE>, <LOCATION> gibi genel etiketlerle maskeler.

Sonuç: LLM'in eline geçen metin tamamen anonimdir. Bu, kullanıcı gizliliğini en başından garanti altına alır.

Adım: LLM'e Sorgu Gönderimi

Artık güvenli ve anonim olan prompt, cevap üretmesi için flan-t5-large modeline gönderilir.

LLM, bu anonim metne dayanarak bir cevap oluşturur (örn: "Midenizdeki yanma için olası nedenler şunlar olabilir...").

Adım: Çıkış Koruması - Teşhis ve Yasaklı İfade Kontrolü (Output Rail)

LLM'in ürettiği bu ham cevap, kullanıcıya gösterilmeden önce ikinci bir güvenlik katmanı olan Nemo Guardrails çıkış koruması tarafından yakalanır.

Bu koruma, healthcare.co dosyasında tanımlanan kurallara göre cevabı tarar:

Cevapta "Teşhisim...", "Tedaviniz...", "Garanti ederim ki..." gibi tehlikeli ve iddialı ifadeler var mı?

Eğer bu ifadelerden herhangi biri bulunursa, çıkış koruması tetiklenir.

Adım: Güvenli Yanıtın Oluşturulması

Senaryo A (Güvensiz Çıktı Tespit Edildi): Eğer çıkış koruması tetiklenirse, LLM'in orijinal, potansiyel olarak tehlikeli cevabı imha edilir. Onun yerine, healthcare.co dosyasında önceden tanımlanmış, tamamen güvenli olan standart bir mesaj kullanıcıya gösterilir: "Ben bir tıp uzmanı değilim ve teşhis koyamam... Lütfen bir doktora danışın."

Senaryo B (Güvenli Çıktı): Eğer LLM'in cevabı tüm kontrolleri geçerse, o zaman kullanıcıya gösterilir. (Mevcut kurallarımız tıbbi sorular için oldukça katı olduğundan, genellikle Senaryo A çalışacaktır.)

## 4. Kodun Ana Bileşenleri ve Sorumlulukları

app.py (Ana Uygulama Dosyası):

Tüm kütüphaneleri ve modelleri yükler.

anonymize_user_prompt adlı özel Python aksiyonunu tanımlar.

Nemo Guardrails'i başlatır ve konfigürasyonları birbirine bağlar.

Uygulamanın ana çalışma döngüsünü yönetir.

config_health/config.yml (YAML Konfigürasyon Dosyası):

Sistemin "yapılandırma beyni"dir.

Hangi LLM'in kullanılacağını (engine: huggingface), özel aksiyonların varlığını (actions:) ve hangi kural dosyalarının (.co) yükleneceğini belirtir.

config_health/healthcare.co (Colang Kural Dosyası):

Sistemin "etik kural kitabı"dır.

define flow, define user, define bot gibi komutlarla sistemin davranışsal mantığı burada tanımlanır.

Girişin nasıl işleneceği, hangi ifadelerin yasaklı olduğu ve bu ifadelerle karşılaşıldığında ne yapılacağı gibi tüm güvenlik mantığı bu dosyada yer alır.

anonymize_user_prompt (Özel Python Fonksiyonu):

Tek bir uzmanlık görevi olan "veri temizleme" aracıdır.

Sistemin geri kalanından bağımsız olarak, sadece gelen metindeki kişisel verileri bulup maskelemekten sorumludur. Bu modüler yapı, sistemin bakımını ve geliştirilmesini kolaylaştırır.

## 5. Sistemin Çalıştırılması

Kütüphaneleri kurun: 

<pre>
pip install -r requirements.txt
</pre>

Kurulum bittikten sonra, yine aynı terminale aşağıdaki komutu yapıştırıp Enter'a basın. Bu komut, Presidio kütüphanesinin ihtiyaç duyduğu dil modelini indirecektir.

<pre>
python -m spacy download en_core_web_lg
</pre>

Uygulamanın çalıştırılması : 
<pre>
python app.py
</pre>

