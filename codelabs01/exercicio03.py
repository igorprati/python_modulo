# 3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) e
# mostre ao final a quantidade de pessoas de cada estado civil.

lista = list()

for i in range(1, 16):
    lista.append(input('Digite o seu estado civil: ').lower())

print(lista)
print(f"São {lista.count('solteiro')} solteiros e {lista.count('casado')} casados.")

