
num = int(input("Digite um número para ver sau tabuada: "))
for c in range(1, 11):
    print("{} X {:2} = {}".format(num, c, num*c))