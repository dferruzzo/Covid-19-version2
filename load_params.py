"""
    Script para carregar parâmetros a partir de arquivo csv.

    Entrada: nome de arquivo csv.

    Saída: data frame com os parâmetros
"""
import pandas as pd
from parameters import *
#from pandas import DataFrame


def load_params(nome_arquivo):
    print('\nCarregando parâmetros do arquivo:', nome_arquivo)
    params_from_file = pd.read_csv(nome_arquivo)
    print('\n')
    print(params_from_file)
    print('\n')
    print('Parâmetros carregados com sucesso...OK!\n')
    return params_from_file 
