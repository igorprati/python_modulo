#04 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase = input("Digite uma frase: ")

for i in frase:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        frase = frase.replace(i, "")


print(frase)

