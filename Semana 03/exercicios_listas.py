# 01 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


# listaUnica = list()
# listaPar = list()
# listaImpar = list()

# for n in range(0, 7):
#     numero = int(input('Digite um número: '))
#     listaUnica.append(numero)

#     if numero % 2 == 0:
#         listaPar.append(numero)

#     elif numero % 2 != 0:
#         listaImpar.append(numero)

# print('-=-'*20)
# print(f'Todos os números são: {sorted(listaUnica)}')
# print('-=-'*20)
# print(f'Os numeros ímpares são: {sorted(listaImpar)}')
# print('-=-'*20)
# print(f'Os números pares são: {sorted(listaPar)}')


# 02 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:
""" 
[  1  ][  2  ][  3  ]
[  4  ][  5  ][  6  ]
[  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[coluna][linha]) 
"""

# matrizPrincipal = []
# matrizSec = []

# while True:
#     for i in range(0, 3):
#         matrizSec.append(int(input('Numero: ')))
#     matrizPrincipal.append(matrizSec[:])
#     matrizSec.clear()

#     for i in range(0, 3):
#         matrizSec.append(int(input('Numero: ')))
#     matrizPrincipal.append(matrizSec[:])
#     matrizSec.clear()

#     for i in range(0, 3):
#         matrizSec.append(int(input('Numero: ')))
#     matrizPrincipal.append(matrizSec[:])
#     matrizSec.clear()

#     break


# print(f'[  {matrizPrincipal[0][0]}  ] [  {matrizPrincipal[0][1]}  ] [  {matrizPrincipal[0][2]}  ]')
# print(f'[  {matrizPrincipal[1][0]}  ] [  {matrizPrincipal[1][1]}  ] [  {matrizPrincipal[1][2]}  ]')
# print(f'[  {matrizPrincipal[2][0]}  ] [  {matrizPrincipal[2][1]}  ] [  {matrizPrincipal[2][2]}  ]')

'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0,3):
   for c in range(0,3):
      matriz[l][c] = int(input(f'Digite um valor [{l},{c}]: '))

for l in range(0,3):
   for c in range(0,3):
      print(f'[{matriz[l][c]:^5}]', end='')
   print()
'''

# 03 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna.
#    C) O maior valor da segunda linha.

# import os
# matrizPrincipal = []
# matrizSec = []
# matrizPar = []
# segundaLinha = []
# maior = 0

# while True:
#     for i in range(0, 3):
#         numero = int(input('Numero: '))
#         matrizSec.append(numero)
#         if numero % 2 == 0:
#             matrizPar.append(numero)
#     matrizPrincipal.append(matrizSec[:])
#     matrizSec.clear()

#     for i in range(0, 3):
#         numero = int(input('Numero: '))
#         matrizSec.append(numero)
#         segundaLinha.append(numero)
#         if numero % 2 == 0:
#             matrizPar.append(numero)
#     matrizPrincipal.append(matrizSec[:])
#     matrizSec.clear()

#     for i in range(0, 3):
#         numero = int(input('Numero: '))
#         matrizSec.append(numero)
#         if numero % 2 == 0:
#             matrizPar.append(numero)
#     matrizPrincipal.append(matrizSec[:])
#     matrizSec.clear()

#     break
# os.system('cls' if os.name == 'nt' else 'clear')

# print(f'\n[  {matrizPrincipal[0][0]}  ] [  {matrizPrincipal[0][1]}  ] [  {matrizPrincipal[0][2]}  ]')
# print(f'[  {matrizPrincipal[1][0]}  ] [  {matrizPrincipal[1][1]}  ] [  {matrizPrincipal[1][2]}  ]')
# print(f'[  {matrizPrincipal[2][0]}  ] [  {matrizPrincipal[2][1]}  ] [  {matrizPrincipal[2][2]}  ]')
# print('\n')
# print(f'A soma dos valores pares é: {sum(matrizPar)}')
# print(f'A soma dos valores da terceira coluna é: {matrizPrincipal[0][2] + matrizPrincipal[1][2] + matrizPrincipal[2][2]}')
# print(f'O maior valor da segunda linha é: {max(segundaLinha)}\n')


# 04 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# import time
# import random as rd

# n = int(input('Digite quantos jogos você quer gerar: '))
# numSena = []

# for i in range(0, n):
#     numeros = rd.sample(range(1,61), 6)
#     numSena = numeros
#     time.sleep(0.5)
#     print(f'\nCarregando jogos aleatórios...')
#     time.sleep(1)
#     print(f'{sorted(numSena)}\n')
