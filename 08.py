
peso = float(input("Digite o seu peso: (KG)"))
altura = float(input("Digite a sua altura: (M)"))
imc = peso / (altura ** 2)
print("O imc é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO normal!")
elif 18.5 <= imc < 25:
    print("Você está na faixa normal de peso")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO!!")
elif 30 <= imc <40:
    print("Você está em OBESIDADE!!")
else:
    print("Está em OBESIDADE MÓRBIDA!!")