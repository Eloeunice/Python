# DES 058 Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora
# o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pc = randint(1, 10)
palp = 0
print('Eu pensei em um número de 1 a 10. Você quer tentar adivinhar qual é?')
acertou = False
while not acertou:
    palp += 1
    user = int(input('Tente adivinhar:'))
    if pc == user:
        acertou = True
        print(f'VOCÊ ACERTOU!Eu pensei em {pc}')
        break
print(f'Você precisou de {palp} palpites para acertar.')
