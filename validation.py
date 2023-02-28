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


def validation(theta_coef_1, param, x0, dados_fit, dados_val, salvar_figs=True):
    N = dados_val['Casos'].size
    tot_pop = dados_fit['Pop'].to_numpy()[0]
    gamma = param[0]
    alpha = param[1]
    beta1 = param[2]
    beta2 = param[3]
    beta3 = param[4]
    #s0 = param[5]
    #i0 = 1 - s0
    #x0 = array([s0, i0, 0])

    # parameters
    t0 = 0
    tf = N - 1
    h = 1
    t, sol = rk4(
        lambda t, x: rhs(t, x, mu, gamma, alpha, theta_coef_1, beta1, beta2, beta3),
        x0, t0, tf, h)
    #
    plt.plot(dados_val.index, dados_val['Casos'], 'o', label='Validação')
    plt.plot(dados_fit.index, dados_fit['Casos'], 'o', label='Ajuste')
    plt.plot(dados_val.index, sol[:, 2] * tot_pop, linewidth=3, label='Otimização', color="green")
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.title('Número de casos')
    plt.grid()
    plt.legend()
    if salvar_figs:
       timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
       filename = 'figures/validacao_'+timestr+'.png'
       plt.savefig(filename,  bbox_inches='tight')
    plt.show()
    return None
