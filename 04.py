from datetime import date
atual = date.today().year
ano = int(input("\033[1;36mEm que ano você nasceu? \033[m"))
idade = atual - ano
print("\033[1;34mQuem nasceu no ano {} tem {} anos de idade em {}.\033[m".format(ano, idade, atual))
if idade == 18:
    print("\033[1;31mVocê tem que se alistar imediatamente!!.\033[m")
elif idade < 18:
    saldo = 18 - idade
    print("\033[1;35mAinda não está na hora de você se alistar, faltam {} anos.\033[m".format(saldo))
    alistamento = atual + saldo
    print("\033[1;35mSeu alistamento será em {}\033[m".format(alistamento))
else:
    saldo = idade - 18
    print("\033[1;30mJá passou da idade para se alistar, voce deveria ter se alistado há {} anos!.\033[m".format(saldo))
    alistamento = atual - saldo
    print("\033[1;30mSeu alistamento foi em {}\033[m".format(alistamento))