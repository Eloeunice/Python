print('Bem vindo a Copiadora da Eloiza Eunice')

# VARIAVEIS QUE VÃO ARMAZENAR OS DADOS PARA CALCULO FINAL DO VALOR DO SERVIÇO
preco = 0
pagina = 0
adicional = 0
desc = 0
extra = 0


# FUNÇÃO EM QUE O USUÁRIO ESCOLHE O SERVIÇO DA COPIADORA
def escolha_servico():
    global servico
    global preco
    while True:
        servico = input('''Entre com o tipo de serviço desejado
DIG- Digitalização
ICO - Impressão Colorida
IPB - Impressão Preto e Branco
FOT - Fotocópia
>>''').upper()
        if servico not in ['DIG', 'ICO', 'IPB', 'FOT']:
         print('Serviço Inválido. Tente Novamente.')
         print()
         continue
        break

    if servico == 'DIG':
        preco = 1.10
    elif servico == 'ICO':
        preco = 1.00
    elif servico == 'IPB':
        preco = 0.40
    else:
        preco = 0.20
    return servico


# FUNÇÃO QUE GUARDA O NUMERO DE PAGINAS
def num_paginas():
    global pagina
    global desc
    while True:
        try:
            pagina = int(input('Entre com o número de páginas:'))
            if 20 <= pagina < 200:
                desc = 0.15
            elif 200 <= pagina < 2000:
                desc = 0.2
            elif 2000 <= pagina < 20000:
                desc = 0.25
            elif pagina > 20000:
                print('Não aceitamos tantas páginas de uma vez.\n Por favor, entre com o número de páginas novamente.')
                continue
            else:
                desc = 0
            pagina = pagina - (pagina * desc)  # APLICA O DESCONTO ENCIMA DO NÚMERO DAS PAGINAS
            break
        except ValueError:
            print('Valor inválido. Por favor, entre com um número de páginas válido.')


# FUNÇÃO QUE ARMAZENA O SERVIÇO ADICIONAL (CASO HAJA)
# noinspection PyPep8
def servico_extra():
    global extra
    while True:
        adc = int(input('''Deseja adicionar algum serviço?
        1 - Encadernação simples - R$15.00
        2 - Encadernação capa dura - R$40.00
        0 - Não desejo mais nada
        >>'''))
        if adc not in [0, 1, 2]:
            print('Opção inválida. Por favor, escolha uma opção válida.')
            continue
        if adc == 1:
            extra = 15.00
        elif adc == 2:
            extra = 40.00
        break


# CHAMANDO A FUNÇÃO
escolha_servico()
num_paginas()
servico_extra()

# ARMAZENANDO E MOSTRANDO O VALOR TOTAL DO SERVIÇO
total = (preco * pagina) + extra
print(f'Total: R${total}. (Serviço: {preco} * Páginas: {pagina} + Extra: {extra})')
