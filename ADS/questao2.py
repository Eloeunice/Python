
print("Bem-vindo a loja de Gelados da Eloiza Eunice")
print("              CARDÁPIO                       ")

print('''
| TAMANHO | Cupuaçu (CP) | Açaí (AC) |
|    P    |  R$ 9.00     | R$ 11.00  |
|    M    |  R$ 14.00    | R$ 16.00  |
|    G    |  R$ 18.00    | R$ 20.00  |
''')

total = 0  # variavel acumuladora
while True:  # laço externo
    sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
    while sabor != 'CP' and sabor != 'AC':  # laço para a verificação da entrada do sabor
        print('Sabor inválido. Tente novamente.')
        print()
        sabor = input('Entre com o sabor desejado (CP/AC): ').upper()

    tam = input('Entre com o tamanho desejado (P/M/G): ').upper()
    if tam != 'P' and tam != 'M' and tam != 'G':
        print('Tamanho inválido. Tente novamente.')
        print()
        continue  # volta lá para o inicio do programa caso o tamanho esteja incorreto
    break  # se estiver tudo certo, ele encerra esse laço e continua com o programa

# IMPLEMENTAÇÃO DE ESTRUTURAS DE CONDIÇÃO COM AS COMBINAÇÕES DE SABOR E TAMANHO
if sabor == 'CP':
    nome = 'Cupuaçu'
    if tam == 'P':
        preco = 9.00
    elif tam == 'M':
        preco = 14.00
    else:
        preco = 18.00

if sabor == 'AC':
    nome = 'Açaí'
    if tam == 'P':
        preco = 11.00
    elif tam == 'M':
        preco = 16.00
    else:
        preco = 20.00

total += preco  # acumulando o valor do pedido na variável
print(f'Você pediu um {nome} no tamanho {tam}: R${preco}')
print()

# PEDIDO A MAIS
mais = input('Deseja mais alguma coisa? (S/N):').upper()
if mais == 'S':  # caso o usuário deseje acrescentar mais coisas, o laço para o pedido repete
      while True:
        sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
        while sabor != 'CP' and sabor != 'AC':  # laço para a verificação da entrada do sabor
            print('Sabor inválido. Tente novamente.')
            print()
            sabor = input('Entre com o sabor desejado (CP/AC): ').upper()

        tam = input('Entre com o tamanho desejado (P/M/G): ').upper()
        if tam != 'P' and tam != 'M' and tam != 'G':
            print('Tamanho inválido. Tente novamente.')
            print()
            continue  # volta lá para o inicio do programa caso o tamanho esteja incorreto
        break  # se estiver tudo certo, ele encerra esse laço e continua com o programa

      if sabor == 'CP':
        nome = 'Cupuaçu'
        if tam == 'P':
         preco = 9.00
        elif tam == 'M':
         preco = 14.00
        else:
         preco = 18.00

      if sabor == 'AC':
        nome = 'Açaí'
        if tam == 'P':
         preco = 11.00
        elif tam == 'M':
         preco = 16.00
        else:
         preco = 20.00
      print(f'Você pediu um {nome} no tamanho {tam}: R${preco}')

total += preco
print(f'O valor total a ser pago: R${total}')
