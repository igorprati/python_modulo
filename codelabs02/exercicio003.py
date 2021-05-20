# 03 -Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random as rd

numPC = rd.randrange(0, 11)
numJogador = int(input("Dê seu palpite de 0 a 10: "))
contador = 1

while numPC != numJogador:
    numJogador = int(input("Dê seu palpite de 0 a 10: "))
    contador += 1

print(f'Você acertou depois de {contador} tentativas.')

