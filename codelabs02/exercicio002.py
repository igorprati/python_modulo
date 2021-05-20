#02 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 0

while sexo != "M" and sexo != "F":
    sexo = input("Qual seu sexo? [M/F]: ").upper()

print(f'Você digitou {sexo}.')