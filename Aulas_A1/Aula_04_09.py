import numpy as np
import pandas as pd
 
lista_1 = [1,2,3,4,5]
lista_2 = ["I", "II", "III", "IV", "V"]

dicionario_1 = {"I":1, "II":2, "III":3, "IV":4, "V":5}

ndarray_1 = np.array(lista_1)

print(lista_1)
print(lista_2)
print(dicionario_1)
print(ndarray_1)
print("#"*60)

ser_1 = pd.Series(lista_1)
print("\nLista 1:", ser_1, sep="\n")

ser_1 = pd.Series(lista_2)
print("\nLista 2:", ser_1, sep="\n")

#Relembrando é viver, ou não
print("\nSer Shape: ", ser_1.shape)
print("\nSer Values: ", ser_1.values)
print("\nSer Index: ", ser_1.index)

ser_1 = pd.Series(lista_1, lista_2)
print("\nLista 1 e Lista 2:", ser_1, sep="\n")

ser_1 = pd.Series(dicionario_1)
print("\nDicionario 1:", ser_1, sep="\n")

ser_1 = pd.Series(ndarray_1, lista_2)
print("\nNDarray 1:",ser_1, sep="\n")

ser_1 = pd.Series(ndarray_1, lista_2)
print("\nNDarray 1 e Lista:", ser_1, sep="\n")

print("\nNumpy para lista", ndarray_1.tolist())
print("\nSer para Numpy", ser_1.to_numpy())
print("\nSer oara Lista: ", ser_1.tolist())

print("#"*60)

#Acesando os elementos
print("\nAcessando os elementos: ", ser_1[:3],sep="\n")
print("\nAcessando os elementos: ", ser_1.head(3),sep="\n")

print("\nAcessando os elementos: ", ser_1.tail(3),sep="\n")
print("\nAcessando os elementos: ", ser_1[-3:],sep="\n")

print("\nAcessando via rótulo:",ser_1[0])
print("\nAcessando via rótulo:",ser_1["I"])

print("\nIndex Max: ", ser_1.idxmax())
print("Index Min: ", ser_1.idxmin())

ser_1 = pd.Series(lista_1)

print("\nLOC:", ser_1.loc[0:3],sep="\n")
print("\nILOC:", ser_1.iloc[0:3],sep="\n")

dicionario_2 = {"I":10, "II":42, "III":7, "IV":1_000_000}
dicionario_3 = {"I":1, "II":12, "III":13, "V":0}

ser_2 = pd.Series(dicionario_2)
ser_3 = pd.Series(dicionario_3)

print("\nDicionario 2:", ser_2, sep="\n")
print("\nDicionario 3:", ser_3, sep="\n")
