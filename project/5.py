import requests

url = "http://79.132.141.128:8003/protected-data/"
headers = {
    'X-API-KEY': '3a3560dd9a914c61aab372a87060888e'  # Замените на ваш API-ключ
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json()[1][0]['object']['object'])
    print(response.json()[1][0]['object']['score'])
else:
    print(f"Error: {response.status_code}, {response.text}")