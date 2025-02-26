#lambda
(lambda base, altura: base * altura)(2, 3)


modelos = [
    {'marca':'Mi', 'tela':6.8, 'cor':'Dourada'}
    {'marca':'Iphone', 'tela':6.1, 'cor':'Preta'}
    {'marca':'Samsung', 'tela':7.2, 'cor':'Azul'}
    {'marca':'Nokia', 'tela':5.5, 'cor':'Preta'}
]

#Ordenando a lista

modelos_ordenados = sorted(modelos, key = lambda x: x['marca'])

print(modelos_ordenados)

#Reduzindo a lista
from functools import reduce

maior_tela = reduce(lambda a, b : b['tela'] if b['tela'] > a else a, modelos, 0)

#Filtrando a lista
modelos_cor_preta = filter(lambda x: (x['cor'] == 'Preta'), modelos)
list(modelos_cor_preta)

#Transformando a lista com o map
def descricao(modelo):
    modelo['discricao'] = f"Celular da {modelo['marca']} tem a tela:{modelo['tela']} da cor: {modelo['cor']}"
    return modelo

modelos_discricao = map(lambda x: descricao(x), modelos)
list(modelos_discricao)