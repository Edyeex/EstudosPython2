valor = float(input("Qual é o valor do imovel?\nR$"))
salario = float(input("Qual é o seu salário mensal?\nR$"))
anos = int(input("Em quantos anos você quer financiar?\nAnos: "))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar o imóvel de \033[1;32mR${:.2f}\033[m em {} anos.".format(valor, anos, end=""))
print(", a prestação será de \033[1;32mR${:.2f}\033[m".format(prestacao))
if prestacao <= minimo:
    print("\033[1;32mEmprestimo aprovado\033[m")
else:
    print("\033[1;31mEmprestimo negado\033[m")