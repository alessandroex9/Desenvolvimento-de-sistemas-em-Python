import numpy as np

data = np.random.randn(2, 3)
print(data)

print(data * 10)

print(data + data)
print(data.shape)
print(np.zeros(5))

#Indexação e Fatiamento

arr = np.arange(10)
arr

print(arr[6])

print(arr[5:8])

#Array bidimensional, uma matriz, consultamos linha, coluna
print(data[1][0])

#Matriz transposta
print(data.T)

#Funções universais

#Raiz Quadrada
np.sqrt(arr)

#Exponencial
np.exp(arr)

data2 = np.random.rand(2, 3)
print(data2)

data3 = np.maximum(data, data2)
print(data3)

print(data3.sun())
print(data3.mean())
print(data3.cumprod())

#Ordenando
data.sort()
print(data)