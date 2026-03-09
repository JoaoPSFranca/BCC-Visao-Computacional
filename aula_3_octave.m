pkg load image

n1 = imread("Banco_Imagens/Banda_ETM+1.tif");
n2 = imread("Banco_Imagens/Banda_ETM+2.tif");
n3 = imread("Banco_Imagens/Banda_ETM+3.tif");
n4 = imread("Banco_Imagens/Banda_ETM+4.tif");
n5 = imread("Banco_Imagens/Banda_ETM+5.tif");
n7 = imread("Banco_Imagens/Banda_ETM+7.tif");

BGR123 = cat(3, n3, n2, n1);

BGR124 = cat(3, n4, n2, n1);
BGR125 = cat(3, n3, n2, n5);
BGR127 = cat(3, n3, n2, n7);

BGR234 = cat(3, n2, n3, n4);
BGR345 = cat(3, n3, n4, n5);
BGR243 = cat(3, n2, n4, n3);

figure, imshow(BGR123), title('BGR123');
figure, imshow(BGR124), title('BGR124');
figure, imshow(BGR125), title('BGR125');
figure, imshow(BGR127), title('BGR127');
figure, imshow(BGR234), title('BGR234');
figure, imshow(BGR345), title('BGR345');
figure, imshow(BGR243), title('BGR243');

# figure, imshow([BGR124 BGR125 BGR127]);
# figure, imshow([BGR234 BGR345 BGR243]);
