km = int(input('Qual a distância da sua viagem:'))
#0,50 por km até 200km
#Acrescentar 0,45 por km depois de t
if km <= 200:
    t = 0.50 * km
    print('O preço da sua passagem é R${}'.format(t))
else:
    t2 = 0.45 * km
    print('O valor da sua passagem é ${}'.format(t2))
