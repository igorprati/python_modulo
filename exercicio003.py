#03 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores.

n = int(input("Digite um número: "))
contador = 0

for i in range(1, n+1):
    if n % i == 0:
        contador += 1

print(f"O número {n} possui {contador} divisores.")