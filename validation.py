"""
Script para fazer a validação do ajuste dos parâmetros do modelo
----------------------------------------------------------------
Entrada:
    * coeficientes do polinômio que descreve theta
    * parâmetros do modelo obtidos com o fitting
    * dados utilizados no ajuste fitting
    * dados para validar
Saída:
    Nenhuma
"""
from parameters import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from numpy import array
from myfunctions import rhs, rk4


def validation(dados_fit_isol,  dados_fit_din, dados_para_fit, dados_para_val, salvar_figs=True):

    theta_t = dados_fit_isol['theta(t)']
     
    N = dados_para_val['Casos'].size
    tot_pop = dados_para_val['Pop'].to_numpy()[0]
    #
    gamma = dados_fit_din['gamma']
    alpha = dados_fit_din['alpha']
    beta1 = dados_fit_din['beta1']
    beta2 = dados_fit_din['beta2']
    beta3 = dados_fit_din['beta3']
    s0 = dados_fit_din['s0']
    i0 = dados_fit_din['i0']
    sick0 = dados_fit_din['sick0']
    #
    # parameters
    t0 = 0
    tf = N - 1
    h = 1
    x0 = array([s0, i0, sick0])
    #
    t, sol = rk4(
        lambda t, x: rhs(t, x, mu, gamma, alpha, theta_t, beta1, beta2, beta3),
        x0, t0, tf, h)
    #
    # 1. Gráfico dos dados para validação
    plt.plot(dados_para_val.index, dados_para_val['Casos'], 'o', label='Validação')
    #
    # 2. Gráfico dos dados para ajuste
    plt.plot(dados_para_fit.index, dados_para_fit['Casos'], 'o', label='Ajuste')

    # 3. Gráfico da curva ajustada
    plt.plot(dados_para_val.index, sol[:, 2] * tot_pop, linewidth=3, label='Otimização', color="green")
    #
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.title('Número de casos')
    plt.grid()
    plt.legend()
    # 
    # Se opção salvar figuras é TRUE,
    if salvar_figs:
       timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
       filename = 'figures/validacao_'+timestr+'.png'
       plt.savefig(filename,  bbox_inches='tight')
    plt.show()
    return None
