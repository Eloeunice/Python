# Crie um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa mostre: a média de idade do grupo
#o nome do homem mais velho
#quantas mulheres têm menos de 20 anos
#dá pra resolver com dicionário!
total_idade = 0
maior = 0
menor = 0
s = 0
homem = ''
for c in range(1, 5):
    print(f"Pessoa {c}")
    nome = str(input("Nome:"))
    idade = int(input('Idade:'))
    sexo = str(input("Sexo:")).lower()
    total_idade += idade
    media_idade = total_idade / 4
    if sexo == "homem":
        if c == 1:
            maior = c
            homem = c
        else:
            if idade > maior:
                maior = idade
                homem = nome #ver como colocar o nome da pessoa
    if sexo == "mulher":
        if idade < 20:
            s += 1
print(f"A média de idade do grupo é: {media_idade}.")
print(f"O homem mais velho é o {homem} que tem {maior} anos.")
print(f'{s} mulheres têm menos de 20 anos.')


