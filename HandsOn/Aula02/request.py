import requests
requisicao2 = requests.get("http://www.httpbin.org/ip")

print(requisicao2.json())

resposta = requisicao2.json()
print(resposta["origin"])