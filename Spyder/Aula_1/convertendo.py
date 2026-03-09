import numpy as np # as imagens são lidas como numpy arrays
from matplotlib import pyplot as plt # é preciso chamar os submódulos
#import matplotlib.pyplot as plt = outra maneira de fazer!
from skimage import io, img_as_float, img_as_ubyte, img_as_uint, color
import skimage
from skimage.exposure import histogram
import cv2
import os

imagem = io.imread('coins.png') # Transforma em uma numpy array

# Obtendo informação sobre a imagem
print('Tipo:',type(imagem)) # classe do objeto
print('Tipo de dado:',imagem.dtype) # tipo = float, uint8, uint32
print('Dimensões:',imagem.shape) # dimensões row, col, dim
print('Mínimo, máximo e média:',imagem.min(), imagem.max(), imagem.mean())

def imprimeInfo(img):
    print(f'Classe do objeto: {type(img)}')
    print(f'Tipo de dado: {img.dtype}')
    print(f'Dimensões: {img.shape}')
    print(f'Mínimo, máximo e média: {img.min(), img.max(), img.mean()}')

imprimeInfo(imagem)

""" Para mostrar figuras em uma janela em separado: Ferramentas/Preferências/iPython console
e selecionar automatic na guia gráficos """

plt.figure(figsize=(5,5)) # o tamanho da figura é dado em polegadas
# se não for especificado, a função usa o tamanho padrão do ambiente computacional
plt.imshow(imagem,cmap='gray')
""" ATENÇÃO! 
A função plt.imshow apenas configura o que será exibido. É necessário
usar plt.show() para de fato exibir o gráfico/imagem na janela. Em alguns
ambientes como Spyder ou Jupyter isso não é necessário """
plt.xlabel('Fotografia de moedas'); 
plt.title('Exemplo de imagem monocromática', fontsize=10)
plt.colorbar();  
plt.show()

print(imagem[0:10,0:10])

# Alterando valores
# imagem_copy = imagem isso não funciona no Python, é como se as duas variáveis
# apontassem para o mesmo objeto. Tem que usar o módulo copy
imagem_copy = np.copy(imagem)
imagem_copy[0:50,0:50]=0
plt.figure()
plt.imshow(imagem_copy,cmap='gray')
plt.colorbar()
plt.show()

hist, hist_centers = histogram(imagem) # histograma da imagem. 
"""hist_centers são os centros dos bins.
Para imagens do tipo int, cada tom de cinza é seu próprio bin."""

plt.figure()
plt.plot(hist_centers,hist,label='Histograma')
plt.grid('on')
plt.legend() # Usa o label do plot como texto
plt.show()

cdf = np.cumsum(hist) / hist.sum()
imprimeInfo(cdf)
plt.figure()
plt.plot(cdf,label='Hist. acumulado')
plt.grid('on')
plt.legend()
plt.show()