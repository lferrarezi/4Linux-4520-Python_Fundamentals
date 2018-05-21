import pprint, json

lista_compras = [
    {
        "nome": "pão",
        "tipo": "francês",
        "quantidade": {
            "medida": "unidade",
            "valor": 800
        }
    },
    {
        "nome": "mistura",
        "tipo": "mortadela",
        "quantidade": {
            "medida": "fatia",
            "valor": 8
        }
    },
    "presunto",
    "queijo",
    "tomate",
    "alface",
    "maionese"
]

print("\n")
print("# busca em listas é feita por posição 0,1,2,3...")
print("print(lista_compras)")
print(lista_compras)
print("\nprint(lista_compras[0])")
print(lista_compras[0])
print("\nprint(lista_compras[1])")
print(lista_compras[1])
print("\n")

lancheJoao = {
    "mistura": "salame",
    "queijo": "prato",
    "fruta": "tomate",
    "hortalica": "alface",
    "condimento": "maionese"
}

lancheMoto = {
    "mistura": "salame",
    "queijo": "prato",
    "fruta": "tomate",
    "hortalica": "alface",
    "condimento": "maionese"
}

monteSeuLanche = {
    "mistura": ["mortadela", "salame"],
    "queijo": ["branco", "prato"],
    "fruta": "tomate",
    "condimento": "maionese"
}
print("\n")
print("# busca em dicionário é feita por chaves...")
print("print(monteSeuLanche[""queijo""]")
print(monteSeuLanche["queijo"])

print("\n")
print("# busca em dicionário dentro de uma lista...")
print("\nlista_compras[0]["'nome'"]")
print(lista_compras[0]["nome"])

print("\n")

for item in lista_compras:
    print("pprint")
    pprint.pprint(item, indent=4)

    print("json")
    print(json.dumps(item, indent=4, sort_keys=True))
    print(item[0])

