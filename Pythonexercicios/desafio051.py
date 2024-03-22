# desafio 051- Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.
pt = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão da PA:'))
for c in range(pt, pt + (11-1)*r,  r):  # até o décimo termo usa se a fórmula da matemática
    print(c)
