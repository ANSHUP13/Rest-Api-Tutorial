import requests

BASE = "http://127.0.0.1:5000/"

resposnse = requests.post(BASE+"helloworld")
print(resposnse.json())
resposnse = requests.get(BASE+"helloworld")
print(resposnse.json())