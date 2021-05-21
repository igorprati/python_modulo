# 4.	Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.

from time import sleep
import random as rd
from operator import itemgetter

jogo = { #cria 4 chaves com 1 valor aleatório cada uma
    'Joao': rd.randint(1,6), # item 1 = chave = 'Joao', valor aleatório
    'José': rd.randint(1,6),
    'Maria': rd.randint(1,6),
    'Ronaldo': rd.randint(1,6),
}

classificacao = {} # cria um dicionário para classificar o ganhador

for j, v in jogo.items(): # j traz a chave (jogador) e v traz o valor(dados)
    print(f'\n{j} tirou {v} nos dados.')
print()
print(f'---' * 8)

classificacao = sorted(jogo.items(), key=itemgetter(1), reverse=True) # sorted para colocar em ordem crescente apenas o itemgetter[1] (valor), reverse para colocar em ordem decrescente, do maior para o menor

for i, v in enumerate(classificacao): # utilizando o enumerate, o valor de i é cada item = 0, 1, 2, 3... e v é o valor, sendo v[0] nome e v[1] dados
    print(f'{i+1}º lugar {v[0]} com dados: {v[1]}') 
print()