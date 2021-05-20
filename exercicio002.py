#02 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece as vogais a,e,i,o,u.

frase = input("Digite uma frase: ").lower()
contador = 0

for i in frase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        contador += 1
    

print(f"As vogais aparecem {contador} vezes!")