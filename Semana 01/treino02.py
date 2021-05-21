# Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) como parâmetro e
# retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def num(a, b, limite):
    resultado = a + b > limite
    return resultado


print(f"Resultado é: {num(3,1, 1)}")