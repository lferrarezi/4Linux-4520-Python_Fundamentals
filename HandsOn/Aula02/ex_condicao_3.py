# If ternário
# não possui elif

lista = [0,1,2,3,4,9,87,10]
# len() retorna a quantidade de itens na lista
tamanho = 0

#r = 3 % 2
#print(r)

while tamanho < len(lista):
    print("par" if lista[tamanho] % 2 == 0 else "impar")
    tamanho += 1

for numero in lista:
    print("par" if numero % 2 == 0 else "impar")

for number in range(0,100,2):
    print(number)
