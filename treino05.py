# Exercício 5 - Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome=0, gols=0):
    nome = input("Digite o nome do jogador: ")
    gols = input("Digite a quantidade de gols: ")
    print(f"O jogador {nome} fez {gols} gols.")


ficha()