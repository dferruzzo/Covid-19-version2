"""
Script para salvar todos os dados gerados
-----------------------------------------------------------------------
Entrada:
    as listas:
    - dados_fit_isol
    - dados_fit_din
    as panda Data Frames
    - dados_para_fit
    - dados_para_val
Saída: 

"""
from parameters import *
import pandas as pd
import time

def save_all(dados_fit_isol, dados_fit_din, dados_para_fit, dados_para_val):
    print('\nGuardando todos os dados...')

    dados_fit_isol_df = pd. DataFrame(list(dados_fit_isol.items()), columns = ['Nome','Valor'])
    print('Dados ajustados de isolamento:\n', dados_fit_isol_df)    

    dados_fit_din_df = pd. DataFrame(list(dados_fit_din.items()), columns = ['Nome','Valor'])
    print('Dados ajustados para a dinâmica:\n', dados_fit_din_df)
    #print('pvoc = ', dados_fit_din_df.'Nome'['10'])
    # 
    # TODO [ ]: (01/03/2023) Falta guardar a informação em arquivo.
    return 
