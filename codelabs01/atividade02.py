#02 - Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

r1 = input("Telefonou para a vítima?: ").lower()
r2 = input("Esteve no local do crime?: ").lower()
r3 = input("Mora perto da vítima?: ").lower()
r4 = input("Devia para a vítima?: ").lower()
r5 = input("Já trabalhou com a vítima?: ").lower()

lista = [r1, r2, r3, r4, r5]
contadorSim = 0
print(lista)

for i in lista:
    if i == "sim":
        contadorSim = contadorSim + 1

if contadorSim == 2:
    print("Suspeita")
elif contadorSim > 2 and contadorSim < 5:
    print("Cúmplice")
elif contadorSim == 5:
    print("Assassino")
else:
    print("Inocente")

    

