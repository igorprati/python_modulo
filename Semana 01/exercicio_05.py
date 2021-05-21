# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
# 1,68 e pese 75kg.

def imc(altura, peso):
    imc = peso / float(altura * altura)
    return imc

print (f"O imc é: {imc(1.68, 75)}")