from loaddata import *
from fit_isol import *
from fitting import *
from validation import *
from save_parameters import *
from save_all import *
from load_params import *
from gerar_figs_param import *
from omega_gamma import *
from simulations import *
from mostrar_dados import *
from mapa1 import *

if __name__ != '__main__':
    pass
else:
    # Mostra todos os dados disponíveis
    #mostrar_dados()
    #
    # Carrega os dados para fitting e para validação
    dados_para_fit, dados_para_val = loaddata()
    #
    # Ajuste do índice de isolamento
    dados_fit_isol = fit_isol(dados_para_fit, order=1, salvar_figs=False)
    #
    # Ajuste de parâmetros para os sicks
    dados_fit_din = fitting(dados_fit_isol, dados_para_fit, salvar_figs=False)
    #
    # Validação do fitting anterior
    validation(dados_fit_isol, dados_fit_din, dados_para_fit, dados_para_val, salvar_figs=False)
    #
    # Salvar dados em arquivo csv com a data no nome.
    #save_parameters(theta_coeffs, param, x0, dados_fit)
    save_all(dados_fit_isol, dados_fit_din, dados_para_fit, dados_para_val)
    #
    #nome_de_arquivo = 'parameters-2023-02-28-14-22-58.csv'
    #params_df = load_params(nome_de_arquivo)

    #gerar_figs_param(params_df, dados_fit, dados_val, salvar_figs=False)
    # 
    # Simulações
    #simulations(params_df, salvar_figs=False)
    #mapa1(params_df)
    # -----------------
    # Date: 01/mar/2023
    # TODO: [ ] 1. Calcular o erro quadrático médio no ajuste de parâmetros e na figura 6
    # TODO: [DONE] 1.1 modificar função fitting para entregar um dicionario
    # TODO: [DONE] 1.2 modificar função fit_isol para entregar um dicionario
    # TODO: [DONE] 1.3 modificar função validação para receber dois dicionarios
    # TODO: [ ] 1.4 modificar função save_parameters para receber dois dicionarios
    # TODO: [ ] 1.5 modificar função gerar figs_param para receber dois dicionarios
    # TODO: [ ] 1.6 modificar função simulations para receber dicionarios
    # TODO: [ ] 1.7 modificar função mapa1 para receber dicionarios


