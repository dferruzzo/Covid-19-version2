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
from load_all import *
from parameters import *

def save_all(dados_fit_isol, dados_fit_din, show=False, verify=False):
    print('\nGuardando todos os dados...')

    # criando nome do arquivo para guardar os dados de ajuste do índice de isolamento e para os dados do ajuste da curva dos infectados
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename_iso = 'dados_iso-'+timestr+'.csv'
    filename_din = 'dados_din-'+timestr+'.csv'

    dados_fit_isol_df = pd. DataFrame(list(dados_fit_isol.items()), columns = ['Nome','Valor']).set_index('Nome')
    dados_fit_isol_df.to_csv(filename_iso)
    
    dados_fit_din_df = pd. DataFrame(list(dados_fit_din.items()), columns = ['Nome','Valor']).set_index('Nome')
    dados_fit_din_df.to_csv(filename_din)
    
    if show:
        print('Dados ajustados de isolamento:\n', dados_fit_isol_df)    
        print('Dados ajustados para a dinâmica:\n', dados_fit_din_df)
    #
    print('\nDados do ajuste do indice de isolamento guardados no arquivo:')
    print(filename_iso,'.csv')
    print('\nDados do ajuste dos dos parâmetros do sistema guardados no arquivo:')
    print(filename_din,'.csv')
    # 
    # Esta parte do código Verifica a qualidade dos dados produzidos pelo ajuste e dos dados recuperados depois de salvar
    # -------------------------------------------------------------------------------------------------------------------
    if verify:
        # TODO [ ]: Escrever programa para verificar se após guardar e carregar todos os valores são os mesmos
        # Compararação dos dados do ajuste no índice de isolamento
        # --------------------------------------------------------
        #
        print('Verificando a qualidade dos dados guardados e recuperados\n')
        # Os coeficientes guardados estão na forma de pandas data frame        
        dados_fit_isol_saved, dados_fit_din_saved = load_all(filename_iso, filename_din)
        #
        # Os coeficientes do polinômio em theta originais são
        theta0 = dados_fit_isol['theta0']
        theta1 = dados_fit_isol['theta1']
        #        
        # comparando os coeficientes de theta(t)
        theta0_saved = float(dados_fit_isol_saved.loc['theta0']['Valor'])
        theta1_saved = float(dados_fit_isol_saved.loc['theta1']['Valor'])
        #        
        print('\nComparando dados dos coeficientes do polinômio theta(t):\n')
        print('| theta0 - theta0_saved | =', abs(theta0-theta0_saved))
        print('| theta1 - theta1_saved | =', abs(theta1-theta1_saved))
        #
        # comparando os parâmetros ajustados do modelo
        #
        # Os coeficientes originais são:
        # mu está no arquivo parameteres.py
        gamma = dados_fit_din['gamma']
        alpha = dados_fit_din['alpha']
        beta1 = dados_fit_din['beta1']
        beta2 = dados_fit_din['beta2']
        beta3 = dados_fit_din['beta3']
        s0 = dados_fit_din['s0']
        i0 = dados_fit_din['i0']
        sick0 = dados_fit_din['sick0']
        #
        # Os coeficientes guardados e recuperados são:
        mu_saved = float(dados_fit_din_saved.loc['mu']['Valor'])
        gamma_saved = float(dados_fit_din_saved.loc['gamma']['Valor'])
        alpha_saved = float(dados_fit_din_saved.loc['alpha']['Valor'])
        beta1_saved = float(dados_fit_din_saved.loc['beta1']['Valor'])
        beta2_saved = float(dados_fit_din_saved.loc['beta2']['Valor'])
        beta3_saved = float(dados_fit_din_saved.loc['beta3']['Valor'])
        i0_saved = float(dados_fit_din_saved.loc['i0']['Valor'])
        s0_saved = float(dados_fit_din_saved.loc['s0']['Valor'])
        sick0_saved = float(dados_fit_din_saved.loc['sick0']['Valor'])
        #
        print('\nComparando dados dos parâmetros ajustados:\n')
        print('| mu - mu_saved | =', abs(mu-mu_saved))
        print('| gamma - gamma_saved | =', abs(gamma-gamma_saved))
        print('| beta1 - beta1_saved | =', abs(beta1-beta1_saved))
        print('| beta2 - beta2_saved | =', abs(beta2-beta2_saved))
        print('| beta3 - beta3_saved | =', abs(beta3-beta3_saved))
        print('| s0 - s0_saved |       =', abs(s0-s0_saved))
        print('| i0 - i0_saved |       =', abs(i0-i0_saved))
        print('| sick0 - sick0_saved | =', abs(sick0-sick0_saved),'\n')
        #
    return filename_iso, filename_din
