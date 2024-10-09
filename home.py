import streamlit as st
from PIL import Image

# Função para configurar a página principal, como o título e o ícone
def configurar_pagina():
    image_icon_path = 'images/new-york-city-logo-5237e7.png'  # Caminho atualizado para a nova imagem enviada
    image_icon = Image.open(image_icon_path)
    st.set_page_config(page_title="Análise Airbnb NYC", page_icon=image_icon, layout='wide')
    return image_icon

# Função para configurar a barra lateral (sidebar)
def configurar_sidebar():
    image_sidebar_path = 'images/pngegg.png'
    image_sidebar = Image.open(image_sidebar_path)
    st.sidebar.image(image_sidebar, width=90)
    st.sidebar.markdown("""---""")
    # Assinatura do autor na sidebar
    st.sidebar.write('')
    st.sidebar.caption('Powered by Marcelo- 2024')
    st.sidebar.caption('[Portifólio](https://marceloalmeida369.github.io/portf-lio_mla/#)')
    st.sidebar.caption('[github](https://github.com/MarceloAlmeida369)')
    st.sidebar.caption('[Linkedin](www.linkedin.com/in/marcelola)')
    st.sidebar.caption(':blue[servicoseletricosloiola@gmail.com]')

# Função para exibir o título e a imagem centralizada na página principal
def exibir_titulo_e_imagem(image_icon):
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Bem-vindo à Análise de Aluguéis da plataforma Airbnb em Nova York no ano de 2019!</h1>
        </div>
        """, unsafe_allow_html=True
    )
    # Exibindo a imagem centralizada diretamente com st.image()
    st.image(image_icon, width=300, output_format="right")

# Função para exibir a introdução da análise
def exibir_introducao():
    st.markdown(
        """
        <div style="text-align: justify;">
            <p>Esta plataforma foi desenvolvida para explorar e visualizar os dados de aluguéis da plataforma Airbnb na cidade de Nova York.
            Aqui você poderá visualizar insights detalhados sobre os preços de aluguéis, avaliações e dados geográficos.
            Acesse o dashboard interativo ao lado na aba visão principal para obter uma análise mais profunda.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.markdown("""---""")

# Função para exibir a descrição do dataset e suas análises
def exibir_descricao_dataset():
    st.markdown("""
        ## Descrição do Dataset

        O dataset contém dados detalhados sobre os aluguéis de imóveis disponíveis na plataforma Airbnb, especificamente na cidade de Nova York, em 2019. As informações contidas no dataset incluem:

        - **ID do Imóvel**: Identificador único de cada imóvel listado no Airbnb.
        - **Nome do Imóvel**: O nome descritivo de cada propriedade.
        - **Host**: O nome do anfitrião responsável pelo imóvel.
        - **Bairro**: O bairro da cidade de Nova York onde o imóvel está localizado.
        - **Tipo de Quarto**: O tipo de acomodação oferecida, como "Quarto Inteiro", "Quarto Privado" ou "Quarto Compartilhado".
        - **Preço por Noite**: O valor cobrado por noite para alugar o imóvel.
        - **Número de Avaliações**: A quantidade de avaliações recebidas pela propriedade.
        - **Avaliação Média**: A média das avaliações dadas pelos hóspedes.
        - **Coordenadas Geográficas**: A latitude e longitude da propriedade para localização geográfica.

        ## Uso do Dataset

        Este dataset pode ser utilizado para realizar diversas análises, como:

        - **Análise de Preços**: Comparar o preço médio de aluguéis em diferentes bairros de Nova York.
        - **Análise de Popularidade**: Identificar quais imóveis são mais populares com base no número de avaliações e na avaliação média.
        - **Análise Geográfica**: Visualizar a distribuição dos imóveis em Nova York em um mapa interativo.
        - **Análise de Tipos de Acomodações**: Explorar os diferentes tipos de acomodações oferecidas (como apartamentos inteiros, quartos privados ou compartilhados).

        ## Análise de Proximidade de Pontos Turísticos

        Nesta análise, calculamos a distância de cada imóvel aos pontos turísticos mais famosos de Nova York, como a **Estátua da Liberdade**, o **Empire State Building** e o **Central Park**.
        Os imóveis mais próximos desses pontos turísticos tendem a ter um preço de aluguel mais alto, refletindo a maior demanda por localizações privilegiadas.

        - **Distância aos Pontos Turísticos**: A distância em quilômetros de cada imóvel ao ponto turístico mais próximo foi calculada usando as coordenadas de latitude e longitude.
        - **Impacto no Preço**: A proximidade dos imóveis a esses pontos pode influenciar significativamente o valor do aluguel, com imóveis mais próximos frequentemente apresentando preços mais elevados.

        ## Possíveis Projetos com o Dataset

        - **Dashboard de Aluguéis do Airbnb**: Um painel interativo que permite ao usuário explorar as propriedades com base em preços, avaliações e localização.
        - **Análise de Popularidade de Imóveis**: Identificar as propriedades mais populares ou com melhor custo-benefício com base nas avaliações e preços.
        - **Previsão de Preços de Aluguéis**: Criar modelos preditivos para estimar o preço de novos aluguéis com base nas características dos imóveis e da localização.

        ## Conclusão

        O dataset de "Aluguéis do Airbnb - Nova York 2019" é uma fonte rica para quem deseja explorar o mercado de hospedagem alternativa em Nova York. Ele oferece diversas possibilidades de análise e visualização, permitindo aos usuários entender melhor o comportamento dos preços e a distribuição das acomodações na cidade.

        ## Fonte do Dataset

        O dataset pode ser acessado através do Kaggle no link abaixo:

        - [New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
    """)

# Função principal que chama as outras funções
def main():
    # Configurando a página e sidebar
    image_icon = configurar_pagina()
    configurar_sidebar()
    
    # Exibindo título, imagem e introdução
    exibir_titulo_e_imagem(image_icon)
    exibir_introducao()
    
    # Exibindo a descrição do dataset
    exibir_descricao_dataset()

# Chamando a função principal
if __name__ == "__main__":
    main()
