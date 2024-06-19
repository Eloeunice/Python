# desafio 053- Crie um programa que leia uma frase qualquer e diga se ela é um palindromo
# (de tras pra frente é igual),
#desconsiderando os espaços:')
# obter uma entrada
frase = str(input('Digite uma frase:').strip().upper())
#fazer uma lista com as palavras da frase
palavras = frase.split()
#juntar todas as letras em espaço
junto = "".join(palavras)
#criar a frase inversa
inverso = ''
#ler a frase de trás pra frente
for letra in range(len(junto)-1, -1, -1):#começa do começo, vai até o fim lendo de trás pra frente
    inverso += junto[letra]
if inverso == junto:
    print('TEMOS UM PALÍNDROMO')
else:
    print("ISSO NÃO É UM PALÍNDROMO")

