# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def salarioTotal(n1, n2):
    if n2 > 40:
        salario_total = n1 + (n2 * 1.5)
    else:
        salario_total = n1
    return salario_total


salario = float(input(f"Digite o seu salário: "))
horas = float(input(f"Digite quantas horas você trabalhou este mês: "))

print(f"Você irá receber R$ {salarioTotal(salario, horas)} este mês.")


