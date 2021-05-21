#02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))

tupla = (num1, num2, num3, num4)

print(tupla)
print(f"O número 9 aparece: {tupla.count(9)} vezes")
print(f"O primeiro número 3 aparece na posição: {tupla.index(3)}")