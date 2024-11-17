# desafio 050-Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidera-o.
s = 0
for n in range(1, 7):
    num = int(input('Digite o valor:'))
    if num % 2 == 0:
        s += num
print('A soma dos números pares é: {}.'.format(s))
