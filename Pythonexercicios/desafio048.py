# desafio 048- Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
# de 3 e que
#se encontram no intervalo de 1 até 500
print('A soma entre todos os números ímpares de 1 a 500 que são múltiplos de 3 é:')
s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
     s += c #s recebe s + c
print(s)


