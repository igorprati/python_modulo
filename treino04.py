# Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
# pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse
# exercício, pesquise sobre a função date da biblioteca Datetime.

import datetime

def voto(ano):
    hoje = datetime.datetime.now()
    ano_nasc = ano
    idade = hoje.year - ano_nasc

    if idade < 18 and idade >= 16:
        print(f"Você tem {idade} anos. O voto é OPCIONAL.")
    elif idade < 16:
        print(f"Você tem {idade} anos. O voto é NEGADO.")
    else:
        print(f"Você tem {idade} anos. O voto é OBRIGATÓRIO!")

voto(2006)






