# Flask Chatbot ve GetCody.ai API

Bu proje, Flask web uygulaması kullanarak GetCody.ai API ile entegrasyon sağlar ve dinamik olarak sohbet oluşturup bot yanıtları almanıza olanak tanır.

## 🚀 Özellikler
- 🌐 GetCody.ai API ile yeni bir sohbet oluşturma.
- 💬 Kullanıcı mesajlarını sohbet botuna gönderme.
- 📄 Bot yanıtlarını web arayüzünde görüntüleme.

## 🛠️ Gereksinimler
Aşağıdaki yazılımların yüklü olduğundan emin olun:
- **Python 3.7+**
- **Flask**
- **Requests kütüphanesi**

## 🔧 Kurulum

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/protesq/chat-bot-python.git
   cd <repo-adi>
   ```

2. **Gerekli Python paketlerini yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **API bilgilerinizi ayarlayın:**
   - `app.py` dosyasındaki `API_KEY` ve `BOT_ID` değerlerini kendi GetCody.ai bilgilerinize göre güncelleyin.

4. **Uygulamayı çalıştırın:**
   ```bash
   python app.py
   ```

5. **Tarayıcınızda çalıştırın:**
   - `http://127.0.0.1:5000` adresine gidin.

## 📂 Dosya Yapısı
```
<proje-dizini>/
|-- app.py              # Ana uygulama dosyası
|-- templates/
|   |-- index.html      # Frontend şablonu
|-- static/
|   |-- css/           # CSS dosyaları (varsa)
|   |-- js/            # JavaScript dosyaları (varsa)
|-- requirements.txt    # Python bağımlılıkları
|-- README.md           # Proje dokümentasyonu
```

## 🌟 API Entegrasyonu

### GetCody.ai API
Bu uygulama, GetCody.ai API ile entegrasyon sağlar ve aşağıdaki işlevleri gerçekleştirir:
- 🆕 Yeni bir sohbet oluşturma: `POST https://getcody.ai/api/v1/conversations`
- ✉️ Sohbet botuna mesaj gönderme: `POST https://getcody.ai/api/v1/messages`

### Ortam Değişkenleri
Güvenliğinizi sağlamak için, API bilgilerinizi `app.py` dosyasına sabit kodlamak yerine ortam değişkenlerinde veya bir konfigürasyon dosyasında saklayın.

## 📖 Örnek Kullanım
1. **Mesajınızı girin:** Ana sayfadaki metin giriş alanına mesajınızı girin.
2. **Gönderin:** "Gönder" butonuna tıklayarak sohbet botu ile etkileşimde bulunun.
3. **Yanıtı görüntüleyin:** Bot yanıtını sayfada görüntüleyin.

## 🛠️ Sorun Giderme
- 🔑 API Anahtarı ve Bot ID'nizin geçerli ve gerekli izinlere sahip olduğundan emin olun.
- 🌐 GetCody.ai API uç noktalarına erişilebildiğini kontrol edin.
- 🐞 Hataları debug etmek için konsolda yazılan logları inceleyin.

## 🤝 Katkı Sağlama
Katkılarınız memnuniyetle karşılanır! Hatalar veya yeni özellik istekleri için bir issue oluşturabilir veya pull request gönderebilirsiniz.

## 📜 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasını inceleyin.

---
Proje hakkında daha fazla bilgi veya soru için [GitHub profilime](https://github.com/protesq) göz atabilirsiniz!
