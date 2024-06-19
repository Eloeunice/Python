# desafio 052- Faça um prgrama que leia um número inteiro e diga se ele
# é ou não um número primo (só é divisível por 1 e por ele mesmo).
num = int(input("Digite o número:"))
t = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
print('\n\033[m O número {} foi divisível {} vezes.'.format(num, t))
if t == 2:
    print('É UM NÚMERO PRIMO')
else:
    print('NÃO É UM NÚMERO PRIMO')

