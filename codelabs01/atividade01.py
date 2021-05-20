# 01 - Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:

# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

lista = [5, 7, 2, 9, 4, 1, 3]

# a) tamanho da lista.
print(f"O tamanho da lista é: {len(lista)}")

# b) maior valor da lista.
print(f"O maior valor da lista é: {max(lista)}")

# c) menor valor da lista.
print(f"O menor valor da lista é: {min(lista)}")

# d) soma de todos os elementos da lista.
print(f"A soma de todos os valores da lista é: {sum(lista)}")

# e) lista em ordem crescente.
print(f"A lista em ordem crescente é: {sorted(lista)}")

# f) lista em ordem decrescente.
print(f"A lista em ordem decrescente é: {sorted(lista, reverse=True)}")

