import numpy as np
import numpy.random as npr

'''
#Operações em NDArrays
print("#"*40)

a1D_1 = np.arange(10)
print(a1D_1, end="\n\n")

#OBS: o reshape é um módulo, não uma função, por isso ele deve ser invocado no objeto.
#a1D_1 = a1D_1.reshape(3,2) ERRO!
a1D_1 = a1D_1.reshape(5,2)
print(a1D_1, end="\n\n")

a1D_1 = a1D_1.transpose()
print(a1D_1, end="\n\n")

print("#"*40)

a1D_2 = np.arange(20)
print(a1D_2, end="\n\n")

a1D_2 = a1D_2.reshape(10,2)
print(a1D_2, end="\n\n")

#Empilha um enbaixo do outro
a1D_3 = np.vstack((a1D_2,a1D_2))
print(a1D_3, end="\n\n")

#Empilha um do lado do outro
a1D_3 = np.hstack((a1D_2,a1D_2))
print(a1D_3, end="\n\n")

print(f"Dados sobre a1D_3:\n\tDimensão: {a1D_3.ndim}\n\t\
Forma: {a1D_3.shape}")

print("#"*40)

#Shallow Copy
a1D = np.arange(10)
print(a1D)

a1D_copy = a1D
print(a1D_copy)

a1D_copy[0] = 42
print(a1D)
print(a1D_copy)

print(id(a1D))
print(id(a1D_copy))

#Deep Copy
a1D = np.arange(10)
print(a1D)

a1D_copy = a1D.copy()
print(a1D_copy)

a1D_copy[0] = 42
print(a1D)
print(a1D_copy)

print(id(a1D))
print(id(a1D_copy))

print("#"*40)

#Retornos de funções: Shallow x Deep

outro_vetor = a1D.reshape(5,2)
outro_vetor[0,0] = 42
print(a1D)
print(outro_vetor)
'''

a = np.zeros((7,6))
print(a)

b = np.ones((7,6))
print(b)

c1 = np.diag([1,1,1,1,1])
print(c)
c2 = np.eye(5)
print(c2, end="\n")

d = np.arange(7, 43)
print(d)

e = np.arange(8, 43, 2)
print(e)

f = npr.rand(1)
print(f)

g = npr.rand(10)
print(g)

h = np.ones(10) * 42
print(h)

i = np.arange(1,10).reshape(3,3)
print(i)