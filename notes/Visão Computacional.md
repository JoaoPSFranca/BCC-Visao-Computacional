
# Conceitos Importantes

A *Radiação Eletromagnética (REM)* pode ser definida como uma onda (tendo comprimento de onda $\lambda$ e frequência $f$) quanto uma partícula (fóton). 

**Irradiância ($E$):** é a intensidade de uma fonte (tipo a luz solar) que incide sobre uma superfície.  Na imagem do domo, é a luz que entra e bate no objeto.

**Radiância ($L$):** é a intensidade de uma fonte que deixa uma superfície por um determinado ângulo. Na imagem do domo, é a luz que reflete do objeto e sai do domo. 

**Reflectância ($\rho$):** é a razão entre a energia refletida e a energia incidente. Basicamente cada alvo tem uma quantidade de energia que pode absorver e, consequentemente, que irá refletir, usamos isso para identificar objetos nas imagens.

**Sensores Ativos:** são sensores que enviam pulsos de energia e geram resultados com base na "resposta" que recebem a esses impulsos. Como exemplo temos os *Lidars* que enviam pulsos de laser para medir distâncias e criar modelos 3D, ou os *Radares* que enviam micro-ondas e medem com base no "eco" que retorna.

**Sensores Passivos:** são sensores que utilizam de fontes naturais de energia, como a reflexão da luz solar. Então eles meio que só observam e não emitem algo de fato.

**Correlação:** É o processo de mover a máscara (filtro de suavização) e calcular a soma dos produtos em cada posição.

**Convolução:** É o mesmo processo, mas a máscara é rotacionada em 180 graus.

# Aulas de Código

## Bibliotecas

- `import numpy as np` - Serve para fazer ações com arquivos no geral. Nesse contexto, ela é importante para transformar a imagem em um `ndarray` e manipulá-la da melhor forma possível.
- `from matplotlib import pyplot as plt` - É a biblioteca padrão para mostrar coisas na tela, como gráficos geralmente. Nesse contexto, utilizamos para mostrar as imagens e os histogramas geralmente.
- `skimage` - Se trata de uma biblioteca de processamento de imagens digitais.
	- `io` - É o responsável pela entrada e saída de dados. 
	- `util, img_as_float, img_as_ubyte` - Convertem a imagem entre tipos de dados.
	- `exposure` (`from skimage.exposure import histogram`) - Fornece a função para calcular a frequência dos tons de cinza.
	- `color` - Contém as funções para conversão de espaços de cores, como transformar uma imagem colorida (RGB) em tons de cinza (`rgb2gray`).
- `import cv2` - OpenCV é uma biblioteca para Visão Computacional. O OpenCV vem para "substituir" o Scikit-Image de forma mais focada em performance e aplicações em tempo real. Ideal para tarefas complexas como detecção de objetos e processamento de vídeo.

## Funções

 - `imgagem = io.imread('nome_imagem.png')`= server para ler a imagem e carrega na RAM como um `numpy` array.
 
 - `imagem.shape` = retorna as dimensões da imagem, relacionado a resolução espectral e espacial. Se retornar x,y é uma imagem monocromática, se retornar mais um valor (geralmente 3), é uma imagem colorida com canais RGB (se a dimensão for 3).

 - `imagem.dtype` = mostra qual o tipo de dado da imagem (como `uint8`), definindo assim a profundidade radiométrica. Por exemplo, um `uint8` significa que os pixels variam de 0 a 255.

 - `img_as_float()` e `img_as_ubyte()` = são autoexplicativos, servem para converter a resolução radiométrica. As vezes é preciso fazer conta com `float` devido a precisão e depois transformar tudo em inteiro de 8 bits.

