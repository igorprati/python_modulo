# Declaração de variável

listaCand = ['José', 'Inácio', 'Tião', 'Severino', 'Branco', 'Nulo'] # lista dos possíveis votos
contador = 0
jose = inacio = tiao = severino = branco = nulo = 0 # contador de votos para cada canditato
continuarVoto = 'S' # laço while

print('Essa é a lista dos candidatos: \n') # mostra a lista dos candidatos

for i in listaCand:  # para numerar os candidatos
    contador += 1
    print(contador, i)

while continuarVoto == "S": # enquanto o usuário escolher continuar votando, while = True
    voto = int(input('\nDigite o número de acordo com o candidato a ser votado: '))
    if voto == 1:
        jose += 1
    elif voto == 2:
        inacio += 1
    elif voto == 3:
        tiao += 1
    elif voto == 4:
        severino += 1
    elif voto == 5:
        branco += 1
    elif voto == 6:
        nulo += 1
    continuarVoto = input('Continuar votando? [S/N]: ').upper() # pergunta se o usuário quer continuar votando

print(f'\n\nTotal de votos:\n\n ------- \n\n José: {jose}\n Inácio: {inacio}\n Tião: {tiao}\n Severino: {severino}\n\n Total de votos Brancos: {branco}\n Total de votos Nulos: {nulo}\n\n')




