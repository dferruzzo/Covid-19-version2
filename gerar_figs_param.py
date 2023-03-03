"""
    Script para gerar as figuras do ajuste de theta e dos ajustes de parâmetros
    para a população SICKS com validação.

    Entrada: Dataframe com os parâmetros

    Saída: As figuras
"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from numpy import array
from myfunctions import rhs, rk4
from numpy import polynomial
import time


def gerar_figs_param(dados_para_fit, dados_para_val, dados_iso, dados_din, salvar_figs=True):
    
    mu = float(dados_din.loc['mu']['Valor'])
    gamma = float(dados_din.loc['gamma']['Valor'])
    alpha = float(dados_din.loc['alpha']['Valor'])
    beta1 = float(dados_din.loc['beta1']['Valor'])
    beta2 = float(dados_din.loc['beta2']['Valor'])
    beta3 = float(dados_din.loc['beta3']['Valor'])
    i0 = float(dados_din.loc['i0']['Valor'])
    s0 = float(dados_din.loc['s0']['Valor'])
    sick0 = float(dados_din.loc['sick0']['Valor'])
    #
    theta0 = float(dados_iso.loc['Coeficientes']['Valor'][1:15])
    theta1 = float(dados_iso.loc['Coeficientes']['Valor'][16:30])
    #
    N = dados_para_val['Casos'].size
    tot_pop = dados_para_val['Pop'].to_numpy()[0]
    theta_coef = polynomial.Polynomial([theta0, theta1])
    #
    x0 = array([s0, i0, sick0])
    # 
    t0 = 0
    tf = N - 1
    h = 1
    t, sol = rk4(
        lambda t, x: rhs(t, x, mu, gamma, alpha, theta_coef, beta1, beta2, beta3),
        x0, t0, tf, h)
    #
    plt.figure()
    plt.plot(dados_para_val.index, dados_para_val['Casos'], 'o', label='Validation')
    plt.plot(dados_para_fit.index, dados_para_fit['Casos'], 'o', label='Fitting')
    plt.plot(dados_para_val.index, sol[:, 2] * tot_pop, linewidth=3, label='Model', color="forestgreen")
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.ylabel('Confirmed cases')
    #plt.title('Número de casos')
    plt.grid()
    plt.legend()
    if salvar_figs: 
        timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
        filename = 'figures/validacao_numero_casos_'+timestr+'.png'
        plt.savefig(filename,  bbox_inches='tight')
    #plt.show()
    #
    plt.figure()
    plt.plot(dados_para_fit.index, dados_para_fit['Isol'], 'o', label='Real data')
    plt.plot(dados_para_fit.index, theta_coef(dados_para_fit['Idx'].to_numpy()), linewidth=3, label='First-order fitting')
    plt.ylim((0, 0.6))  # set the ylim to bottom, top
    ##plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    #plt.title('Ajuste dos dados de isolamento')
    plt.ylabel('Isolation index')
    plt.grid()
    plt.legend()
    # plt.xticks(rotation=45)
    if salvar_figs:
        timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
        filename = 'figures/validacao_isolamento_'+timestr+'.png'
        plt.savefig(filename,  bbox_inches='tight')
    plt.show()
    return None
