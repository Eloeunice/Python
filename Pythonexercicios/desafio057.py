# DES 057 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado.
# Peça a digitação novamente até ter o valor correto.
while True:
    sexo = input('Qual o seu sexo(F/M)?').upper()
    if sexo != 'F' and sexo != 'M':
        continue
    else:
        break
