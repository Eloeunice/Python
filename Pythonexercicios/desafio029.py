vel = int(input('Qual é a velocidade do seu carro:'))
km = vel - 80
mult = 7 * km
if vel > 80:
    print('Você foi multado! A multa vai custar R$7 por cada km acima do limite.')
    print('O valor total da sua multa é: R${}'.format(mult))
else:
    print('Está tudo certo com sua velocidade.Sem penalidades')
