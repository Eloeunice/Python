p = float(input('Qual é o preço normal do produto:R$'))
print('1- À vista dinheiro/cheque\n 2-À vista no cartão\n 3-Em até 2x no cartão\n 4-3x ou mais no cartão')
f = int(input('Qual será a forma de pagamento:'))
if f == 1:
    t = p - (0.1 * p)
    print("O valor final do seu produto é:R${}".format(t))
elif f == 2:
    u = p - (0.05 * p)
    print("O valor final do seu produto é:R${}".format(u))
elif f == 3:
    print('O valor do seu produto não muda')
elif f == 4:
    v = p + (0.2 * p)
    print("O valor final do seu produto é:R${}".format(v))
