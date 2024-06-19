lista_livro = []
id_global = 0

print('Bem vindo a Livraria da Eloiza Eunice')
print('-' * 38)


# Função que pede as informações para o cadastro do livro


def cadastrar_livro(id_global):
    id_global += 1
    print('-' * 38)
    print('          MENU CADASTRAR LIVRO  ')
    print(f'Id do Livro:{id_global}')

    nome = input('Entre com o nome do livro:')
    autor = input('Entre com o autor do livro:').lower()
    editora = input('Entre com a editora do livro:')

    dict_livro = {'id': id_global, 'Nome': nome, 'Autor': autor, 'Editora': editora}
    (lista_livro.append(dict_livro))  # Coloca as informações do livro cadastrado dentro da lista de livros

# FUNÇÃO QUE FAZ A CONSULTA DOS LIVROS


def consultar_livro():
    while True:
        print('-' * 38)
        print('       MENU CONSULTAR LIVRO')
        try:
            consulta = int(input('''Escolha a opção desejada:
1 - Consultar Todos
2 - Consultar por Id
3 - Consultar por Autor
4- Retornar ao menu
>>'''))
            if consulta not in [1, 2, 3, 4]:
                print('Opção Inválida.')
                continue

            elif consulta == 1:  # Consulta todos
                for dict_livro in lista_livro:
                    print(dict_livro)

            elif consulta == 2:  # Consulta por Id
                id_livro = int(input('Entre com o Id do livro: '))
                livro_encontrado = next((dict_livro for dict_livro in lista_livro if dict_livro['id'] == id_livro),
                                        None)
                if livro_encontrado:
                    print(livro_encontrado)
                else:
                    print("Id Inválido.")

            elif consulta == 3:  # Consulta por autor
                autor_livro = input('Entre com o autor do livro:').lower()
                for dict_livro in lista_livro:
                    if dict_livro['Autor'] == autor_livro:
                        print(dict_livro)

            else:  # Retorna
                break
        except ValueError:
            print('Valor inválido')

        print(op_menu_principal)

# FUNÇÃO QUE REMOVE OS LIVROS


def remover_livro():
 while True:
    try:
     id_livro = int(input('Entre com o Id do livro que você deseja remover: '))
     livro_encontrado = next((dict_livro for dict_livro in lista_livro if dict_livro['id'] == id_livro), None)
     if livro_encontrado:
        lista_livro.remove(livro_encontrado)
        print('O livro foi removido com sucesso.')
     else:
        print("Id Inválido.")
        continue
     break
    except ValueError:
     print('Valor inválido.')


# ESSE É O MENU PRINCIPAL
# Ele é colocado no fim do programa para reconhecer todas as funções e variáveis


while True:
    try:
        print()
        op_menu_principal = int(input('''       MENU PRINCIPAL 
Escolha a opção desejada:
1 - Cadastrar Livro
2 - Consultar livro(s)
3- Remover Livro
4 - Sair
>>'''))
        if op_menu_principal == 1:
            cadastrar_livro(id_global)
            id_global += 1

        elif op_menu_principal == 2:
            consultar_livro()

        elif op_menu_principal == 3:
            remover_livro()

        elif op_menu_principal == 4:
            break
    except ValueError:
        print("Opção Inválida.Tente Novamente.")
