dias = int(input('Quantos dias alugados:'))
km = float(input('Quantos Km rodados:'))
#60 reais por dia e 0,15 por km
t = dias*60+km*0.15
print('O valor total a pagar é de R${}'.format(t))