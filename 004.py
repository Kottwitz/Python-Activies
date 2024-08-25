print('Programa de leitura de analise de dados de uma tupla')

#Declaracao de Variaveis

c = 0
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro Numero:'))
n3 = int(input('Digite outro Numero:'))
n4 = int(input('Digite outro Numero:'))
t1 = (n1, n2, n3, n4)

#Leitura de Dados da Tupla

print(f'O numero 9 aparece {t1.count(9)} vezes.')
if 3 in t1:
    print(f'O primeiro 3 aparece na {t1.index(3)+1} posicao.')
else:
    print('O valor 3 Nao foi digitado')
if n1 % 2 == 0:
    c = c + 1
if n2 % 2 == 0:
    c = c + 1
if n3 % 2 == 0:
    c = c + 1
if n4 % 2 == 0:
    c = c + 1
print(f'A quantidade de Numeros pares sao {c} numeros')
