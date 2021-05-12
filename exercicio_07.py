# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles
# forem iguais, imprima que eles são iguais.

def parametros(n1,n2):
    if n1 > n2:
        resultado = n2
    elif n1 == n2:
        resultado = "Os número são iguais!"
    else:
        resultado = n1
    return resultado



print(f"{parametros(5,5)}")