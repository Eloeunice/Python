# desafio 052- Faça um prgrama que leia um número inteiro e diga se ele
# é ou não um número primo (só é divisível por 1 e por ele mesmo).
num = int(input('Digite um número:'))
if num % 2 == 0 and num != 2:
    print('Não é primo.')
if num % 3 == 0 and num != 3:
    print('Não é primo.')
if num % 5 == 0 and num != 5:
    print('Não é primo.')
if num % 7 == 0 and num != 7:
    print('Não é primo.')
if num % 11 == 0 and num != 11:
    print('Não é primo.')
else:
    print('É primo')




