pkg load image

imfinfo("Banco_Imagens/pout.tif");

img = imread("Banco_Imagens/pout.tif");
figure, imshow(img)

amoastra = img(10:20,10:20);

img2 = img;
img2(10:50,10:50) = 0;
figure, imshow(img2);

img2(:,1:50) = 0;
figure, imshow(img2);colorbar()
title('Imagem em tons de cinza');
xlabel('Eixo x');
ylabel('Eixo y');

[lin, col] = size(img);
disp('O número de linhas é:');
disp(' ');
disp(lin);

save('myworkspace.m');

max(img(:));
min(img(:));

