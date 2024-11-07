# Importando as bibliotecas necessárias
import base64
from io import BytesIO
import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from Functions import Funcoes

# Carregando o banco de dados
df = pd.read_csv('data/fitness_gym.csv')

# Exibindo imagens na barra lateral
Funcoes.display_centered_image('src/imgs/nesfitv2.jpg')
st.sidebar.image('src/imgs/satisfaction_stars.png')

# Seletor de navegação na barra lateral
chart_type = st.sidebar.selectbox("Navegação", [
    "Tela de Início", "Mercado", "Planos", "Atividades", "Frequência", 
    "Informações do Projeto", "Informações do Grupo"
])

# Função para converter imagem em base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

# Renderizando o conteúdo de cada página
if chart_type == "Tela de Início":
    img_base64 = get_base64_of_bin_file("src/imgs/Tela_Inicial.jpg")
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

elif chart_type == "Mercado":
    col1, col2 = st.columns(2)
    with col1:
        st.image('src/imgs/gym_mercado.png')
    with col2:
        st.markdown("<h1 style='text-align: center;'>Contexto de mercado</h1>", unsafe_allow_html=True)
        st.markdown("""
            ***********************
            #### - O mercado fitness é uma área ampla que contempla negócios voltados à saúde e bem-estar de modo geral.
            #### - Durante as últimas décadas, a necessidade de exercícios físicos é cada vez maior, a crescente preocupação com a saúde fez com que mais pessoas procurassem academias e espaços fitness.
        """)
    st.markdown("************************")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h1 style='text-align: center;'>Estatísticas do mercado</h1>", unsafe_allow_html=True)
        st.markdown("""
            *******************
            #### - O mercado fitness no Brasil fatura R$ 12 bilhões ao ano, de acordo com o Panorama Setorial de 2023.
            #### - O valor transacionado com academias e produtos fitness cresceu cerca de 35% em 2023 comparado ao ano anterior, segundo estudo do Itaú Unibanco.
        """)
    with col2:
        st.image('src/imgs/gym_mercado2.png')

elif chart_type == "Planos":
    st.markdown("<h1 style='text-align: center;'>Estudo dos Planos</h1>", unsafe_allow_html=True)
    st.write("### Porcentagem de Alunos por Plano")
    st.pyplot(Funcoes.distribuicao_assinaturas(df))
    st.markdown("""
        ### Observação:
        - **O plano Básico engloba mais de 50% do público da academia.**
        *******************************
    """)
    st.write("### Cancelamentos por Tipo de Plano (Motivos)")
    st.pyplot(Funcoes.cancelamento_plano(df))
    st.markdown("""
        ### Principais Motivos de Cancelamento:
        - **Insatisfação**: 40%
        - **Custo alto**: 25%
        - **Falta de tempo**: 20%
        *******************************
    """)
    st.markdown("<h1 style='text-align: center;'>Satisfação Média por Plano</h1>", unsafe_allow_html=True)
    st.pyplot(Funcoes.satisfacao_plano(df))
    st.markdown("""
        ### Observação:
        - **Classificação do plano básico está bem abaixo dos outros.**
        *******************************
    """)
    st.write("<h1 style='text-align: center;'>Problemas e soluções</h1>", unsafe_allow_html=True)
    st.markdown("""
        ### Problemas e Estratégias para o Plano Básico da Academia
        (segue texto completo sem alteração)
    """)

elif chart_type == "Atividades":
    st.write("<h1 style='text-align: center;'>Estudo das Atividades</h1>", unsafe_allow_html=True)
    st.write("### Atividades Mais Realizadas")
    st.pyplot(Funcoes.distribuicao_atividades(df))
    st.markdown("""
        ### Top 3 Atividades Mais Realizadas:
        - **1. Zumba**
        - **2. Yoga**
        - **3. Musculação**
        *******************************
    """)
    st.write("### Calorias x Atividades")
    st.write("#### Média de Calorias Queimadas por Atividade")
    st.pyplot(Funcoes.calorias_atividade(df))
    st.markdown("""
        ### Top 3 Atividades com Mais Calorias Queimadas:
        - **1. CrossFit**
        - **2. Spinning**
        - **3. Boxing**
        *******************************
    """)
    st.write("<h1 style='text-align: center;'>Problemas e soluções</h1>", unsafe_allow_html=True)
    st.markdown("""
        ### Substituição da Atividade de Jump para Otimização do Desempenho
        (segue texto completo sem alteração)
    """)

elif chart_type == "Frequência":
    st.markdown("<h1 style='text-align: center;'>Estudo das Frequências</h1>", unsafe_allow_html=True)
    st.write("### Frequência Diária dos Alunos")
    st.pyplot(Funcoes.frequencia_dia(df))
    st.markdown("""
        ### Horário de Funcionamento:
        - **06:00 às 22:00**
        ### Horários de Pico:
        - **17:00 às 18:00**
        *******************************
    """)
    st.write("<h1 style='text-align: center;'>Problemas e soluções</h1>", unsafe_allow_html=True)
    st.markdown("""
        ### Otimização de Fluxo e Redução de Custos na Academia
        (segue texto completo sem alteração)
    """)

elif chart_type == "Informações do Projeto":
    st.markdown("<h1 style='text-align: center;'>Informações do projeto</h1>", unsafe_allow_html=True)
    st.markdown("""
        ****************************
        # Descrição do Projeto - Academia Fitness
        (segue texto completo sem alteração)
    """)

elif chart_type == "Informações do Grupo":
    st.markdown("<h1 style='text-align: center;'>Informações do grupo</h1>", unsafe_allow_html=True)
    st.markdown("********************")
    st.markdown("<h2 style='text-align: center;'>Integrantes do grupo FITNES</h2>", unsafe_allow_html=True)
    for col, member in zip(st.columns(3), ["Clarisse", "Malena", "Isabela"]):
        col.image(Funcoes.make_circle_image(f'src/imgs/{member}.jpg'), width=150)
        col.write(f"##### {member}")
    st.markdown("********************")
    st.markdown("<h2 style='text-align: center;'>Descrição das Responsabilidades</h2>", unsafe_allow_html=True)
    st.markdown("""
        ## Código
        ### Tiago Trindade
        - **Funções**: (segue texto completo sem alteração)
    """)
