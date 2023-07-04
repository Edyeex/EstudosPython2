import time
numero = int(input("Digite um numero inteiro: "))
time.sleep(2)
print('''Escolha uma das opções para converter:\033[1;34m 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL \033[m''')

opcao = int(input("Sua opção:"))
time.sleep(2)
if opcao == 1:
    print("\033[1;34m{} convertido para BINÁRIO é {}\033[m".format(numero, bin(numero)[2:]))
elif opcao == 2:
    print("\033[1;34m {} convertido para OCTAL é {}\033[m".format(numero, oct(numero)[2:]))
elif opcao == 3:
    print("\033[1;34m {} convertido para HEXADECIMAL é {}\033[m".format(numero, hex(numero)[2:]))
else:
    time.sleep(2)
    print("\033[1;31;47m Opção Invalida \033[m")