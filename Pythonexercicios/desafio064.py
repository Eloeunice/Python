# DES 064 que leia vários numeros inteiros pelo teclado.
# # O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# # No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o 'flag)
qnt = 0
sum = 0
num = int(input("Digite um número inteiro:"))
while num != 999:
    qnt += 1
    sum += num
    num = int(input("Digite um número inteiro:"))

print(f'Você digitou {qnt} números e a soma deles é {sum}.')

