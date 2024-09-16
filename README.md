# Análise de Ações com Streamlit

## Descrição do Projeto
Este projeto é um aplicativo de análise financeira desenvolvido com **Streamlit**, uma biblioteca Python para criação de aplicações web interativas. O objetivo do aplicativo é permitir que os usuários analisem o histórico e a previsão de preços de ações.


## Video do dashboard
  <div align="center">
    <img height="600" src="img/dashboard.gif"  />
  </div>


### Funcionalidades

- **Visualização de Dados**: O aplicativo exibe uma tabela com os últimos valores de fechamento e abertura de uma ação selecionada.
- **Gráficos de Preços**: Inclui gráficos interativos que mostram os preços de abertura e fechamento das ações ao longo do tempo.
- **Previsão de Preços**: Utiliza o modelo Prophet para prever os preços futuros das ações com base nos dados históricos.
- **Escolha da Ação**: Permite que o usuário escolha a ação que deseja analisar a partir de uma lista fornecida.

### Como Usar

1. **Escolha uma Ação**: No painel lateral, selecione a ação que deseja analisar.
2. **Defina o Período de Previsão**: Use o slider para definir o número de dias para o qual deseja prever os preços.
3. **Visualize os Dados**: Veja a tabela com os últimos valores de fechamento e abertura, gráficos de preços e previsões futuras.


## Bibliotecas Utilizadas
Abaixo estão listadas as bibliotecas e dependências necessárias para a execução do projeto:

### Principais Bibliotecas

- **Streamlit**: Criação da interface web de forma simples e eficiente.
  - Instalação: `pip install streamlit`
  
- **yFinance**: Obtenção de dados históricos e atuais das ações.
  - Instalação: `conda install yfinance`

- **Plotly**: Visualização interativa de dados financeiros.
  - Instalação: `conda install plotly`

- **Prophet**: Previsão de preços usando modelos de machine learning.
  - Instalação: 
    ```bash
    conda install -c conda-forge fbprophet
    conda install -c conda-forge pystan
    ```

- **Ephem**: Cálculos astronômicos para análise de calendários financeiros.
  - Instalação: `conda install -c anaconda ephem`

### Instalação das Dependências

Você pode instalar as dependências do projeto usando os comandos abaixo:

```bash
conda install yfinance
pip install streamlit
conda install plotly
conda install -c anaconda ephem
conda install -c conda-forge pystan
conda install -c conda-forge fbprophet
