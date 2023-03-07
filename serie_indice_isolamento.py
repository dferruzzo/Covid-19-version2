"""
Script carregar os dados da série completa do índice de isolamento
------------------------------------------------------------------
Não tem argumentos de entrada.
Produz uma figura de saída
"""
import pandas as pd
from parameters import *
from numpy import arange
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker


def serie_indice_isolamento():
    # carregando data do índice de isolamento
    print('Carregando dados do índice de isolamento...')
    df = pd.read_csv("data/SaoPaulo_isolamento.csv")    
    df.drop(labels='Unnamed: 0', axis=1, inplace=True)
    df.rename(columns={'Isol': 'Dados'}, inplace=True)
    df.set_index('Data', inplace=True)
    #
    plt.figure(figsize=(20,5), dpi=80)
    plt.plot(df.index, df['Dados'])
    plt.plot(df.index, df['Dados'],'o', color='tab:blue')
    plt.ylabel('Isolation Index')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0, decimals=0))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    plt.gca().grid(axis='y')
    plt.gca().annotate('', xy=(100,0.55), xytext=(200,0.55), arrowprops={'arrowstyle': '<->'}, va='center')
    plt.xticks(rotation=90)
    plt.show()
    #
    return