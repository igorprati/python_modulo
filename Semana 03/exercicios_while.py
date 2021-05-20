# NÃO PODE UTILIZAR LISTAS COMPOSTAS, NEM DICIONÁRIOS, APENAS WHILE:

# 01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

def novosNumeros():
    global num1, num2
    num1 = int(input(f'Digite o primeiro valor: '))
    num2 = int(input(f'Digite o segundo valor: '))


def soma():
    global num1, num2
    soma = num1 + num2
    print(f'\n------- A soma é {soma} -------')


def multiplicar():
    global num1, num2
    multiplicar = num1 * num2
    print(f'\n------- A multiplicação é {multiplicar} -------')


def maior():
    global num1, num2
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    print(f'\n------- O maior número é {maior} --------')


menu = 0
num1 = int(input(f'Digite o primeiro valor: '))
num2 = int(input(f'Digite o segundo valor: '))

while menu < 5:
    menu = int(input(
        f'\nEste é o MENU\n{"===" * 4}\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair\n\nEscolha uma opção: '))
    if menu == 1:
        soma()
    elif menu == 2:
        multiplicar()
    elif menu == 3:
        maior()
    elif menu == 4:
        novosNumeros()

print('\n ----- Você saiu do programa! -----\n')

# 02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#  A) quantas pessoas tem mais de 18 anos.
#  B) quantos homens foram cadastrados.
#  C) quantas mulheres tem menos de 20 anos.

# contadorHomens = contadorIdade = contadorMulheres =  0
# parar = False

# while parar == False:
#     idade = int(input('Digite sua idade por favor: '))
#     if idade > 18:
#         contadorIdade += 1

#     sexo = input('Certo... Agora me informe seu sexo biológico: ').strip().upper()[0]
#     if sexo == "M":
#         contadorHomens += 1
#     if sexo == "F" and idade < 20:
#         contadorMulheres += 1

#     continuar = input('\nDeseja continuar cadastrando? [S/N]: \n').strip().upper()[0]
#     if continuar == "N":
#         parar = True

# print(f"\nForam cadastrados {contadorHomens} homens.\n{contadorIdade} pessoas tem mais de 18 anos.\n{contadorMulheres} mulheres tem menos de 20 anos.")

# 03 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
