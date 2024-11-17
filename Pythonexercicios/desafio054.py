# desafio 054- Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda
#não atingiram a maioridade (21 anos) e quantas já são maiores
from datetime import date
data = date.today().year
me = 0
ma = 0
for p in range(1, 8):
    y = int(input('Em que ano você nasceu:'))
    idade = data - y
    if idade < 21:
     me += 1
    elif idade > 21:
     ma += 1

print("{} pessoas atingiram a maioridade (21 anos)".format(ma))
print('{} pessoas não atingiram a maioridade (21 anos). '.format(me))






