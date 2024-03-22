#US1,00=RS3,27
real = float(input('Dinheiro na carteira:R$'))
#3,27 compra 1 dólar, real compra quantos?
dolar = float(4.86)
t = float(real/dolar)
print('Com R${}, você pode comprar U${:.2f}'.format(real, t))