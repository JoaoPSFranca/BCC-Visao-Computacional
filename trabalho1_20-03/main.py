import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Lendo a Imagem
brute_img = io.imread('IMG_0080_5.tif').astype(np.float32)
b_img = brute_img.copy()

# Constantes da banda 5
ISO = 800
gain = ISO / 100
te = 1.5
blackLevel = 4800

# Coeficientes radiométricos
a1 = 0.00036494025950395686
a2 = 8.8666518209275022e-08
a3 = 1.4911493946260918e-05

# Parâmetros do centro óptico
cx = 697.57412520205469
cy = 483.3379020042467

# Polinômio do Vignetting
k0 = -0.00011488197737851787
k1 = 1.183167572859751e-06
k2 = -1.171867123703797e-08
k3 = 3.3530562168475598e-11
k4 = -4.1718260305381848e-14
k5 = 1.8823938615703626e-17

# Normalização [0, 1]
p = brute_img / 65535.0
p_bl = blackLevel / 65535.0

# Cria a grid
rows, cols = brute_img.shape
x, y = np.meshgrid(np.arange(cols), np.arange(rows))

# Distancia Radial
r = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)

# Polinomio de correcao
k = 1 + (k0 * r) + (k1 * r ** 2) + (k2 * r ** 3) + (k3 * r ** 4) + (k4 * r ** 5) + (k5 * r ** 6)

# Vignetting
V = 1.0 / k

# Calculo da Radiância
denominador = te + (a2 * y) - (a3 * te * y)
L = V * (a1 / gain) * ((p - p_bl) / denominador)

# Limites da imagem
L_min = L.min()
L_max = L.max()

L_norm = 255.0 * (L - L_min) / (L_max - L_min)
L_final = np.clip(L_norm, 0, 255).astype(np.uint8)

io.imsave('Radiancia_Banda5.tif', L_final, check_contrast=False)

# Parece que está mostrando a mesma imagem por algum motivo
# Mas olhando o arquivo gerado e o arquivo original, estão diferente
# Então real não sei

# # Exibe a Imagem Final
# plt.figure(figsize=(15, 5))
#
# plt.subplot(1, 2, 1)
# plt.imshow(b_img, cmap='gray')
# plt.title('Imagem Original', fontsize=10)
# plt.axis('on')
#
# plt.subplot(1, 2, 2)
# plt.imshow(L_final, cmap='gray')
# plt.title('Imagem Final', fontsize=10)
# plt.axis('on')
#
# plt.show()