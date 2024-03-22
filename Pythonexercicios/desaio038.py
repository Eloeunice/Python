print('Digite abaixo o valor de cada número:')
n1 = int(input('Number 1:'))
n2 = int(input('Number 2:'))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('O segundo valor é maior.')
