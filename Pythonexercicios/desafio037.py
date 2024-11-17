n1 = int(input('Número 1:'))
print('As bases de conversão são:\n1-Para Binários \n2-Para Octal \n3-Para hexadecimal')
conv = int(input('Qual será a base de conversão:'))
if conv == 1:
    print('O número {} convertido para BINÁRIO É {}.'.format(n1, bin(n1)[2:]))
elif conv == 2:
    print('O número {} convertido para OCTAL é {}.'.format(n1, oct(n1)[2:]))
elif conv == 3:
    print('O número {} convertido para HEXADECIMAL é {}.'.format(n1, hex(n1)[2:]))
else:
    print('Opção Inválida')
