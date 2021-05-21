# 5.	Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

ano = 2021
dados = dict()

dados['Nome'] = input('Nome: ')
dados['Idade'] = 2021 - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de trabalho: '))

if dados['CTPS'] != 0:
    dados['anoContratacao'] = int(input('Ano de contratação: '))
    dados['Salário'] = int(input('Salário: '))
    aposentadoria = (dados['anoContratacao'] + 35) - 1998
    print(f'Você irá se aposentar com {aposentadoria} anos.')
else:
    print('Não sei quando você vai se aposentar...')

print(dados)

