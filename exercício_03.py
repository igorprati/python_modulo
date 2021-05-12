# Faça um programa com uma função chamada somaImposto. A função possui dois
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o
# valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo=0):
    valorFinal = taxaImposto + (custo * taxaImposto)
    return valorFinal


num_custo = int(input(f"Digite o custo: "))
num_imposto = float(input(f"Digite o imposto: "))

print(f"O valor final do produto é: R$ {somaImposto(num_custo, num_imposto)}")
