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
    #print('mu =', mu)
    gamma = float(dados_din.loc['gamma']['Valor'])
    #print('gamma =', gamma)
    alpha = float(dados_din.loc['alpha']['Valor'])
    #print('alpha =', alpha)
    beta1 = float(dados_din.loc['beta1']['Valor'])
    #print('beta1 =', beta1)
    beta2 = float(dados_din.loc['beta2']['Valor'])
    #print('beta2 =', beta2)
    beta3 = float(dados_din.loc['beta3']['Valor'])
    #print('beta3 =', beta3)
    i0 = float(dados_din.loc['i0']['Valor'])
    #print('i0 =', i0)
    s0 = float(dados_din.loc['s0']['Valor'])
    #print('s0 =', s0)
    sick0 = float(dados_din.loc['sick0']['Valor'])
    #print('sick0 =', sick0)
    #
    theta0 = float(dados_iso.loc['theta0']['Valor'])
    #print('theta0 =', theta0)
    theta1 = float(dados_iso.loc['theta1']['Valor'])
    #print('theta1 =', theta1)
    #
    N = dados_para_val['Casos'].size
    print('N =', N)
    tot_pop = dados_para_val['Pop'].to_numpy()[0]
    print('tot_pop =', tot_pop)
    theta_coef = polynomial.Polynomial([theta0, theta1])
    print('theta_t =', theta_coef)
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
        filename = 'figures/validacao_numero_casos_'+timestr+'.eps'
        plt.savefig(filename, format='eps', bbox_inches='tight')
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
        filename = 'figures/validacao_isolamento_'+timestr+'.eps'
        plt.savefig(filename, format='eps', bbox_inches='tight')

    plt.show()
    return None
