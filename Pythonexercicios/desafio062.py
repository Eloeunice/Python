# DES 062 Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0  termos.


pt = int(input('Digite o primeiro termo:'))
ra = int(input('Digite a razão da PA:'))
count = 0
while not count == 10:
    count += 1
    pt += ra
    print(pt, end=' ')
    continue
while True:
    r = int(input('\nQuantos termos a mais?'))
    if r != 0:
        for c in range(r):
            pt += ra
            print(pt, end=' ')
            continue
    else:
        print('Fim do programa.')

