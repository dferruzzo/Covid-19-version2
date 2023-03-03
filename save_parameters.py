"""
NÃO ESTOU UTILIZANDO MAIS ESSA FUNÇÃO
NÃO FUNCIONA
DEIXADA AQUI APENAS COMO REFERÊNCIA DO QUE FOI FEITO
NO LUGAR ESTOU UTILIZNADO A FUNÇÃO save_all.py
#
Script para salvar dos parâmetros
-----------------------------------------------------------------------
Entrada: os coeficientes do polinômio theta obtidos pela função fit_isol
         e os coeficientes ajustados do modelo obtidos pela função 
         fitting.
         SÓ SALVA DOIS PARÂMETROS PARA THETA, THETA0 E THETA1.
         É A APROXIMAÇÃO DE PRIMEIRA ORDEM PARA THETA
Saída: Arquivo csv com os parâmetros, o nome do arquivo é 'parametros-data.csv' 

"""
from parameters import *
from pandas import DataFrame
import time

def save_parameters(theta_coeffs, param, x0, dados_fit):
    print('Salvando parametros...')
    gamma = param[0]
    alpha = param[1]
    beta1 = param[2]
    beta2 = param[3]
    beta3 = param[4]
    s0 = x0[0]
    i0 = x0[1]
    sick0 = x0[2]
    TotPop = dados_fit['Pop'].to_numpy()[0]
    parametros_otimos = {
        'Parametros': ['mu', 'gamma', 'alpha', 'beta1', 'beta2', 'beta3', 'theta0', 'theta1', 's0', 'i0', 'sick0', 'TotPop'],
        'Valor': [mu, gamma, alpha, beta1, beta2, beta3, theta_coeffs[0], theta_coeffs[1], s0, i0, sick0, TotPop]}
    parametros_df = DataFrame(data=parametros_otimos, columns=['Parametros', 'Valor'])
    print('Parametros:\n',parametros_df)
    print('Coeficientes theta:\n', theta_coeffs)  
    # criando o arquivo para guardar os dados.
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename = 'parameters-'+timestr+'.csv'
    print('filename:', filename)
    parametros_df.to_csv(filename, index=False)
    print('Parametros guardados no arquivo:', filename, '   OK!')
    return 
