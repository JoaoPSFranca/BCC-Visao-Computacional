import numpy as np
import skimage.io as io
from skimage.util import img_as_ubyte

# Variáveis para mudar facilmente
mask_size = 3
sigma = 0.5

# cria uma nova borda copiando os valores das bordas
def edge_padding(img_path):
    img = io.imread(img_path)
    img_8bit = img_as_ubyte(img)
    rows, cols = img_8bit.shape

    pad = int((mask_size - 1) / 2)

    # Cria uma matriz com linhas e colunas
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

    return img_8bit

def filtro_media(img):
    img2 = img.copy()



if __name__ == '__main__':
    print('PyCharm')
