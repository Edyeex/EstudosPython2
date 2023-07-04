from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("{:=^40}".format(" ESCOLHA UMA OPÇÃO "))
print('''
[1] PEDRA
[2] PAPÉL
[3]TESOURA''')
jogador = int(input("Qual a sua escolha??🤔"))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-=+=-" * 11)
print("Eu joguei {}🤔".format(itens[computador]))
print("Você jogou {}🤔".format(itens[jogador]))
print("-=+=-" * 11)

if computador == 0: #Pedra
    if  jogador == 0:
        print("EMPATE😡")
    elif jogador == 1:
        print("VOCÊ VENCEU!!😒")
    elif jogador == 2:
        print("EU VENCI!!🤣")
    else:
        print("JOGADA INVALIDA!!!😐")     

elif computador == 1: #Papel
    if  jogador == 0:
        print("EU VENCI!!🤣")
    elif jogador == 1:
        print("EMPATE😡")
    elif jogador == 2:
        print("VOCÊ VENCEU!!😒")
    else:
        print("JOGADA INVALIDA!!!😐")  

elif computador == 2: #Tesoura
    if  jogador == 0:
        print("VOCÊ VENCEU!!😒")
    elif jogador == 1:
        print("EU VENCI!!🤣")
    elif jogador == 2:
        print("EMPATE😡")
    else:
        print("JOGADA INVALIDA!!!😐")  

    