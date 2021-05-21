#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))

# veririfca o maior número
if n1 > n2:
   maior = n1
else:
   maior = n2

# verifica se o resultado da soma é par ou ímpar
if (n1 + n2) % 2 == 0:
   resultadoSoma = "Par"
else:
   resultadoSoma = "Impar"

# verifica se a multiplicação for maior que 40 e divide o resultado pela divisão inteira
if n1 < n2:
   resultadoMultip = "Não é possível dividir por zero." # caso n1 for menos que n2, o resultado será zero
elif (n1 * n2) > 40:
   resultadoMultip = (n1 * n2) / (n1//n2)
elif (n1 * n2) < 40:
   resultadoMultip = "A multiplicação não foi maior que 40"


print(f'''
   A soma entre os números é: {n1+n2}
   A multiplicação entre os números é: {n1*n2}
   A divisão inteira entre eles é: {n1//n2}
   O maior número é o {maior}
   O resultado da soma entre os números é: {resultadoSoma}
   Multiplicação maior que 40: {resultadoMultip} ({n1*n2} / {n1//n2})
''')

