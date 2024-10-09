import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import folium as f
from streamlit_folium import folium_static
from PIL import Image

# Caminho da nova imagem (ícone da aba do navegador)
image_icon_path = 'images/new-york-city-logo-5237e7.png'
image_icon = Image.open(image_icon_path)

# Configurando o título e o ícone da aba do navegador
st.set_page_config(page_title="Análise de Aluguéis NYC", page_icon=image_icon, layout='wide')

# Caminho da imagem original da sidebar
image_sidebar_path = 'images/pngegg.png'
image_sidebar = Image.open(image_sidebar_path)

# Carregando o dataset
st.title('Análise de Aluguéis na Cidade de Nova York')

@st.cache_data
def load_data():
    data = pd.read_csv('dataset/AB_NYC_2019.csv')
    return data

data = load_data()

# Icone e Título do App
st.sidebar.image(image_sidebar, width=60)
st.sidebar.markdown("""---""")

# Sidebar para o controle do número de imóveis a serem plotados no mapa
st.sidebar.title('Configurações do Mapa')
num_pontos = st.sidebar.slider('Número de imóveis a serem plotados no mapa', min_value=10, max_value=500, value=100, step=10)
st.sidebar.markdown("""---""")

# Multiselect para selecionar os bairros
bairros_selecionados = st.sidebar.multiselect(
    'Selecione os bairros que deseja visualizar no mapa',
    options=data['neighbourhood_group'].unique(),
    default=data['neighbourhood_group'].unique()
)

# Filtrar os dados com base nos bairros selecionados
data_filtrada = data[data['neighbourhood_group'].isin(bairros_selecionados)]
st.sidebar.markdown("""---""")

# Radio button para selecionar o gráfico a ser exibido
grafico_tipo = st.sidebar.radio(
    'Escolha o tipo de gráfico a ser exibido',
    ('Histograma de Preços', 'Histograma de Avaliações')
)

# Assinatura do autor
st.sidebar.markdown("""---""")
st.sidebar.write('')
st.sidebar.caption('Powered by Marcelo- 2024')
st.sidebar.caption('[Portifólio](https://marceloalmeida369.github.io/portf-lio_mla/#)')
st.sidebar.caption('[github](https://github.com/MarceloAlmeida369)')
st.sidebar.caption('[Linkedin](www.linkedin.com/in/marcelola)')
st.sidebar.caption(':blue[servicoseletricosloiola@gmail.com]')

# Dividindo o dashboard em abas
abas = st.tabs(["Principal", "Mapas", "Mapa por Bairro"])

