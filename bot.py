import requests

API_KEY = "API_KEY"
API_URL_BOTS = "https://getcody.ai/api/v1/bots"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.get(API_URL_BOTS, headers=headers)

if response.status_code == 200:
    bots = response.json().get('data', [])
    for bot in bots:
        print(f"Bot Name: {bot['name']}, Bot ID: {bot['id']}")
else:
    print(f"Botlar alınamadı: {response.status_code} - {response.text}")
