import random
print('Escreva o nome dos seus alunos a seguir:')
n1 = input('Aluno 1:')
n2 = input('Aluno 2:')
n3 = input('Aluno 3:')
n4 = input('Aluno 4:')
lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)
print('O aluno escolhido para limpar o quadro é: {}'.format(sorteio))



