
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input(" digite a segunda nota do aluno: "))
media = (n1 + n2) / 2
print("A nota total do aluno de {:.1f} e {:.1f}, é {:.1f}".format(n1, n2, media))

if 7 > media >= 5:
    print("O aluno está de RECUPERAÇÃO!!")
elif media < 5:
    print("O aluno está REPROVADO!!")
else:
    print("O aluno está APROVADO!!")