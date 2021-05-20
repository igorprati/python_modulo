#01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições. Dica: utilizar a biblioteca random do Python.

import random

num_random1 = random.randint(1,50)
num_random2 = random.randint(1,50)
num_random3 = random.randint(1,50)
num_random4 = random.randint(1,50)
num_random5 = random.randint(1,50)
tupla = (num_random1, num_random2, num_random3, num_random4, num_random5)

print(f"Os valores da tupla são: {tupla}")
print(f"O maior valor da tupla é {max(tupla)}, e o menor valor é {min(tupla)}.")

