import requests
import json

url = "https://aves.ninjas.cl/api/birds"

def request_get(url):
    return json.loads(requests.get(url).text)

if __name__ =="__main__":
    url = "https://aves.ninjas.cl/api/birds"

response = request_get(url)

print(response)

if response.status_code == 200:
    print("Obtención correcta")
    #print(response.json)
    print("")
    post = response.json()
    print(post[0])

else:
    print("error")