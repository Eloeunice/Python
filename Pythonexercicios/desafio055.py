# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {}° pessoa:".format(p)))
    if p == 1:
        menor = p
        maior = p
    else:
        if peso > maior:
         maior = peso
        if peso < menor:
         menor = peso

print(f'O maior peso foi {maior}KG')
print(f'o menor peso foi {menor}KG')


