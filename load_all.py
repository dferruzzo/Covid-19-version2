"""
    Script para carregar todos os dados guardados em arquivos .csv

    Entrada: nome de quatro (4) arquivos .csv.

        - csv1: arquivo .csv de dados do fitting do índice de isolamento
        - csv2: arquivo .csv de dados do fitting donumero de infectados

    Saída: Quatro (04) data frame com os dados
"""
import pandas as pd

def load_all(csv1, csv2):
    #
    print('\nLoading data from file:', csv1)
    dados_iso = pd.read_csv(csv1).set_index('Nome') 
    #
    print('\nLoading data from file:', csv2)
    dados_din = pd.read_csv(csv2).set_index('Nome')
    #
    print('\nData loaded successfully...OK!\n')
    return dados_iso, dados_din