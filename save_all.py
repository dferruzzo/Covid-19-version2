"""
Script para salvar todos os dados gerados
-----------------------------------------------------------------------
Entrada:
    as listas:
    - dados_fit_isol
    - dados_fit_din   
Saída: 
    dois arquivos csv.
        O primeiro com os dados do ajuste do índice de isolamento.
        O segundo com os dados do ajuste da curva dos infectados.
"""
from parameters import *
import pandas as pd
import time

def save_all(dados_fit_isol, dados_fit_din):
    print('\nGuardando todos os dados...')

    # criando nome do arquivo para guardar os dados de ajuste do índice de isolamento e para os dados do ajuste da curva dos infectados
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename_iso = 'dados_iso-'+timestr+'.csv'
    filename_din = 'dados_din-'+timestr+'.csv'

    dados_fit_isol_df = pd. DataFrame(list(dados_fit_isol.items()), columns = ['Nome','Valor']).set_index('Nome')
    dados_fit_isol_df.to_csv(filename_iso)
    print('Dados ajustados de isolamento:\n', dados_fit_isol_df)    

    dados_fit_din_df = pd. DataFrame(list(dados_fit_din.items()), columns = ['Nome','Valor']).set_index('Nome')
    dados_fit_din_df.to_csv(filename_din)
    print('Dados ajustados para a dinâmica:\n', dados_fit_din_df)
    #
    print('\nDados do ajuste do indice de isolamento guardados no arquivo:')
    print(filename_iso,'.csv')
    print('\nDados do ajuste dos dos parâmetros do sistema guardados no arquivo:')
    print(filename_din,'.csv')
    # 
    # TODO [DONE]: (01/03/2023) Falta guardar a informação em arquivo.
    return 
