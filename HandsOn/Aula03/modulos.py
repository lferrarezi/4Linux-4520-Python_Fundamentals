import os, sys, datetime
from time import sleep

# ver usuário logado
print(os.getlogin())
print(sys.platform)
print(datetime.datetime.now())
print("\n")

print(os.get_exec_path())
print("\n")

# Lista conteúdo de diretório
print(os.listdir("/Users"))
print("\n")

print(sys.argv)

sleep(5)
# os.system("clear")

