valor = int(input("Valor para sacar [10 : 600]: "))

cem = valor // 100
valor = valor - (cem*100)

cinquenta = valor // 50
valor -= (cinquenta*50)

dez = valor // 10
valor -= (dez*10)

cinco = valor // 5
valor -= (cinco*5)

um = valor

print(f"Nota de R$100 : {cem}")
print(f"Nota de R$50 : {cinquenta}")
print(f"Nota de R$10 : {dez}")
print(f"Nota de R$5 : {cinco}")
print(f"Nota de R$1 : {um}")