# Aba Principal
with abas[0]:
    st.subheader('Visualizando as primeiras linhas do dataset')
    # Pequena descrição explicando o que está sendo mostrado
    st.write("""
    Abaixo estão as primeiras linhas do dataset filtrado, que mostram uma amostra das propriedades disponíveis para alugar na cidade de Nova York. 
    Essas informações incluem detalhes como o tipo de acomodação, preço, avaliações e localização dos imóveis. 
    Use esta visualização para entender a estrutura básica dos dados e os tipos de informação disponíveis para análise.
    """)
    st.write(data_filtrada.head())
    st.markdown("""---""")

    # Calculando o valor médio do aluguel
    # Pequena descrição explicando o que está sendo mostrado
    st.write("""
    Abaixo estão as estatísticas básicas dos aluguéis disponíveis no dataset. 
    Você verá o valor médio dos aluguéis e também o valor máximo cobrado por noite. 
    Essas informações são úteis para entender a faixa de preços e a distribuição de valores na cidade de Nova York.
    """)
    valor_medio = np.mean(data_filtrada['price'])
    st.subheader(f'O valor médio dos aluguéis é: U${valor_medio:.2f}')

    # Calculando o valor máximo do aluguel
    valor_maximo = np.max(data_filtrada['price'])
    st.subheader(f'O valor máximo dos aluguéis é: U${valor_maximo:.2f}')
    st.markdown("""---""")

    # Exibindo as categorias de tipo de quarto
    room_types = np.unique(data_filtrada['room_type'])
    st.subheader('Tipos de quartos disponíveis:')
    st.write("""Aqui estão os tipos de quartos disponíveis nas listagens de aluguel do Airbnb. Cada categoria define o tipo de acomodação que os hóspedes terão ao alugar uma propriedade. """)
    st.write(room_types)
    st.write("Tradução:")
    st.write("Entire home/apt: Casa/Apartamento Inteiro")
    st.write("Private room: Quarto Privado")
    st.write("Shared room: Quarto Compartilhado")
    st.markdown("""---""")
    

    # Número de hosts únicos
    # Pequena descrição explicando o que está sendo mostrado
    st.write("""
    A seguir, você verá o número total de hosts únicos, ou seja, a quantidade de diferentes anfitriões que oferecem imóveis para alugar na plataforma. 
    Além disso, é exibido o desvio padrão dos preços dos aluguéis, que indica a dispersão dos valores em torno da média. 
    Essas informações ajudam a entender a diversidade de proprietários e a variabilidade dos preços na cidade de Nova York.
    """)
    host_id_unique = np.unique(data_filtrada['host_id'])
    st.subheader(f'Número de hosts únicos: {len(host_id_unique)}')
    

    # Desvio padrão dos preços
    desvio_padrao = np.std(data_filtrada['price'])
    st.subheader(f'O desvio padrão dos preços é: U${desvio_padrao:.2f}')
    st.markdown("""---""")

    # Exibindo o gráfico de acordo com a escolha do usuário
    # Pequena descrição explicando o que está sendo mostrado
    st.write("""
    A seguir, você pode visualizar dois tipos de gráficos, dependendo da escolha do usuário(Selecione a opção de gráfico ao lado):
    
    - **Histograma de Preços**: Este gráfico exibe a distribuição dos aluguéis com valores abaixo de U$1250, permitindo analisar como os preços estão distribuídos entre as listagens de imóveis mais acessíveis.
    - **Histograma de Avaliações**: Este gráfico mostra a distribuição do número de avaliações para os imóveis que possuem menos de 300 avaliações. Isso ajuda a identificar quais propriedades têm maior interação com os hóspedes.
    """)
    if grafico_tipo == 'Histograma de Preços':
        st.subheader('Distribuição de aluguéis abaixo de U$1250')
        price_filtered = data_filtrada.loc[data_filtrada['price'] < 1250, 'price']
        fig, ax = plt.subplots()
        ax.hist(price_filtered, bins=12)
        st.pyplot(fig)
    else:
        st.subheader('Distribuição do número de avaliações abaixo de 300')
        reviews_filtered = data_filtrada.loc[data_filtrada['number_of_reviews'] < 300, 'number_of_reviews']
        fig2, ax2 = plt.subplots()
        ax2.hist(reviews_filtered, bins=10)
        st.pyplot(fig2)
        

    # Gráfico de barra dos valores de aluguel mais caros por região
    st.markdown("""---""")
    st.subheader('Valores de aluguel mais caros por região')
    # Pequena descrição explicando o que está sendo mostrado
    st.write("""
    Abaixo, você verá um gráfico de barras que mostra os aluguéis mais caros em cada região da cidade de Nova York. 
    Este gráfico exibe o valor máximo cobrado por noite em diferentes bairros, permitindo uma comparação clara entre as áreas mais caras da cidade. 
    Essa visualização é útil para identificar quais regiões possuem os imóveis com os preços mais elevados, ajudando a entender a distribuição de aluguéis de luxo.
    """)
    df_grouped = data_filtrada[['price', 'neighbourhood_group']].groupby('neighbourhood_group').max().reset_index()
    fig3 = px.bar(df_grouped, x='neighbourhood_group', y='price', title='Aluguéis mais caros por Região')
    st.plotly_chart(fig3)
    

# Aba de Mapas
with abas[1]:
    # Mapa interativo com os imóveis mais caros
    st.subheader('Mapa dos imóveis mais caros por região')
    # Pequena descrição explicando o que está sendo mostrado
    st.write("""
    A seguir, você verá um mapa interativo que mostra a localização dos imóveis mais caros por região na cidade de Nova York. 
    Os pontos no mapa representam os imóveis com o maior valor de aluguel em cada bairro, permitindo que você visualize geograficamente onde estão concentrados os aluguéis mais elevados. 
    Essa visualização é útil para identificar as regiões com imóveis de alto padrão e comparar as áreas de maior valor em Nova York.
    """)
    data_plot = data_filtrada[['price', 'neighbourhood_group', 'latitude', 'longitude']].groupby(['neighbourhood_group']).max().reset_index()

    mapa = f.Map(location=[data_plot['latitude'].mean(), data_plot['longitude'].mean()], zoom_start=11)
    for index, location_info in data_plot.iterrows():
        f.Marker([location_info['latitude'], location_info['longitude']],
                 popup=location_info['neighbourhood_group']).add_to(mapa)

    folium_static(mapa)

    # Mapa interativo com o número de imóveis definido pela sidebar
    st.subheader(f'Mapa com {num_pontos} imóveis categorizados por tipo de quarto')
    st.write("""
    O mapa interativo abaixo exibe uma amostra de imóveis disponíveis na cidade de Nova York, com o número de propriedades sendo ajustado pela opção da sidebar ao lado. 
    Cada ponto no mapa representa um imóvel, categorizado de acordo com o tipo de acomodação oferecida: **Quarto Privado**, **Casa/Apartamento Inteiro** ou **Quarto Compartilhado**. 
    As cores dos pontos ajudam a diferenciar cada tipo de acomodação, facilitando a visualização da distribuição desses imóveis por tipo de quarto nas diferentes regiões da cidade.
    """)
    colunas = ['neighbourhood_group', 'room_type', 'latitude', 'longitude']
    data_plot = data_filtrada[colunas].sample(num_pontos)

    # Definindo cores para os diferentes tipos de quartos
    data_plot['color'] = 'NA'
    data_plot.loc[data_plot['room_type'] == 'Private room', 'color'] = 'darkgreen'
    data_plot.loc[data_plot['room_type'] == 'Entire home/apt', 'color'] = 'darkred'
    data_plot.loc[data_plot['room_type'] == 'Shared room', 'color'] = 'purple'

    # Criando o mapa
    mapa_2 = f.Map(location=[data_plot['latitude'].mean(), data_plot['longitude'].mean()], zoom_start=11)
    for _, location_info in data_plot.iterrows():
        f.Marker([location_info['latitude'], location_info['longitude']],
                 popup=f"{location_info['neighbourhood_group']}, {location_info['room_type']}",
                 icon=f.Icon(color=location_info['color'])).add_to(mapa_2)

    folium_static(mapa_2)

