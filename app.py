from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API bilgileri
API_KEY = "APIKEY" # API Key - getcody.ai
API_URL_CONVERSATIONS = "https://getcody.ai/api/v1/conversations"
API_URL_MESSAGES = "https://getcody.ai/api/v1/messages"
BOT_ID = "BOT_ID"  # Bot ID'si


def create_conversation():
    """Yeni bir konuşma oluştur ve conversation_id'yi döndür."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "name": "Yeni Konuşma",
        "bot_id": BOT_ID
    }
    response = requests.post(API_URL_CONVERSATIONS, headers=headers, json=data)
    
    # 200 veya 201 yanıtlarını kabul et
    if response.status_code in [200, 201]:
        conversation_id = response.json().get('data', {}).get('id')
        return conversation_id
    else:
        print(f"Konuşma oluşturulamadı: {response.status_code} - {response.text}")
        return None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form.get('message')
    conversation_id = create_conversation()  # Yeni konuşma oluştur

    if not conversation_id:
        return jsonify({"response": "Konuşma ID oluşturulamadı, lütfen tekrar deneyin."})

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "content": user_message,
        "conversation_id": conversation_id
    }

    try:
        response = requests.post(API_URL_MESSAGES, headers=headers, json=data)
        print(f"API Yanıt Kodu: {response.status_code}")
        print(f"API Yanıtı: {response.text}")

        if response.status_code == 200:
            # Gelen veriden `content` bilgisini al
            bot_response = response.json().get('data', {}).get('content', 'Bot yanıt vermedi.')
        else:
            bot_response = f"API Hatası: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        bot_response = f"Bağlantı hatası: {str(e)}"

    return jsonify({"response": bot_response})


if __name__ == '__main__':
    app.run(debug=True)
