from math import sqrt

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

# sjaeroruido.tif

img_path = "sjaeroruido.tif"

laplace_principal = np.array([[0, -1, 0],
                              [-1, 4, -1],
                              [0, -1, 0]])

laplace_secundario = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]])

def convolucao(img_path, kernel):
    # Lê a imagem
    img = io.imread(img_path)

    # Cria a matriz filtrada
    rows, cols = img.shape
    img_filtered = np.zeros((rows, cols), dtype=np.float16)

    # Itera sobre a imagem ignorando as bordas
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Cria uma submatriz do tamanho da mascara
            subMatrix = img[i - 1: i + 2, j - 1: j + 2]

            # Aplica a função da diagonal principal
            novo_pixel = int(np.sum(kernel * subMatrix))

            # Salva na coordenada original (descontando o pad)
            img_filtered[i, j] = novo_pixel

    return img_filtered


def mostraImagens(tittles=[], imgs=[]):
    nrows, ncols = 0,0

    total = len(imgs)

    c = int(sqrt(total))

    if total / c == c:
        r = c
    elif total % c == 0:
        r = int(total / c)
    else:
        r = int(total / c) + 1

    fig, axes = plt.subplots(r, c, figsize=(12, 10))

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray', vmin=0, vmax=255)
        ax.set_title(tittles[i], fontsize=12)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    img = io.imread(img_path)
    img_d_principal = convolucao(img_path, laplace_principal)
    img_d_secundario = convolucao(img_path, laplace_secundario)
    img_final = img_d_secundario + img_d_principal

    # fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Lista de dados para facilitar o loop de exibição
    tittles = ['Original', 'Diagonal Principal', 'Diagonal Secundária', 'Realce Completo', '1', '2', '3']
    images = [img, img_d_principal, img_d_secundario, img_final, img, img, img]

    mostraImagens(tittles, images)

    # # Itera sobre os eixos e as imagens para plotar
    # for i, ax in enumerate(axes.flat):
    #     ax.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    #     ax.set_title(tittles[i], fontsize=12)
    #     ax.axis('off')
    #
    # plt.tight_layout()
    # plt.show()