# DES 059 Crie um programa que leia dois valores e mostre um menu na tela: 1-SOMAR,2-MULTIPLICAR.3-MAIOR,
# 4-NOVOS NÚMEROS,5-SAIR DO PROGRAMA. Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
while True:
    op = int(input('''Escola a operação:
    1 - SOMAR
    2 - MULTIPLICAR
    3 - MAIOR
    4 - NOVOS NÚMEROS
    5 - SAIR DO PROGRAMA
    >>'''))
    if op == 1:
        tot = n1 + n2
        print(f'O valor da soma entre {n1} e {n2} é {tot}.')
        continue
    elif op == 2:
        tot = n1 * n2
        print(f'O valor da multiplicação entre {n1} e {n2} é {tot}.')
        continue
    elif op == 3:
        tot = max(n1, n2)
        print(f'O maior valor é {tot}')
        continue
    elif op == 4:
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
        continue
    else:
        break