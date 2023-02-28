"""
Script para mostrar todos os dados disponíveis
data: 18/08/2022
"""

import pandas as pd
#from parameters import *
#from numpy import arange
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def mostrar_dados():
    print('Carregando data...\n')
    # Dados do isolamento na cidade de São Paulo
    saopaulo_isol_data = pd.read_csv("data/SaoPaulo_isolamento.csv")
    print('Dados do isolamento na cidade de Sao Paulo')
    print('------------------------------------------')
    print(saopaulo_isol_data)
    plt.figure()
    plt.plot(saopaulo_isol_data['Data'], saopaulo_isol_data['Isol'], 'o')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.xticks(rotation=45)
    plt.grid()
    plt.title('Dados dos isolamento na cidade de São Paulo')
    plt.savefig('figures/dados_isolamento.png', bbox_inches='tight')
    #plt.show(block=False)
    # Dados do Covid na Cidade de São Paulo
    saopaulo_covid_df = pd.read_csv("data/SaoPaulo_dados_covid.csv")
    print('Dados de Covid-19 na cidade de Sao Paulo')
    print('----------------------------------------')
    print(saopaulo_covid_df)
    plt.figure()
    plt.plot(saopaulo_covid_df['datahora'], saopaulo_covid_df['casos'], 'o')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.xticks(rotation=45)
    plt.grid()
    plt.title('Dados dos casos confirmados na cidade de São Paulo')
    plt.savefig('figures/dados_casos_confirmados.png', bbox_inches='tight')
    #plt.show(block=False)
    plt.figure()
    plt.plot(saopaulo_covid_df['datahora'], saopaulo_covid_df['obitos'], 'o')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.xticks(rotation=45)
    plt.grid()
    plt.title('Dados dos obitos na cidade de São Paulo')
    plt.savefig('figures/dados_obitos.png', bbox_inches='tight')
    plt.show()
    return None
