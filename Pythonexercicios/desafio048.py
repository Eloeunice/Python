# desafio 048- Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
# de 3 e que
#se encontram no intervalo de 1 até 500
print('A soma entre todos os números ímpares de 1 a 500 que são múltiplos de 3 é:')
s = 0
count = 0
for c in range(1, 501, 2): #números ímpares
 #Un número é divisível por 3, se a soma dos seus algarismos é divisível por 3
   if c % 3 == 0:
    count += 1
    s += c
print(s)
print(count, "valores")



