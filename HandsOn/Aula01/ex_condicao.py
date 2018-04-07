#if int(input("Diga a sua idade:")) >= 16 and input("Trouxe documento? (S/N)") == "S":
#    print("Entre")
#else:
#    print("Não entre")

idade = input("Diga a sua idade:")
doc = input("Trouxe documento? (S/N)")

if int(idade) >= 18 and doc.lower() == "s":
    print("Entre")

elif int(idade) >= 16 and doc.lower() == "s":
    print("Entra mas não bebe")

else:
    print("Não entre")
