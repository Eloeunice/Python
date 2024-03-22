print('Vamos ver a sua situação para a aprovação do empréstimo.')
p = float(input('Qual é o valor da casa:'))
s = float(input('Quanto você ganha:'))
y = int(input('Em quantos anos você pretende pagar:'))
m = 12 * y
pm = p / m
ss = 0.3 * s
print('O valor da prestração mensal é de:R${:2f}.'.format(pm))
if pm > ss:
    print('O valor da prestação mensal excede 30% ou mais do seu salário. O EMPRÉSTIMO FOI NEGADO.')
