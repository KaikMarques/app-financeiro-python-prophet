# App Financeiro com Python e Streamlit

## Descrição do Projeto
Este projeto cria um aplicativo web financeiro usando Python e Streamlit para acompanhar ações do mercado financeiro, fazer previsões de preços usando machine learning com a biblioteca Prophet e salvar os dados na nuvem.

## Video do dashboard
  <div align="center">
    <img height="600" src="img/dashboard.gif"  />
  </div>


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