- `imagem[0:10, 0:10]` = basicamente é uma forma de fazer *slicing* da imagem para ter acesso à **vizinhança**.
-
- `r = cores[:, :, 0]` = o código visa isolar a banda zero (Vermelho) do tensor tridimensional `cores` (um vetor de imagem mesmo, lido com o `io.imread()`).

 - `L = ((max - min) / 255) * img + min` = é o cálculo para transformar os valores para a escala de 0 a 255, pega o valor máximo e mínimo da imagem, converte um determinado ponto (`img`). 

 - `hist, bins = np.histograma(...)` = conta a frequência absoluta de cada nível de cinza gerando base para as estatísticas locais e globais. 

 - `cdf = np.cumsum(hist)` = calcula o histograma acumulado.

# Capítulo 1 - Introdução

Para a computação, imagens são uma matriz de números, representando as cores das imagens em uma determinada escala, seja ela tons de cinza, coloridas ou outras.  Isso auxilia a identificar padrões. 

Para iniciar neste ramo, é necessário se atentar à algumas especificações e necessidades como um **Hardware Especializado** (GPUs e Processadores dedicados), **Softwares de Processamento** (bibliotecas e algorítimos) e **Armazenamento e Rede** (Gerenciamento de grandes volumes de dados).

# Capítulo 2 - Formação de Imagens

## 2.1. Discretização

* Uma imagem monocromática pode ser determinada por uma função *f(x,y)*, onde *x* e *y* representam coordenadas espaciais.

* Para que isso seja entendido pelo computador, é necessário fazer algumas transformações, passando valores contínuos para discretos, realizando amostragem (domínio espacial) e quantização (valores de intensidade luminosa). 

* Resultando assim em uma matriz bidimensional onde cada elemento é um pixel.

## 2.2. Estrutura de Dados

Basicamente computador enxerga essa matriz de uma determinada maneira, trazendo conceitos como **Vizinhança-4** (que conta somente nas 4 direções) e **Vizinhança-8** (conta as 4 direções + 4 diagonais).

# Capítulo 3 - Resoluções

## 3.1. Resolução Espacial

A *Grade* de Dados representa a resolução espacial, que por si, está relacionada com as dimensões reais das coisas, então por exemplo, quanto maior a resolução, menor a área que cada pixel representar no mundo real. A Resolução Linear pode ser calculada por:
$$IFOV_{linear} = \frac{H \cdot D} {f}$$

* $H$ é a altitude, $D$ é a dimensão do detector e $f$ é a distância focal.

> Isso entra naquele ponto que ele disse, para melhorar a resolução é só diminuir a distância focal

> Tome cuidado, pois resoluções espaciais muito altas geram matrizes gigantes, aumentando a complexidade dos algoritmos de varredura.

## 3.2. Resolução Radiométrica

A **Resolução Radiométrica** refere-se ao número de níveis de intensidade (tons de cinza) que o sistema consegue registrar. Em termos computacionais, isso é a *largura* do dado em bits. Por exemplo, 6 bits = 64 níveis, 8 bits = 256 níveis e por ai vai.

## 3.3. Resolução Espectral

A **Resolução Espectral** é definida pelo número e largura das bandas espectrais (canais) que o sensor possui. Uma imagem multiespectral, acaba por se tornar um array tridimensional e não mais uma matriz bidimensional.

## 3.4. Resolução Temporal

Basicamente, a **Resolução Espectral** se refere ao intervalo de tempo entre aquisições de dados na mesma área. Como por exemplo, quanto tempo demorou para um drone passar novamente por uma área.

# Capítulo 4 - Transformações de Imagem

Aqui começam as transformações de imagens, realizando operações de mapeamento entre conjuntos de dados, entendendo como funcionam os algoritmos para manipular esses dados.

## 4.1. Operações de Ponto (Point Processing)

A forma mais simples de transformação é através das **Operações de Ponto (Point Processing)**, onde o valor de um pixel na imagem de saída depende apenas do valor do pixel correspondente na imagem de entrada.

A implementação é feita através de uma **Look-Up Table (LUT)**, que se trata de uma tabela para facilitar as transformações, evitando a aplicação de fórmulas muito complexas em cada um dos milhões de pixels.

