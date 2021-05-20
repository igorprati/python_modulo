# 6. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar
# a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães,
# de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o
# exemplo abaixo:

precoPao = 0.18

n = int(input("Digite quantos pães você quer: "))

for i in range(1, n+1):
    precoPao = i * 0.18
    print(f"{i} - R$ {precoPao:.2f}")



