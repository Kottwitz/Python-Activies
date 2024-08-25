print('Programa Leitura de um numero por extenso')

#Declarando os numeros de 0 a 20 por extenso em uma tupla

numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'dessesete', 'dezoito',
          'dezenove', 'vinte')

#Estrutura For para ler o numero digitado pelo usuario na tupla
for c in range(0, len(numero)):
    c = int(input('Digite um numero de 0 a 20:'))

    #Estrutura de condicao if para checar se o numero esta entre 0 e 20

    if c < 0 or c > 20:

        #Estrutura de repeticao while para fazer o usuario digitar um numero entre 0 e 20

        while c < 0 or c > 20:
            c = int(input('Tente Novamente digite um numero entre 0 e 20:'))
        print(f'Voce Digitou {numero[c]}')
        break
    else:
        print(f'Voce Digitou {numero[c]}')
        break

