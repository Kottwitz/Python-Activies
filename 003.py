print('Programa Colocando numeros aleatorios em Tuplas')

#importa a Biblioteca Random

import random
from random import randint

#atribuicao das variaveis

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)
n4 = random.randint(1, 10)
n5 = random.randint(1, 10)
t1 = (n1, n2, n3, n4, n5)

#comandos para exibicao dos resultados

print(f'os numeros sorteados foram{t1}')
print(f'o maior numero foi {max(t1)}')
print(f'E o menor foi {min(t1)}')
