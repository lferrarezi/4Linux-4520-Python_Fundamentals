lista = [1,2,3,4,5,6]

list_comp = [ numero * numero for numero in lista]
print(list_comp)

pares = [p for p in lista if p % 2 == 0]
impares = [p for p in lista if p % 2]
print(pares, impares)