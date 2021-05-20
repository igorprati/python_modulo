# 5. Faça um programa que mostre os valores numéricos inteiros ímpares situados
# na faixa de 0 a 20.

impar = 0
par = 0

for i in range(0, 20+1):
    if i % 2 != 0:
        impar += 1


print(f"São {par} pares e {impar} ímpares.")
