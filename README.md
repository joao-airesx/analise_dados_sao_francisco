# Análise de Crimes em São Francisco

Este projeto tem como objetivo realizar uma análise exploratória dos dados de crimes ocorridos na cidade de São Francisco. Foram utilizadas bibliotecas Python para manipulação de dados e visualização de gráficos.

Bibliotecas Utilizadas:

- numpy: Biblioteca para operações numéricas.
- pandas: Biblioteca para manipulação de dados em formato tabular.
- matplotlib: Biblioteca para criação de gráficos.
- seaborn: Biblioteca para melhorar a estética dos gráficos.
- folium: Biblioteca para criação de mapas interativos.
- squarify: Biblioteca para criação de mapas de árvore.
- wordcloud: Biblioteca para criação de nuvem de palavras.

Dados Utilizados

Os dados de crimes estão armazenados em um arquivo CSV chamado 'crime.csv'. Eles foram carregados utilizando a biblioteca pandas, e algumas informações iniciais foram verificadas, como a forma dos dados, as primeiras linhas do dataframe e a descrição das variáveis.

# Visualização de Dados

Foram utilizados diversos gráficos para visualizar os dados de crimes em São Francisco:
- Gráfico de contagem das categorias de crimes: Foi plotado um gráfico de barras para visualizar a quantidade de ocorrências de cada tipo de crime. As cores das barras foram personalizadas usando a paleta 'gnuplot'.

Mapa de árvore dos 25 principais crimes: 
- Foi criado um mapa de árvore para visualizar os 25 principais crimes de forma hierárquica. As cores das áreas foram personalizadas usando a paleta 'magma'.

Nuvem de palavras da descrição dos crimes: 
- Foi gerada uma nuvem de palavras para visualizar as palavras mais frequentes nas descrições dos crimes. A cor de fundo foi definida como laranja.

Gráfico de barras dos distritos com mais crimes: 
- Foi criado um gráfico de barras para visualizar a quantidade de crimes em cada distrito de São Francisco. As cores das barras foram personalizadas usando a paleta 'spring'.

Gráfico de barras das regiões com mais crimes: 
- Foi criado um gráfico de barras para visualizar as regiões com mais ocorrências de crimes. As cores das barras foram personalizadas usando a paleta 'ocean'.

Execução do Projeto
Para executar o projeto, é necessário ter instaladas as bibliotecas mencionadas no início do código. Os dados de crimes devem estar disponíveis no arquivo 'crime.csv' no mesmo diretório do código.

# Observações
- Algumas das bibliotecas utilizadas estão sendo importadas mais de uma vez ao longo do código, o que pode gerar advertências. Recomenda-se otimizar as importações e utilizar apenas uma vez as bibliotecas necessárias.
- É importante notar que alguns estilos usados ​​para plotar os gráficos podem estar obsoletos a partir da versão 3.6 do Matplotlib.
