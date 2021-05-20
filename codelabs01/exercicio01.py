# Crie um código em Python que pede qual tabuada o usuário quer ver, em
# seguida imprima essa tabuada.

n = int(input("Digite qual tabuada você quer ver: "))

print("------ soma -------")
for i in range(1, 11):
    soma = n + i
    print(f"{n} + {i} = {soma}")

print("\n------ multiplicação -------")

for i in range(1, 11):
    multiplicacao = n * i
    print(f"{n} * {i} = {multiplicacao}")

print("\n------ divisão -------")

for i in range(1, 11):
    divisao = n / i
    print(f"{n} / {i} = {divisao:.2f}")

print("\n------ subtração -------")

for i in range(1, 11):
    subtracao = n - i
    print(f"{n} - {i} = {subtracao}")



