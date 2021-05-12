# Escreva uma função que, dado um número nota representando a nota de um estudante,
# converte o valor de nota para um conceito (A, B, C, D, E e F).

def conceito(nota):
    if nota >= 9:
        conceito = "A"
    elif nota >= 8:
        conceito = "B"
    elif nota >= 7:
        conceito = "C"
    elif nota >= 6:
        conceito = "D"
    elif nota >= 5:
        conceito = "E"
    elif nota <= 4:
        conceito = "F"
    return conceito


print(f"Seu conceito foi: {conceito(10)}")