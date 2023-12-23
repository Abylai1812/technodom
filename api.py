import requests
from bs4 import BeautifulSoup
import json

url = "https://api.technodom.kz/katalog/api/v1/products/category/smartfony?city_id=5f5f1e3b4c8a49e692fefd70&limit=24&brands=apple&cl-smartphones-memory-13=256&sorting=score&price=0"

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
data = json.loads(soup.text)

first_20_phones = data['payload'][:20]
filtered_data = {'payload': first_20_phones}

with open('apple.json', 'w', encoding='utf-8') as json_file:
    json.dump(filtered_data, json_file, ensure_ascii=False, indent=4)