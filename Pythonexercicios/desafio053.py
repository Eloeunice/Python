# desafio 053- Crie um programa que leia uma frase qualquer e diga se ela é um palindromo
# (de tras pra frente é igual),
#desconsiderando os espaços:')
# obter uma entrada
frase = input('Digite uma frase:')
# remover espaços em branco
frase2 = frase.strip('')
# inverter a sequência de caracteres
frase_invertida = frase.strip('')[::-1]
print(frase_invertida)
# comparar a sequência invertida com a sequência original
# se as duas sequencias forem iguas significa que é um palíndromo
if frase_invertida == frase2:
    print('É um palíndromo')
else:
    print('Não é um palíndromo.')