# Aba Mapa por Bairro
with abas[2]:
    
    st.subheader('Mapa com pinos coloridos por bairro')

    st.write("""
    Neste mapa interativo, você verá a localização dos imóveis disponíveis para alugar na cidade de Nova York, representados por pinos coloridos, categorizados por bairro. 
    Além disso, você encontrará os principais pontos turísticos da cidade, como **Estátua da Liberdade**, **Empire State Building**, e **Central Park**, indicados por pinos **cinzas(Clique com o cursor do mouse para ver o nome dos pontos turísticos ou do imóvel)**. 
    Os imóveis que estão mais próximos dos pontos turísticos tendem a ter um valor de aluguel mais elevado devido à alta demanda por localizações privilegiadas.
    
    A análise da proximidade dos imóveis com relação aos pontos turísticos pode ser um fator importante na determinação dos preços dos aluguéis. Quanto mais próximo o imóvel estiver de um ponto turístico, maior a probabilidade de ele ser mais caro devido à conveniência e atratividade da localização.
    """)

    
    # Definindo cores para cada bairro
    cores_bairros = {
        'Bronx': 'blue',
        'Brooklyn': 'green',
        'Manhattan': 'red',
        'Queens': 'orange',
        'Staten Island': 'purple'
    }
    
    # Criando o mapa com pinos coloridos por bairro
    data_amostrada = data_filtrada.sample(num_pontos)  # Usar o número de pontos da sidebar
    
    mapa_3 = f.Map(location=[data_amostrada['latitude'].mean(), data_amostrada['longitude'].mean()], zoom_start=11)
    
    # Adicionando pinos para as residências
    for _, location_info in data_amostrada.iterrows():
        bairro = location_info['neighbourhood_group']
        cor = cores_bairros.get(bairro, 'gray')  # Usar cor padrão caso o bairro não esteja no dicionário
    
        f.Marker([location_info['latitude'], location_info['longitude']],
                 popup=f"{bairro}, {location_info['room_type']}",
                 icon=f.Icon(color=cor)).add_to(mapa_3)
    
    # Definindo pontos turísticos
    pontos_turisticos = [
        {'nome': 'Estátua da Liberdade', 'latitude': 40.6892, 'longitude': -74.0445},
        {'nome': 'Empire State Building', 'latitude': 40.748817, 'longitude': -73.985428},
        {'nome': 'Central Park', 'latitude': 40.785091, 'longitude': -73.968285},
        {'nome': 'Times Square', 'latitude': 40.758896, 'longitude': -73.985130},
        {'nome': 'Brooklyn Bridge', 'latitude': 40.706086, 'longitude': -73.996864},
        {'nome': 'One World Trade Center', 'latitude': 40.712743, 'longitude': -74.013379}
    ]
    
    # Adicionando pinos para os pontos turísticos
    for ponto in pontos_turisticos:
        f.Marker([ponto['latitude'], ponto['longitude']],
                 popup=ponto['nome'],
                 icon=f.Icon(color='cadetblue', icon='info-sign')).add_to(mapa_3)
    
    # Exibindo o mapa com os pinos das residências e pontos turísticos
    folium_static(mapa_3)
    
    # Slider abaixo do mapa para controlar o número de pinos no mapa de bairros
    num_pinos_mapa_bairros = st.slider('Número de imóveis por bairro no terceiro mapa', min_value=10, max_value=200, value=50, step=10)

    st.write("""
    Neste mapa, além de visualizar os imóveis por bairro e os pontos turísticos de Nova York, você pode ver a proximidade dos imóveis com relação aos pontos turísticos mais famosos. 
    Imóveis que estão mais próximos dos pontos turísticos, como a **Estátua da Liberdade** ou o **Empire State Building**, têm uma demanda maior, o que pode refletir em um aumento nos preços. 
    A nova coluna **distância_ponto_turistico_mais_proximo** calcula a distância em quilômetros entre o imóvel e o ponto turístico mais próximo. Utilize essa informação para identificar como a localização pode influenciar os valores de aluguel.
    """)