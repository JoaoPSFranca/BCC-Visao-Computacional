import numpy as np
import skimage.io as io
from skimage.util import img_as_ubyte
import matplotlib.pyplot as plt

# Variáveis para mudar facilmente
img_path = "gaussian.tif"
mask_size = 3 # Tamanho da mascara
sigma = 0.5
pad = int((mask_size - 1) / 2) # calcula o tamanho da borda

# cria uma nova borda copiando os valores das bordas
def edge_padding(img):
    img_8bit = img_as_ubyte(img)
    rows, cols = img_8bit.shape

    # Cria uma matriz com linhas e colunas do tamanho da imagem + o pad
    new_rows = rows + (2 * pad)
    new_cols = cols + (2 * pad)
    img_padded = np.zeros((new_rows, new_cols), dtype=img.dtype)

    # Centraliza a Imagem na matriz
    img_padded[pad: rows + pad, pad: cols + pad] = img

    # Copia as bordas horizontais (linhas)
    img_padded[0: pad, pad: cols + pad] = img[0, :]
    img_padded[rows + pad: new_rows, pad: cols + pad] = img[-1, :]

    # Copia as bordas verticais (colunas)
    img_padded[pad: rows + pad, 0: pad] = img[:, 0][:, np.newaxis]
    img_padded[pad: rows + pad, cols + pad: new_cols] = img[:, -1][:, np.newaxis]

    # Preenche os 4 cantos
    img_padded[0: pad, 0: pad] = img[0, 0]
    img_padded[0: pad, cols + pad: new_cols] = img[0, -1]
    img_padded[rows + pad: new_rows, 0: pad] = img[-1, 0]
    img_padded[rows + pad: new_rows, cols + pad: new_cols] = img[-1, -1]

    return img_padded

def create_gaussian_mask():
    # Calcula a distância até o centro
    limite = pad

    # Cria uma grade de coordenadas
    x, y = np.meshgrid(np.arange(-limite, limite + 1), np.arange(-limite, limite + 1))

    # Aplica a fórmula
    mask = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))

    # Normaliza a máscara
    mask_normalizada = mask / np.sum(mask)

    return mask_normalizada

gaussian_mask = create_gaussian_mask()

def filter_avg(subMatrix):
    return int(np.mean(subMatrix))

def filter_median(subMatrix):
    return int(np.median(subMatrix))

def filter_gaussian(subMatrix):
    return int(np.sum(gaussian_mask * subMatrix))

def filter_generic(func):
    # Lê a imagem
    img = io.imread(img_path)

    # Cria a matriz filtrada
    original_rows, original_cols = img.shape
    img_filtered = np.zeros((original_rows, original_cols), dtype=np.uint8)

    img_padded = edge_padding(img)
    padded_rows, padded_cols = img_padded.shape

    # Itera sobre a imagem ignorando as bordas
    for i in range(pad, padded_rows - pad):
        for j in range(pad, padded_cols - pad):
            # Cria uma submatriz do tamanho da mascara
            subMatrix = img_padded[i - pad: i + pad + 1, j - pad: j + pad + 1]

            # Aplica a função que tiver no parâmetro
            novo_pixel = func(subMatrix)

            # Salva na coordenada original (descontando o pad)
            img_filtered[i - pad, j - pad] = novo_pixel

    return img_filtered

if __name__ == '__main__':
    img = io.imread(img_path)
    img_avg = filter_generic(filter_avg)
    img_median = filter_generic(filter_median)
    img_gaussian = filter_generic(filter_gaussian)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Lista de dados para facilitar o loop de exibição
    tittles = ['Original', 'Média', 'Mediana', 'Gaussiano (Pesos)']
    images = [img, img_avg, img_median, img_gaussian]

    # Itera sobre os eixos e as imagens para plotar
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
        ax.set_title(tittles[i], fontsize=12)
        ax.axis('off')

    # Ajusta o espaçamento para que as legendas não se sobreponham
    plt.tight_layout()
    plt.show()

    save_gaussian = io.imsave("gaussian_filtered.tif", img_gaussian)
    save_avg = io.imsave("avg_filtered.tif", img_avg)
    save_median = io.imsave("median_filtered.tif", img_median)
