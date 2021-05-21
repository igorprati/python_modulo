# 3.	Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo sa estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado


situacao = dict()

situacao['Nome'] = str(input('Nome: '))
situacao['Nota'] = float(input('Nota: '))

if situacao['Nota'] >= 7:
    print(f'O aluno {situacao["Nome"]} tirou nota {situacao["Nota"]} e está aprovado!')
elif 5 <= situacao['Nota'] <= 6.9:
    print(f'O aluno {situacao["Nome"]} tirou nota {situacao["Nota"]} e está de recuperação')
else:
    print(f'O aluno {situacao["Nome"]} tirou nota {situacao["Nota"]} e está reprovado!')