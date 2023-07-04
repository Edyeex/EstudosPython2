
print("{:=^40}".format(" AMERICANAS "))
valor = float(input("Quanto cuta o produto? R$"))
print(''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input("Qual é a opção? "))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = valor / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS".format(parcela))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totalparc = int(input("Quantas parcelas: "))
    parcela = total / totalparc
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(totalparc, parcela))
else:
    total = valor
    print("OPÇÃO INVALIDA!!!")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(valor, total))