Na prática, seria como se criássemos um array de 256 posições (para imagens de 8 bits) com os resultados pré-calculados. O algoritmo consulta o valor no array, transformando todo o cálculo complexo em acesso à memória de tempo constante.

## 4.2. Transformações Radiométricas Comuns

As **Transformações Radiométricas** servem para alterar o brilho ou contraste, afetando diretamente a *Resolução Radiométrica*. 
* **Negativo:** é útil para realçar detalhes claros em fundos escuros, invertendo os valores. $$s = L - 1 - r$$ 
	- $s$ = saída (novo valor de intensidade do pixel transformado)
	* $L$ = níveis (quantidade total de níveis de cinza da imagem)
	* $r$ = entrada (intensidade do pixel original)
- **Limiarização:** transforma uma imagem em tons de cinza em uma imagem binária (preto e branco puro).
- **Transformação Logarítmica:** Expande os valores de pixels escuros e comprime os claros. Essencial quando você tem uma imagem com uma faixa dinâmica muito alta.

## 4.3. Operações Aritméticas e Lógicas

É possível fazer com que o algoritmo processe apenas uma parte do frame através de operações lógicas com **AND/OR**. Outro ponto importante, é a **Subtração de Imagens** que detecta as mudanças que houveram na cena, usado principalmente para detecção de movimento.

# Capítulo 5 - Distorções Radiométricas

Na prática, este capítulo relata sobre os erros nos valores de brilho dos pixels que não apresentam a realidade do objeto da imagem. Em resumo, ele busca fazer um tratamento de dados para realmente retratar a realidade.

As principais distorções ocorrem por falhas no sensor, ruído eletrônico ou interferência atmosférica, como nuvens ou problemas com o tempo.

Devido a estes e outros erros, podemos perder dados em uma imagem, gerando pontos pretos ou brancos sem informação. Para corrigir isso, precisamos de algoritmos para estimar os valores ausentes com base nos vizinhos. Nessa linha temos dois métodos principais, **Método da Substituição Simples** e **Método da Média entre Linhas Adjacentes**.

## 5.1. Método da Substituição Simples

O algoritmo assume que o pixel *V* perdido na posição *i, j* é idêntico ao pixel da linha imediatamente anterior: 
$$v_{i,j} = v_{i, j-1}$$
Este método se torna muito barato computacionalmente tem O(1) por pixel corrigido, porém pode acabar criando artefatos visuais se houver ma mudança brusca de detalhe entre as linhas.

## 5.2. Método da Média entre Linhas Adjacentes

O algoritmo calcula a média aritmética entre os pixels das linhas superior e inferior.
$$v_{i,j} = \frac {v_{i, j-1} + v_{i, j+1}} {2}$$
Isso faz acaba gerando uma transição mais suave e natural, porém em regiões de bordas, com transições rápidas de brilho, esse método pode causar erros grosseiros de estimativas.

# Capítulo 7 - Realce de Imagens

Este capítulo visa entender as técnicas de destaque de características de interesse em uma imagem, isso facilita a visualização, tornando-a mais adequada para análise humano e por máquina. Para isso, podemos aplicar essas técnicas no **domínio espacial** (manipulação direta dos pixels) ou no **domínio da frequência**.

## 7.1. Histogramas

O histograma é uma representação gráfica que informa a frequência com que cada tom de cinza aparece na imagem.

A probabilidade de ocorrência de um nível de cinza $l$ é estimada pela sua frequência relativa: $P(l) = \frac {n_l} {n}$​​, onde $n_l$​ é o número de pixels com esse nível e $n$ o total de pixels.

Esse tipo de representação nos traz dados imediatos sobre o brilho e o contraste da cena. Além disso, através do histograma, calculam-se métricas essenciais como a média ($m$), o desvio padrão ($std$) e a amplitude ($a$).

## 7.2. Técnicas de Realce por Contraste

Existem várias formas de transformar os níveis de brilho originais para melhorar a imagem:

