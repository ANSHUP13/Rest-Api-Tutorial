import requests

BASE = "http://127.0.0.1:5000/"

resposnse = requests.post(BASE+"helloworld/Anshuman/1")
print(resposnse.json())
resposnse = requests.get(BASE+"helloworld/Anshuman/0")
print(resposnse.json())