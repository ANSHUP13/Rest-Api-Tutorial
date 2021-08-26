import requests

BASE = "http://127.0.0.1:5000/"

resposnse = requests.put(BASE+"video/1",{'name':'at my worst','likes':100,'views':500000})
print(resposnse.json())

resposnse = requests.get(BASE+"video/1")
print(resposnse.json())

resposnse = requests.delete(BASE+"video/2")
print(resposnse.json())

resposnse = requests.delete(BASE+"video/1")
print(resposnse.json())
