import json

lista_compras = [
    {
        "nome": "pao",
        "tipo": "francês",
        "marca": "mercado",
        "quantidade": {
            "medida": "unidades",
            "valor": 8
        }
    },

    {
        "nome": "mistura",
        "tipo": "mortadela",
        "marca": "Perdigão de ouro",
        "quantidade": {
            "medida": "fatia",
            "valor": 8
        }
    },

    {
        "nome": "mistura",
        "tipo": "salame",
        "marca": "sadia",
        "quantidade": {
            "medida": "gramas",
            "valor": 500
        }
    },

    {
        "nome": "queijo",
        "tipo": "branco",
        "marca": "vacaloka",
        "quantidade": {
            "medida": "gramas",
            "valor": 400
        }
    },

    {
        "nome": "queijo",
        "tipo": "prato",
        "marca": "vacaloka",
        "quantidade": {
            "medida": "fatias",
            "valor": 10
        }
    },

    {
        "nome": "fruta",
        "tipo": "tomate",
        "marca": "turma da monica",
        "quantidade": {
            "medida": "unidade",
            "valor": 1
        }
    },

    {
        "nome": "hortalica",
        "tipo": "alface",
        "marca": "raiz",
        "quantidade": {
            "medida": "saco",
            "valor": 1
        }
    },

    {
        "nome": "condimento",
        "tipo": "maionese",
        "marca": "hellmans",
        "quantidade": {
            "medida": "pote 800g",
            "valor": 1
        }
    }
]

for item in lista_compras:
    # print(json.dumps(item, indent=4, sort_keys=True))
    print(item["quantidade"]["valor"],
          item["quantidade"]["medida"],
          "de",
          item["nome"],
          item["tipo"],
          "da marca",
          item["marca"],
          )


def printLegivel(item):
    print(item["quantidade"]["valor"],
          item["quantidade"]["medida"],
          "de",
          item["nome"],
          item["tipo"],
          "da marca",
          item["marca"]
          )


def printItem(linha):
    linha = linha - 1
    printLegivel(lista_compras[linha])


def trocaItem(linha, novo_item):
    linha = linha - 1  # 8 - 1 = 7
    # print(json.dumps(novo_item, indent=4, sort_keys=True))
    # print(json.dumps(lista_compras[linha], indent=4, sort_keys=True))
    if (novo_item["nome"] == lista_compras[linha]["nome"]):
        # lista_compras[linha] = lista_compras[7]
        lista_compras[linha] = novo_item
        print("Item alterado:")
        printLegivel(lista_compras[linha])
    else:
        print("Os itens são de tipos diferentes.")


def trocaValor(linha, chave, valor):
    # linha recebeu 5
    # chave recebeu "quantidade"
    linha = linha - 1  # linha valendo 4
    lista_compras[linha][chave] = valor
    print(lista_compras[linha][chave])  # lista_compras[4]["tipo"]


requeijao = {
    "nome": "condimento",
    "tipo": "requeijao",
    "marca": "crioulo",
    "quantidade": {
        "medida": "pote",
        "valor": 1
    }
}

trocaItem(8, requeijao)

nova_quantidade = {
    "medida": "fatias",
    "valor": 10
}
trocaValor(5, "quantidade", nova_quantidade)

for item in lista_compras:
    # print(json.dumps(item, indent=4, sort_keys=True))
    printLegivel(item)
