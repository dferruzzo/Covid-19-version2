"""
Script carregar os dados da cidade de São Paulo
----------------------------------------------------
Não tem argumentos de entrada.
Entrega dois data frames, cada um com três colunas: datas, isolamento, casos (de covid)
    1. data frame para fitting, dados desde 'data_fit_ini' até 'data_fit_end'.
    2. data frame para validação, dados desde 'data_val_ini' até 'data_val_end'.
"""
import pandas as pd
from parameters import *
from numpy import arange


def loaddata() -> object:
    """

    Returns
    -------
    object
    """
    # carregando data do índice de isolamento
    print('Carregando data...')
    saopaulo_isol_data = pd.read_csv("data/SaoPaulo_isolamento.csv")
    saopaulo_isol_df = pd.DataFrame(saopaulo_isol_data)
    saopaulo_isol_df.drop(labels='Unnamed: 0', axis=1, inplace=True)
    saopaulo_isol_df.rename(columns={'Isol': 'Dados'}, inplace=True)
    saopaulo_isol_df.set_index('Data', inplace=True)
    saopaulo_isol_df = saopaulo_isol_df[data_fit_ini:data_fit_end]  # aqui corto os dados
    # -----------------------------------------------------------------------------------
    # Carregando os dados para São Paulo
    saopaulo_covid_df = pd.read_csv("data/SaoPaulo_dados_covid.csv")
    saopaulo_covid_df.drop(labels='Unnamed: 0', axis=1, inplace=True)
    saopaulo_covid_df.rename(columns={'datahora': 'Data'}, inplace=True)
    saopaulo_covid_df.set_index('Data', inplace=True)
    saopaulo_covid_fit_df = saopaulo_covid_df[data_fit_ini:data_fit_end]  # recorte dos dados para fitting
    # -----------------------------------------------------------------------------------
    # Preparando data para fitting
    dados_fit = pd.DataFrame(saopaulo_covid_fit_df['casos'])
    dados_fit.rename(columns={"casos": "Casos"}, inplace=True)
    dados_fit['Isol'] = saopaulo_isol_df['Dados'].values
    dados_fit['Idx'] = arange(0, dados_fit['Casos'].size, 1)
    dados_fit['Pop'] = int(saopaulo_covid_fit_df['pop'].mean())
    # -----------------------------------------------------------------------------------
    # Preparando data para validação
    dados_val = pd.DataFrame(saopaulo_covid_df[data_val_ini:data_val_end])  # recorte dos dados para validação
    dados_val.rename(columns={"casos": "Casos", "obitos": "Obitos", "pop": "Pop"}, inplace=True)
    print('Data loaded...OK!')
    return dados_fit, dados_val
