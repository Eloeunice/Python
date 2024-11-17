import random
n = random.randint(1, 5)
print('Eu pensei em um número de 1 a 5. Você quer tentar adivinhar qual é?')
n1 = int(input('Tente adivinhar:')) #estava dando errado porque eu esqueci de colocar o int
print(n)
if n == n1:
    print("Parabéns!Você venceu.")
else:
    print("Que pena, você perdeu")


