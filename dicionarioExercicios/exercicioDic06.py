# 6.	DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

pessoas = dict()
contadorPessoas = mediaIdade = 0
completoPessoas = list()
mulheres = list()
idades = list()
idadesAcimaMedia = list()

while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    pessoas['Idade'] = int(input('Idade: '))
    
    completoPessoas.append(pessoas.copy())
    idades.append(pessoas['Idade'])

    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas['Nome'])

    contadorPessoas += 1
    mediaIdade = sum(idades) / contadorPessoas

    if pessoas['Idade'] > mediaIdade:
        idadesAcimaMedia.append(pessoas['Idade'])

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'-----' * 6)
print(f'''
    Existem {contadorPessoas} pessoas cadastradas.
    A média das idades é de {mediaIdade} anos
    A lista de mulheres cadastradas: {mulheres}
    As idades acima da média são: {idadesAcimaMedia}
''')
print(f'-----' * 6)



