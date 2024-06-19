print("Bem-vindo a loja da Eloiza Eunice")
valor = float(input("Entre com o valor do produto: R$"))
qtd = int(input("Entre com a quantidade do produto:"))
preco = valor * qtd# variavel calcula o valor da compra

# Se preco for menor que 2500 o desconto será de 0%;
if preco < 2500:
    print("Você não recebeu desconto.")
    print(f"O valor total é: R${preco}.")

# Se preco for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
elif 6000 > preco >= 2500:# condição do programa caso o valor da compra esteja entre 2500 a 6000
    desc = preco * 0.04
    total = preco - desc
    print(f'O valor SEM desconto: R${preco}')
    print(f'O valor COM desconto: R${total}')

# Se preco for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
elif 10000 > preco >= 6000:
    desc = preco * 0.07
    total = preco - desc
    print(f'O valor SEM desconto: R${preco}')
    print(f'O valor COM desconto: R${total}')

# Se preco for igual ou maior que 10000 o desconto será de 11%;
else:
    desc = preco * 0.11
    total = preco - desc
    print(f'O valor SEM desconto: R${preco}')
    print(f'O valor COM desconto: R${total}')

