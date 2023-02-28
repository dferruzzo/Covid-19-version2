from loaddata import *
from fit_isol import *
from fitting import *
from validation import *
from save_parameters import *
from load_params import *
from gerar_figs_param import *
from omega_gamma import *
from simulations import *
from mostrar_dados import *
from mapa1 import *

if __name__ != '__main__':
    pass
else:
    #
    #mostrar_dados() # <- Mostra todos os dados disponíveis
    #
    # Essa primeira parte faz o ajuste de parâmetros e gera um arquivo csv com os valores.
    #
    dados_fit, dados_val = loaddata() # <- carrega dados truncados
    #
    # Ajuste do índice de isolamento
    #
    theta_poly, stats, theta_coeffs = fit_isol(dados_fit, order=1, salvar_figs=False)
    # Ajuste de parâmetros
    param, x0, cov, desv = fitting(theta_poly, dados_fit, salvar_figs=False)
    # Validação
    validation(theta_poly, param, x0, dados_fit, dados_val, salvar_figs=False)
    # Salvar dados em arquivo csv com a data no nome.
    #save_parameters(theta_coeffs, param, x0, dados_fit)

    #nome_de_arquivo = 'parameters-2023-02-28-14-22-58.csv'
    #params_df = load_params(nome_de_arquivo)

    #gerar_figs_param(params_df, dados_fit, dados_val, salvar_figs=False)
    # 
    # Simulações
    #simulations(params_df, salvar_figs=False)
    #mapa1(params_df)
    # -----------------
    # Date: 28/fev/2023
    # TODO: 1. Calcular o erro quadrático médio no ajuste de parâmetros e na figura 6


