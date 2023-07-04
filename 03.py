n1 = int(input("\033[33m Digite um numero: \033[m"))
n2 = int(input("\033[33m Digite outro numero: \033[m"))

if n1 > n2:
    print("\033[1;36m O PRIMEIRO numero é maior.\033[m")
elif n1 < n2:
    print("\033[1;36m O SEGUNDO numero é maior.\033[m")
else:
    print("\033[4;31m Não existe numero maior, os dois são iguais \033[m")
    