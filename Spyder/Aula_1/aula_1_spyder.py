import numpy as np

# definindo lista
a = [1, 2, 3, 4, 5]

# em um array numpy todos os valores sao do mesmo tipo
b = np.array(a)
c = b * 2
print(c)

# array bidimensional
d = np.array([[1,2,3],[4,5,6]])
print(d)
print(d[0,0])

# imprimindo o tipo de dado
print(type(d))

# imprimindo o tipo de dado
print(d.dtype)

# convertendo entre tipos de dados
# d é do tipo int64, convertendo para uint8
d_uint8 = d.astype(np.uint8)
print(d_uint8.dtype)

e = np.array([-10, -1, 0, 100, 255, 256, 257, 300, 500])
e_uint8 = e.astype(np.uint8)
print(e_uint8.dtype)
print(e_uint8)

e_uint8 = np.clip(e, 0, 255).astype(np.uint8)
print(e_uint8)

f = np.array([-10, -1, 0, 100, 255, 256, 257, 300, 500])
g = f + abs(f.min())
print(e)

escala = 255/e.max()
f = f * escala


print(np.info(np.int32))

# Criando uma cópia
d2 = np.array([[1., 2, 3], [4, 5, 6]])
print(d2.dtype)

# Cirando uma matriz de zeros
m = np.zeros((2,2), dtype=float)
print(m)

#Também podemos criar uma matriz preenchida com um determinado valor
n = np.full((2,2),6)
print(n)

# matriz identidade
o = np.eye(3)
print(o)

# usando índices
p = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(p)
print(p[:,0:2])

# alterando valores
p[:,0] = 100
print(p)

# somando valores 
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a + b)

# multiplicando valores
print(a * b)

# divisão
print(a / b)

# matriz transposta
print(a.T)

# pontenciacao
print(a**2)
print(np.power(a, 2))

# radiciacao
print(np.sqrt(a))

# funcoes trigonometricas
tetha = np.deg2rad(45)
print(np.sin(tetha))
print(np.cos(tetha))

