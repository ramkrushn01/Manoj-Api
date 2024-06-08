import requests
import json

r_get = requests.get('https://fakestoreapi.com/products')
r_data = r_get.json()

print(r_data)
reqUrl = "http://127.0.0.1:8000/api/products/"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

for dt in r_data:
    del dt['image']
    dt['name'] = dt['title']
    dt['company'] = 'm/r'
    dt['colors'] = "white"
    payload = json.dumps(dt)
    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

    print(response.text)


exit()

import requests
import json




payload = json.dumps({
  "name": "laptop",
  "company": "dell",
  "price": "189.95",
  "colors": "black",
  "description": "this is a dell laptop",
  "category": "digital",
  "featured": true
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)