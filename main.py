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
    # Essa primeira parte faz o fitting e gera um arquivo csv com os valores.
    #
    #dados_fit, dados_val = loaddata() # <- carrega dados truncados
    #
    # Ajuste do índice de isolamento
    #
    #theta_poly, stats, theta_coeffs = fit_isol(dados_fit, order=1, salvar_figs=False)
    # Fitting
    #param, x0, cov, desv = fitting(theta_poly, dados_fit, salvar_figs=False)
    # Validação
    #validation(theta_poly, param, x0, dados_fit, dados_val, salvar_figs=False)
    # Salvar dados
    #save_parameters(theta_coeffs, param, x0, dados_fit)

    nome_de_arquivo = 'parameters-2022-08-19-14-22-55.csv'
    params_df = load_params(nome_de_arquivo)

    #gerar_figs_param(params_df, dados_fit, dados_val, salvar_figs=False)
    # 
    # Simulações
    # TODO: 1. [DONE] Computar os parâmetros de bifurcação para os dados fitados
    # TODO: 2. [DONE] Rodar simulações com omega = 0 e theta = theta_c.
    # TODO: 3. [DONE] Rodar simulações com omega = omega_min e theta = 0.
    # TODO: 4. [DONE] Gráfico com theta com periodicidade semanal
    # TODO: 6. [DONE] Gráfico com theta com periodicidade semestral em equilíbrio endêmico.
    #simulations(params_df, salvar_figs=False)
    #mapa1(params_df)
    # -----------------
    # Date: 28/fev/2023
    # TODO: 1. Calcular o erro quadrático no fitting e na figura 6


