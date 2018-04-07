'''
modos:
r - leitura
w - escrita (sobrescreve)
x - abre para criação (falha caso o arquivo exista)
a - abre para escrita (acrescenta no arquivo)
+ abre um arquivo para atualização (leitura e escrita)

/r/n - quebram a linha

'''

#with open("ex_open_file.py", "w") as f:
#    f.write("print('Curso de Python')")

#with open("ex_open_file.txt", "w") as f:
#    f.write("Curso de Python;")

#with open("ex_open_file.txt", "a+") as f:
#    f.write("Curso de Python;")

#with open("ex_open_file.txt", "r+") as f:
#    texto = f.read()
#    print(texto)
#    print(texto.split(";"))

#with open("ex_open_file.txt", "w") as f:
#    f.write("Curso de Python\r\n")
#    f.write("Curso de Python\r\n")
#    f.write("Curso de Python\r\n")
#    f.write("Curso de Python\r\n")

with open("ex_open_file.txt", "r+") as f:
   print(f.read().splitlines())
