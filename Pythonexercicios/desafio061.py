# DES 061 Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''for c in range(pt, pt + (11-1)*r,  r,):  # até o décimo termo usa se a fórmula da matemática
    print(c, end=" ")'''

pt = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão da PA:'))
count = 0
while not count == 10:
    print(pt, end=' ')
    count += 1
    pt += r
    continue
print('Fim')
