"""
Script para fazer o ajuste dos parâmetros do modelo
---------------------------------------------------
Entrada:
    ajuste para o índice de isolamento e dataframe de dados para fazer o ajuste
Saída:
    popt : os parâmetros ajustados,
    X0   : a condição inicial da simulação,
    pvoc : matriz das covariâncias,
    perr : desvio padrão para cada parâmetro
"""
from parameters import *
from numpy import array, mean, dot, sqrt
from numpy.random import uniform
import scipy.optimize as optimize
from myfunctions import f, rk4, rhs
from numpy import sqrt, diag, min, max
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pprint

# TODO: 1. Calcular o erro quadrático médio no ajuste de parâmetros e na figura 6

def fitting(dados_fit_isol, dados, salvar_figs=True):
    #
    print('\nIniciando ajuste de parâmetros')
    print('------------------------------\n')
    #
    theta_t = dados_fit_isol['theta(t)']    # função polinomial que depende de t
    N = dados['Casos'].size # <- número de iterações
    tempo = dados['Idx'].to_numpy()
    casos = dados['Casos'].to_numpy()
    tot_pop = dados['Pop'].to_numpy()[0]
    # Parâmetros para optimização
    sigma = None
    absolute_sigma = False
    # checar se ha algum NaN ou InF nos dados
    check_finite = True
    # método de otimização (escolher um deles)
    # ‘dogbox’ : dogleg algorithm with rectangular trust regions,
    # 'trf' : Trust Region Reflective algorithm
    method = 'trf'
    # Jacobiano
    jac = None
    # condições iniciais
    sick0 = casos[0]/tot_pop
    i0_min = 1*sick0
    i0_max = 3*sick0 # (7) Os casos não reportados podem ser até 7 vezes os reportados
    #
    # organizando os parâmetros
    params_min = [gamma_min, alpha_min, beta1_min, beta2_min, beta3_min, i0_min]
    # organizando os parâmetros
    params_max = [gamma_max, alpha_max, beta1_max, beta2_max, beta3_max, i0_max]
    # organizando os vetores dos limites inferior e superior
    bounds = (params_min, params_max)
    # chute inicial para os parâmetros, para ajustar o resultado da simulação podemos ajustar esses chutes iniciais
    gamma_0 = uniform(gamma_min, gamma_max)
    alpha_0 = uniform(alpha_min, alpha_max)
    beta1_0 = uniform(beta1_min, beta1_max)
    beta2_0 = uniform(beta2_min, beta2_max)
    beta3_0 = uniform(beta3_min, beta3_max)
    i0_0 = uniform(i0_min, i0_max)
    s0_0 = 1-i0_0-sick0-0.9*sick0 # Os recuperados no Brasil são de 90% dos casos confirmados, 0.8*Sick
    #print('S0_0=', s0_0)
    # organizando os parâmetros
    p0 = array([gamma_0, alpha_0, beta1_0, beta2_0, beta3_0, i0_0])
    # a otimização
    # ------------
    print('Rodando otimização...')
    f_adj = lambda x, gamma, alpha, beta1, beta2, beta3, i: f(x, gamma, alpha, beta1, beta2, beta3, i, s0_0, sick0, theta_t, mu, N)
    popt, pvoc = optimize.curve_fit(f_adj, tempo, casos / tot_pop, p0, sigma, absolute_sigma, check_finite, bounds, method, jac)
    perr = sqrt(diag(pvoc))
    #
    gamma = popt[0]
    alpha = popt[1]
    beta1 = popt[2]
    beta2 = popt[3]
    beta3 = popt[4]
    i0 = popt[5]
    s0 = 1-i0-sick0
    x0 = array([s0, i0, sick0])
    #print('x0 =',x0)
    # rodando Runge-Kutta de 4ta ordem de passo fixo. Testando o ajuste
    # parameters
    t0 = 0
    tf = N - 1
    h = 1
    t, sol = rk4(lambda t, x: rhs(t, x, mu, gamma, alpha, theta_t, beta1, beta2, beta3),x0, t0, tf, h)

    # Cálculo do MSE e RMSE
    MSE = mean(((casos / tot_pop)- sol[:,2])**2)
    RMSE = sqrt(mean(((casos / tot_pop)- sol[:,2])**2 ))
    #print('Mean Squared Error: ', MSE)
    #print('Root Mean Squared Error: ', RMSE)
    ss_res = dot(((casos / tot_pop)- sol[:,2]),((casos / tot_pop)- sol[:,2]))
    ymean = mean(casos / tot_pop)
    ss_tot = dot(((casos / tot_pop)-ymean),((casos / tot_pop)-ymean))
    Mean_R = 1-ss_res/ss_tot
    #print('Mean R :', Mean_R)
    #
    # TODO [DONE]: (28/02/2023) Colocar o RMSE, MSE na saída para salvar os dados.
    #
    # ---------------------------------------------------------------------------------------------
    # print('sol shape =', sol.shape)
    # print('Num. Casos =', dados['Casos'].size)
    #plt.close('all')
    plt.figure()
    plt.plot(dados.index, dados['Casos'], 'o', label='Dados')
    plt.plot(dados.index, sol[:, 2] * tot_pop, linewidth=3, label='Otimização')
    #plt.plot(dados.index, ffit(dados['Idx'].to_numpy()), linewidth=3, label='Ajute de ordem ' + str(order))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.title('Ajuste dos dados de número de casos')
    plt.grid()
    plt.legend()
    plt.xticks(rotation=45)
    if salvar_figs:
       timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
       filename = 'figures/fitting_'+timestr+'.png'
       plt.savefig(filename,  bbox_inches='tight')
    plt.show()
    #
    dados = {
        'mu': mu,
        'gamma': gamma,
        'alpha': alpha,
        'beta1': beta1,
        'beta2': beta2,
        'beta3': beta3,
        'i0': i0,
        's0': s0,
        'sick0': sick0,
        'N': N,
        'pvoc': pvoc,       # matriz das covarianças dos coeffs.
        'perr': perr,       # desvio padrão
        'MSE': MSE,         # Mean Squared Error
        'RMSE': RMSE,       # Root Mean Squared Error
        'Mean_R': Mean_R,
        'ss_res': ss_res,   # Residuo
        'ss_tot':ss_tot     # Residuo total
            }
    print('\nDados após ajuste:\n')
    pprint.pprint(dados, sort_dicts=False)
    print('\nAjuste finalizado... OK!')
    # pronto para entregar na saída o dicionário 'dados'
    return dados