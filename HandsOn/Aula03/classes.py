import time
class Cachorro:
    status = None
    raca = None
    nome = None
    cor = None
    tamanho = None
    sexo = None
    idade = None
    patas = 4
    latido = None

    def __init__(self, status, raca, nome, cor, tamanho, sexo, idade, patas, latido
                 ):
        self.status = status
        self.raca = raca
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.sexo = sexo
        self.idade = idade
        self.patas = patas
        self.latido = latido
        print("teste")

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def descricao(self):
        print("%s, é um cachorro da raça %s de porte %s e da cor %s" %(self.nome, self.raca, self.tamanho, self.cor))

    def latir(self):
        self.status = "Latindo"
        print(self.status)
        return self.latido * 3
        # print("Late %s! "%(self.nome))
        # time.sleep(1)
        # print("%s " %(self.latido) * 3)

    def comer(self, comida):
        self._status = "Comendo"
        return "%s está comendo %s" % (self.nome, comida)

    # def bricar(self, objeto):


    # def rolar(self, vezes):


    # def deitar(self):


print(Cachorro)

spark = Cachorro("Capenga", "Pug", "Spark",
                 "Marrom", "Pequeno", "Macho", 5, 4, "au")
twister = Cachorro("Morto", "Poodle", "Twister",
                 "Branco", "Grande", "Macho", 15, 5, "iau")

print("Spark")
print(spark)
print(spark.status)
print(spark.patas)
spark.descricao()

print("\n")

print("Twister")
print(twister)
print(twister.status)
print(twister.patas)
twister.descricao()

print("\n")

twister.idade = 20
print(vars(twister))

print("\n")

print(spark.latir())
print("\n")
print(twister.latir())

print("\n")
print(twister.comer("o pé da mesa"))