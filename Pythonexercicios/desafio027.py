nome = str(input('Digite seu nome completo:')).strip()
print('Muito prazer em te conhecer!')
nomed = nome.split()
print('Seu primeiro nome é: {}'.format(nomed[0]))
print('Seu último nome é:{}'.format(nomed[len(nomed)-1]))
#ele conta quantos tem na lista e mostra o "-1" que é o último nome.