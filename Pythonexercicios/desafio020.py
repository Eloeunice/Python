import random
print('Escreva o nome dos seus alunos:')
n1 = input('Aluno 1:')
n2 = input('Aluno 2:')
n3 = input('Aluno 3:')
n4 = input('Aluno 4:')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
st = random.sample(lista, 4)
print('A ordem de apresentação é: {}'.format(st))
