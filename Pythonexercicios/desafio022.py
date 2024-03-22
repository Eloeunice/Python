nome = str(input('Qual é o seu nome?')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(" "))
nomed = nome.split()
print(len(nomed[0]))
#tá contando os espaços
