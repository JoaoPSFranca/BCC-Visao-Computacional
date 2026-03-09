pkg load image

imtif = imread('Banco_Imagens/IMG_0080_5.tif');
figure, imshow(imtif), colorbar();
imwrite(imtif, 'Banco_Imagens/img_teste.jpg');

img_cor = imread('Banco_Imagens/cores.jpg');
figure, imshow(img_cor), colorbar();

r = (img_cor(:,:,1));
g = (img_cor(:,:,2));
b = (img_cor(:,:,3));

figure, imshow([r g b]);

rgb = cat(3, r, g, b);
figure, imshow(rgb);

