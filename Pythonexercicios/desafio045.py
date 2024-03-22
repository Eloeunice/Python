import random
# tinha escolhido a função errada do módulo, mas a lógica estava certa.
print('Vamos jogar jokenpô!')
p1 = int(input('1-Pedra\n2-Papel\n3-Tesoura\n Escolha uma das opções:'))
itens = ('Pedra', 'Papel', 'Tesoura')
cp = random.randint(1, 3)
print('Eu escolhi {}.'.format(itens[cp]))
if p1 == 1 and cp == 3:
    print('VOCÊ GANHOU!')
elif p1 == 2 and cp == 1:
    print('VOCÊ GANHOU!')
elif p1 == 3 and cp == 2:
    print('VOCÊ GANHOU')
elif p1 == cp:
    print('EMPATAMOS')
else:
    print('VOCÊ PERDEU')

#pedra ganha de tesoura e perde de papel
#papel ganha de pedra e perde de tesoura
#tesoura ganha de papel e perde de pedra
