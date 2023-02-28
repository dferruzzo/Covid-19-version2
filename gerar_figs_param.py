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

def gerar_figs_param(params_df, dados_fit, dados_val, salvar_figs=True):
    #print('Param df:\n', params_df)
    params_val = params_df['Valor'].to_numpy()
    mu = params_val[0]
    gamma = params_val[1]
    alpha = params_val[2]
    beta1 = params_val[3]
    beta2 = params_val[4]
    beta3 = params_val[5]
    theta0 = params_val[6]
    theta1 = params_val[7]
    s0 = params_val[8]
    i0 = params_val[9]
    sick0 = params_val[10]
    tot_pop = params_val[11]
    theta_coef = polynomial.Polynomial([theta0, theta1])

    N = dados_val['Casos'].size
    #tot_pop = dados_fit['Pop'].to_numpy()[0]
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
    plt.plot(dados_val.index, dados_val['Casos'], 'o', label='Validation')
    plt.plot(dados_fit.index, dados_fit['Casos'], 'o', label='Fitting')
    plt.plot(dados_val.index, sol[:, 2] * tot_pop, linewidth=3, label='Model', color="forestgreen")
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
    plt.plot(dados_fit.index, dados_fit['Isol'], 'o', label='Real data')
    plt.plot(dados_fit.index, theta_coef(dados_fit['Idx'].to_numpy()), linewidth=3, label='First-order fitting')
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
