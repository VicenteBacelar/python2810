import numpy as np

# Criando um array Numpy (vetor)
arr = np.array([1, 2, 3, 4, 5])

print('Array Numpy: ')
print(arr)

# Operacoes matematicas em arrays
print('\n Array multiplicando por 2:')
print(arr * 2)

# Operação entre arrays
arr2 = np.array([10, 20, 30, 40, 50])
print('\nSomando duas arrays: ')
print(arr + arr2)

# Criando uma matriz (2D)
Matriz = np.array([[1,2,3],[4,5,6]])
print('\nMatriz 2 x 3: ')
print(Matriz)

# Soma e media da matriz
print('\nSoma de todos os elementos da matriz')
print(np.sum(Matriz))

print('\nMédia dos elementos da Matriz')
print(np.mean(Matriz))

# Transposta da Matriz
print('\nMatriz transposta: ')
print(Matriz.T)

# Gerando numeros aleatorios
print('\nNumeros aleatorios entre 0 e 1: ')
print(np.random.rand(3,3))   # Gera uma matriz de 3 x 3 com valores aleatorios

