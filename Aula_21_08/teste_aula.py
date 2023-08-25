import numpy as np
import documentation_module as dm

'''
array_1 = np.array([1,2,3,4,5])
array_2 = np.array([2,4,6,8,10])
array_3 = np.arange(100)

# Encontrar os valores comuns entre dois vetores
def valores_comuns(array1, array2):
    intersection = np.intersect1d(array_1, array_2)
    return intersection
print(valores_comuns(array_1, array_2))


# Em um vetor com 1000 elementos (0-99), inverta os valores de 42 até 66
def inverte_valores(array):
    array[(array>41) & (array<67)] *= -1
    return array
print(inverte_valores(array_3))


# Encontre o elemento de um vetor mais próximo de um dado valor
def encontrar_mais_proximo(array, valor):
    indice_elemento = np.abs(array - valor).argmin()
    return array[indice_elemento]
print(encontrar_mais_proximo(array_2, 7))
'''

print(dm.juros_simples(10000, 15.18, 12))
print(dm.juros_compostos(10000, 15.18, 12))

help(dm)