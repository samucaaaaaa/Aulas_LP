import numpy as np
import numpy.random as npr
import pandas as pd

#Questão 5 dos exercícios
'''
npr.seed(42)
serie_numeros = pd.Series(npr.randint(1, 10, 42))
print("Série: ", serie_numeros, sep="\n")

frequencias = serie_numeros.value_counts()
print("Frequências: ", frequencias, sep="\n")

passo_1 = serie_numeros.value_counts().index[0]
passo_1 = pd.Series(passo_1)
print("Passo 1: ", passo_1, sep="\n")

passo_2 = serie_numeros.isin(passo_1)
print("Passo 2: ", passo_2, sep="\n")

passo_3 = ~passo_2
print("Passo 3: ", passo_3, sep="\n")

serie_numeros[passo_3] = "Desconsiderar"
print("Último passo:", serie_numeros, sep="\n")
'''

# Questão 6 dos exercícios
'''
ser_1 = pd.Series([1,2,3,4,5])
ser_2 = pd.Series([4,5,6,7,8])

print("Série 1: ", ser_1, sep="\n")
print("Série 2: ", ser_2, sep="\n")

serie_uniao = pd.Series(np.union1d(ser_1, ser_2))
print("Série união: ", serie_uniao, sep="\n")

serie_intersecao = pd.Series(np.intersect1d(ser_1, ser_2))
print("Série Interseção; ", serie_intersecao, sep="\n")

passo_1 = serie_uniao.isin(serie_intersecao)
print("Passo 1: ", passo_1, sep="\n")

passo_2 = ~passo_1
print("Passo 2: ", passo_2, sep="\n")

print("\nResultado: ", serie_uniao[passo_2], sep="\n")
'''