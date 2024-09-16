import streamlit as st
import yfinance as yf
from datetime import date
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, plot_components_plotly
from plotly import graph_objs as go

DATA_INICIO = '2017-01-01'
DATA_FIM = date.today().strftime('%y-%m,-%d')

st.title('Análise de ações')

# Criando a sidebar
st.sidebar.header('Escolha a ação')

n_dias = st.slider('Quantidade de dias de previsão', 30, 365)


def pegar_dados_acoes():
    path = 'C:/Users/kaikm/OneDrive/Documentos/GitHub/Python/App-Financeiro-Python/base de dados/acoes.csv'
    return pd.read_csv(path, delimiter=';')

df = pegar_dados_acoes()

acao = df['snome']
nome_acao_escolhida = st.sidebar.selectbox('Escolha uma ação:', acao)



