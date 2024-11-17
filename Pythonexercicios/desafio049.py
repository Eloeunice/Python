# desafio 049- Refaçã o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando o laço for
num = int(input('Digite um valor:'))
for c in range(1, 11):
    print("{} X {}:".format(num, c), end=" ")
    print(num*c)
