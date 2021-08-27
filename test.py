import requests
from pprint import pprint

BASE = "http://127.0.0.1:5000/"

resposnse = requests.put(BASE+"video/3",{'name':'closer','likes':100,'views':500000})
pprint(resposnse.json())

resposnse = requests.get(BASE+"video/3")
pprint(resposnse.json())

resposnse = requests.patch(BASE+"video/3",{'likes':99})
pprint(resposnse.json())

resposnse = requests.get(BASE+"video/3")
pprint(resposnse.json())


#resposnse = requests.delete(BASE+"video/2")
#print(resposnse.json())
#
#resposnse = requests.delete(BASE+"video/1")
#print(resposnse.json())
