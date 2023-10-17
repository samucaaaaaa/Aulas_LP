import math
import numpy as np
import numpy.random as npr

"""
#Broadcasting
lista_a = [1,2,3]
lista_b = [4,5,6]

a1D_a = np.array([1,2,3,4])
a1D_b = np.array([0,1,2,3])

#OPERAÇÕES BÁSICAS#
#print(lista_a * lista_b) - ERRO
print(a1D_a * a1D_b)

print(a1D_a * 3)
print(lista_a * 3)

#print(lista_a + 3) - ERRO
print(a1D_a + 3)

#print(lista_a - 3) - ERRO
print(a1D_a - 3)

#print(lista_a ** 3) - ERRO
print(a1D_a ** 3)

#print(lista_a / 3) - ERRO
print(a1D_a / 3)

print(a1D_a / 0)
print(a1D_b / 0)

print(a1D_a / a1D_b)
print("#"*80)

#Produtos entre NDArrays
a1D_a = a1D_a.reshape(1,4)
a1D_b = a1D_b.reshape(4,1)
print(a1D_a)
print(a1D_b)
print(a1D_a*a1D_b)
print("#"*80)

#Bagulho doido
ndarray = np.array([1,2,3,4,5,6])
indices = ndarray>3
print(indices)
print(ndarray[indices])

indices = (ndarray%2 == 0)
print(indices)
print(ndarray[indices])
print("#"*80)
"""

"""
ndarray = np.arange(9).reshape(3,3)
indices = np.array([[False, True, False], [True, False, True], [True, False, True]])
print(ndarray)
print(indices)

print(ndarray[indices])
print("#"*80)
"""

"""
#Breaking Bad
notas = np.array([87, 72, 95, 93, 70, 100])

#Average(média)
print("Average: ", np.average(notas))

#Median(mediana)
print("Median: ", np.median(notas))

#Standard Deviation(desvio padrão)
print("Standard Deviation: ", np.std(notas))

#Percentile(percentil)
print("Percentile: ", np.percentile(notas))

#Minimun e Maximun(máximo e mínimo)
print("Minimun e Maximun: ", np.amax(notas), "e", np.amin(notas))

#Peak to peak(distância entre o máximo e o mínimo)
print("Peak to peak: ", round(np.ptp(notas), 2))
"""

#Exercício

matriz = np.array([1,2,3,4], [5,6,7,8])

def erro_absoluto(valor_estimado, valor_obs):
    erro_medio_absoluto = np.sum(valor_estimado - valor_obs)/len(valor_estimado)
    return erro_medio_absoluto

def erro_quadratico(valor_estimado, valor_obs):
    erro_quadratico = (valor_estimado - valor_obs)**2
    erro_medio_quadratico = np.sum(erro_quadratico)/len(valor_estimado)
    
def dados_gerais()   