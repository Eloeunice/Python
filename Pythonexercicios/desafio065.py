# DES 065 Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from typing import Type

qnt = 0
soma = 0
num = 0
r = Type[str]
lista_num = []

while True:
    num = int(input('Digite um número:'))
    lista_num.append(num)
    qnt += 1
    soma += num
    med = soma / qnt
    r = input('Você deseja digitar mais valores?(S/N)').upper()
    if r == 'N':
        ma = max(lista_num)
        me = min(lista_num)
        print(f'A média foi {med}, o maior valor foi {ma} e o menor {me}')
        break
    else:
        continue
