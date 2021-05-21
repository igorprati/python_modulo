#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

import random as rd
from os import system
import sys

senhaValida = 'senhasenha'
senha = ''
tentativas = 4

while True: # validação da senha
    senha = input('Digite sua senha: ')
    if senha != senhaValida: # se a senha for diferente...
        tentativas -= 1 # diminui uma tentativa restante
        print(f'Senha incorreta. Tentativas restantes {tentativas}')
        if tentativas == 0: # se o numero de tentativas restantes forem 0...
            print('\nAcesso negado. Número de tentativas excedido!\n')
            sys.exit() # acesso negado, encerra o programa          
    elif senha == senhaValida: # se as senhas forem iguais...
        system('cls') # limpa o prompt de comando
        print('\nVocê está logado')
        break # encerra o while de validação de senha, continua as próximas linhas de código

print('''
        Seja bem vindo ao Jogo da Adivinhação!
------------------------------------------------------------
Para este jogo, você precisa descobrir o número que
eu escolhi, de 1 a 10. Eu vou te dar dicas, fique tranquilo!

        Vamos lá?
------------------------------------------------------------
''')

numMaquina = rd.randint(1,10) # gera um número aleatório de 1 a 10
n = int(input('Dê o seu palpite de 1 a 10: ')) # usuário escolhe um número
palpites = 0 # contador de palpites

while n > 10 or n < 1: # validação para ver se o número está entre 1 e 10
    print('\n!!!! Atenção! Apenas números de 1 a 10 !!!!')
    n = int(input('Dê o seu palpite de 1 a 10: ')) 

while True:
    if n != numMaquina: # enquanto o número for diferente...
        palpites += 1 # some 1 a cada palpite
        if n < numMaquina: # se o número escolhido for menor
            print('Quase... um pouco mais!\n')
            n = int(input('Dê o seu palpite de 1 a 10: '))
        elif n > numMaquina: # se o número escolhido for maior
            print('Quase.. um pouco menos!\n')
            n = int(input('Dê o seu palpite de 1 a 10: '))
    elif n == numMaquina: # se o usuário acertou o número escolhido
        palpites += 1 # some 1 ao palpite
        print(f'\n\nParabéns! Você acertou! Foram necessários {palpites} palpites.\n') # mostre a soma total dos palpites
        break
        
        