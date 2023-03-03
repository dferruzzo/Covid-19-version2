"""
    Script para carregar todos os dados guardados em arquivos .csv

    Entrada: nome de quatro (4) arquivos .csv.

        - csv1: arquivo .csv de dados para fitting
        - csv2: arquivo .csv de dados para validação
        - csv3: arquivo .csv de dados do fitting do índice de isolamento
        - csv4: arquivo .csv de dados do fitting donumero de infectados

    Saída: Quatro (04) data frame com os dados
"""
import pandas as pd

def load_all(csv1, csv2, csv3, csv4):
    #
    print('\nCarregando dados do arquivo:', csv1)
    dados_para_fit = pd.read_csv(csv1).set_index('Nome') 
    #
    print('\nCarregando dados do arquivo:', csv2)
    dados_para_val = pd.read_csv(csv2).set_index('Nome') 
    #
    print('\nCarregando dados do arquivo:', csv3)
    dados_iso = pd.read_csv(csv3).set_index('Nome') 
    #
    print('\nCarregando dados do arquivo:', csv4)
    dados_din = pd.read_csv(csv4).set_index('Nome') 
    #
    print('\nDados carregados com sucesso...OK!\n')
    return dados_para_fit, dados_para_val, dados_iso, dados_din