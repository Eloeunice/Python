print('Digite o valor das três retas sendo a Reta 1 o maior lado')
r1 = int(input('Reta 1 (Maior reta):'))
r2 = int(input('Reta 2:'))
r3 = int(input('Reta 3:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formam um triângulo.')
    if r1 == r2 == r3:
        print('Há a formação do triângulo EQUILÁTERO, pois todos os lados são iguais.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Há a formação do triângulo ISÓSCELES, pois 2 lados são iguais.')
    else:
        print('Há a formação do triângulo ESCALENO, pois todos os lados são diferentes.')
else:
    print('Essas retas não formam um triângulo.')
#!=(diferente)