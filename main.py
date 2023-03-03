from loaddata import *
from fit_isol import *
from fitting import *
from validation import *
from save_all import *
from load_all import *
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
    # Carrega os dados para fitting e para validação e salva os dados em arquivos .csv
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
    # Salvar dados em arquivos csv com a data no nome.
    save_all(dados_fit_isol, dados_fit_din)
    #
    # Carregando dados salvos
    #
    # Dados para ajuste de parâmetros
    csv1 = 'dados_para_fit-2023-03-03-10-28-13.csv'
    #
    # Dados para validação
    csv2 = 'dados_para_val-2023-03-03-10-28-13.csv'
    #
    # Dados estatisticos obtidos como resultado do ajuste do índice de isolamento
    csv3 = 'dados_iso-2023-03-03-10-29-47.csv'
    #
    # Dados obtidos como resultado do ajuste do número de infectados
    csv4 = 'dados_din-2023-03-03-10-29-47.csv'
    #
    dados_para_fit, dados_para_val, dados_iso, dados_din =\
        load_all(csv1, csv2, csv3,csv4)
    #
    # Gerar figuras
    #gerar_figs_param(params_df, dados_fit, dados_val, salvar_figs=False)
    # 
    # Simulações
    #simulations(params_df, salvar_figs=False)
    #
    # Produce o mapa
    #mapa1(params_df)
    # -----------------
    # Date: 01/mar/2023
    # TODO: [ ] 1. Calcular o erro quadrático médio no ajuste de parâmetros e na figura 6
    # TODO: [DONE] 1.1 modificar função fitting para entregar um dicionario
    # TODO: [DONE] 1.2 modificar função fit_isol para entregar um dicionario
    # TODO: [DONE] 1.3 modificar função validação para receber dois dicionarios
    # TODO: [DONE] 1.4 modificar função `save_parameters` ou `save_all` para receber dois dicionarios
    # TODO: [DONE] 1.5 Modificar `load_params` para carregar os dados guardados pela função anterior
    # TODO: [ ] 1.6 modificar função gerar figs_param para receber dois dicionarios
    # TODO: [ ] 1.7 modificar função simulations para receber dicionarios
    # TODO: [ ] 1.8 modificar função mapa1 para receber dicionarios