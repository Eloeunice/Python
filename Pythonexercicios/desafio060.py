# DES 060 Faça um programa que leia um número qualquer e mostre o fatorial
n = int(input('Digite um número para ver seu fatorial:'))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print(f'O fatorial de {n} é {f}')