- **Realce Linear:** utiliza uma função linear ($y = ax +b$), assim expande os valores de brilho em um intervalo mais amplo. 

- **Negativo de Imagem:** Inverte os tons de cinza, assim realçando os detalhes claros em fundos escuros. 

- **Transformações de Gama:** Utiliza potências ($y = c \cdot x^y$) para comprimir ou expandir os níveis de brilho. Valores de $γ>1$ comprimem os tons claros, enquanto $γ<1$ realça áreas escuras.

## 7.3. Equalização de Histogramas

Essa técnica visa gerar imagens com uma distribuição uniforme de níveis de cinza, ou seja, fazer com que cada nível de cinza tenha aproximadamente o mesmo número de pixels.

Existem situações em que, após a equalização, a imagem se torna muito homogênea e perde o contraste e os detalhes.

## 7.4. Processamento Local

Existem dois tipos básicos de processamento, o *processamento global* que afetam a imagem inteira e funcionam com base em estatísticas totais e o *processamento local* que atua em **vizinhanças** (geralmente em $3 \times 3$ pixels).

Esse tipo de abordagem nos permite realizar pequenas alterações em áreas que necessitam, sem afetar outras áreas que já estão corretas, ou até mesmo que receberam outro tipo de tratamento. Permitindo que, por exemplo, uma área $X$ receba um tratamento de imagem e uma área $Y$ receba outro, sem que uma afete a outra diretamente.

Este método de **processamento local**, busca utilizar a média e a variância de cada vizinho para adaptar a transformação do contraste de forma dinâmica, permitindo um processamento mais assertivo da imagem.


# Capítulo 8 - Filtros Espaciais de Suavização

A suavização de imagens é utilizada para atenuação de ruídos na imagem. Ao contrário de outros capítulos, a transformação da imagem é calculada não com base no mesmo pixel, mas sim com base nos seus vizinhos. 

Nesse tipo de transformação, utilizamos uma máscara com uma submatriz (geralmente $3\times3$, $5\times5$ ou $7\times7$) e então essa máscara é aplicada sobre a imagem deslizando linha por linha.

## 8.1. Suavização pela Média

$$R(i,j) = \left[\frac{1}{MN}\right] \sum_{m=1}^M \sum_{n=1}^N f(m,n)$$
> $M$ e $N$ são o tamanho da máscara $M \times N$

A função acima vai gerar o resultado da máscara, onde $\left [\frac{1}{MN} \right ]$ é o valor que será multiplicado em cada ponto da imagem onde a máscara está sendo aplicada e faz a média de acordo com o tamanho da máscara. Então no caso do exemplo de uma máscara $3 \times 3$, seriam somados todos os pontos nesse intervalo e dividido por 9. $$\frac{\left (\sum_{m=1}^3 \sum_{n=1}^3 \right)} 9$$O maior problema disso é que ao aplicar a máscara em "grade", ela vai criar lacunas nas bordas que pode variar de tamanho de acordo com o tamanho da máscara, essa variação segue a fórmula $\frac{(K-1)} 2$. Então $3 \times 3$ tem 1 pixel de borda, $5 \times 5$ tem 2 pixels de borda e por ai vai.

## 8.2. Filtragem Gaussiana
$$h(x, y) = e^{\frac {x^2+y^2} {2\sigma^2}}$$
> Em que o $\sigma$ (sigma) é o desvio padrão. Ele controla o nível do borrão, quanto maior o $\sigma$ maior a abertura do sino e mais suave fica a imagem.

A filtragem gaussiana da pesos maiores para os pixels mais próximos do centro, o que faz com que haja uma suavização mais "natural" e preserva melhor as estruturas do que o borrão gerado pela média.

## 8.3.  Mediana

Basicamente aplica a mediana nos pixels afetados pela máscara, ela tem um ponto especial em que ela não cria tons de cinza que não existiam antes. Porém, ela destrói bordas pontudas solitárias e suaviza bordas retas.