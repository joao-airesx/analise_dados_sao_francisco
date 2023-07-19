# for comandos basicos
import numpy as np
import pandas as pd
# para visualização
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import squarify

data = pd.read_csv('crime.csv')
#verifica a forma de dados
data.shape

print(data.head())
#descrever o conjunto de dados
print(data.describe())
#verfificar se há um valor nulo
print(data.isnull().sum())

data['PdDistrict'].fillna(data['PdDistrict'].mode()[0], inplace = True)
data.isnull().any().any()


# Definir tamanho da figura
plt.rcParams['figure.figsize'] = (20, 9)
# Definir estilo de fundo
plt.style.use('dark_background')


# Plotar o gráfico de contagem da coluna 'Category'
sns.countplot(x = data['Category'],data=data, palette = 'gnuplot')

# Configurar título e rótulos dos eixos
plt.title('Maiores Crimes em São Francisco', fontweight = 30, fontsize = 20)
plt.xticks(rotation = 90)
plt.show()

#traçando um mapa de árvore
y = data['Category'].value_counts().head(25)

plt.rcParams['figure.figsize'] = (15,15)
plt.style.use('fivethirtyeight')

color = plt.cm.magma(np.linspace(0, 1, 15))
squarify.plot(sizes=y.values, label= y.index, alpha=.8, color=color)
plt.title('Mapa da árvore dos 25 principais crimes', color= 'black', fontweight = 30, fontsize = 20)

plt.axis('off')
plt.show()

from wordcloud import WordCloud

plt.rcParams['figure.figsize'] = (15, 15)
plt.style.use('fast')

wc = WordCloud(background_color= 'orange', width = 1500, height=1500).generate(str(data['Descript']))
plt.title('Descrição do Crime',color = 'Black', fontweight = 'bold', fontname = 'Arial', fontsize = 20)

plt.imshow(wc)
plt.axis('off')
plt.show()

plt.rcParams['figure.figsize'] = (20, 9)
plt.style.use('seaborn')

color = plt.cm.spring(np.linspace(0, 1, 15))
data['PdDistrict'].value_counts().plot.bar(color= color, figsize = (15, 10))

plt.xticks(rotation = 90)
plt.show()

plt.rcParams['figure.figsize'] = (20, 9)
plt.style.use('seaborn')

color = plt.cm.ocean(np.linspace(0, 1, 15))
data['Address'].value_counts().head(15).plot.bar(color = color, figsize = (15, 10))

plt.title('Top 15 Regiões com Crimes', color = 'Black', fontweight = 'bold', fontsize = 20)

plt.xticks(rotation = 90)
plt.show()