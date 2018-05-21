import time

class Dog(object):
    patas = 4
    cor = None
    tamanho = None
    sexo = None
    idade = None

    def __init__(self, cor, tamanho, sexo, idade, patas = 4):
        print("Iniciando Dog")
        print(cor, tamanho, sexo, idade, patas)
        self.cor = cor
        self.tamanho = tamanho
        self.sexo = sexo
        self.idade = idade
        self.patas = patas

    def latir(self):
        print("Bark")

    def descricao(self):
        print("Cor: {0}".format(self.cor))
        print("Tamanho" + self .tamanho)
        print("Sexo: " + self.sexo)
        print("Idade: " + str(self.idade))
        print("Patas: " + str(self.patas))
        print(self.latir())
        print(self.latido())

class Shinauzer(Dog):
    raca = "Shinauzer"
    nome = None

    def __init__(self, nome, cor, tamanho, sexo, idade, patas):
        print("Iniciando Shinauzer")
        super().__init__(cor, tamanho, sexo, idade, patas) #chama o método __init__ da classe herdada
        self.nome = nome
        # self.cor = cor
        # self.tamanho = tamanho
        # self.sexo = sexo
        # self.idade = idade
        # self.patas = patas

    def latido(self):
        print("Auau")

    def descricao(self):
        print("Nome: " + self.nome)
        print("Raça: %s" %(self.raca))
        super().descricao()


twister = Dog("Preto", "Pequeno", "Fêmea", 5)
twister.latir()
# print(dir(twister))
print("-"*100)
time.sleep(2)
cachorro = Shinauzer("Twister", "Preto", "Medio", "Macho", 10, 4)
print("-"*100)
cachorro.latir()
cachorro.latido()
# print(dir(cachorro))
print("-"*100)
cachorro.descricao()

