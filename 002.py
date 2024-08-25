print('Programa Times do Brasileirao 2023')

#Leitura dos times em uma tupla na ordem de colocacao

times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
        'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
         'Vasco', 'Bahia','Santos', 'Goiás', 'Coritiba', 'América-MG')

#Comandos para exibicao dos resultados

print(f'os 5 primeiros times sao {times[0:5]}')
print(f'os qutro ultimos sao{times[-4:]}')
print(f'os times em ordem alfabetica ficam{sorted(times)}')
print(f'o Flamengo esta na {times.index('Flamengo')+1}ª colocacao')