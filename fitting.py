"""
Script para fazer o ajuste dos parâmetros do modelo
---------------------------------------------------
Entrada:
    ajuste para o índice de isolamento e dataframe de dados para fazer o ajuste
Saída:
    popt : os parâmetros ajustados,
    pvoc : matriz das covariâncias,
    perr : desvio padrão para cada parâmetro
"""
from parameters import *
from numpy import array
from numpy.random import uniform
import scipy.optimize as optimize
from myfunctions import f, rk4, rhs
from numpy import sqrt, diag, min, max
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# TODO: [DONE] Melhorar esse chute inicial, é possível utilizar um método melhor, talvez random
# TODO: [DONE] A condição inicial do fitting deve ser compatível com os dados.

def fitting(theta_coef, dados, salvar_figs=True):
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
    print('S0_0=', s0_0)
    # organizando os parâmetros
    p0 = array([gamma_0, alpha_0, beta1_0, beta2_0, beta3_0, i0_0])
    # a otimização
    print('Rodando otimização...')
    f_adj = lambda x, gamma, alpha, beta1, beta2, beta3, i: f(x, gamma, alpha, beta1, beta2, beta3, i, s0_0, sick0, theta_coef, mu, N)
    popt, pvoc = optimize.curve_fit(f_adj, tempo, casos / tot_pop, p0, sigma, absolute_sigma, check_finite, bounds, method, jac)
    gamma = popt[0]
    alpha = popt[1]
    beta1 = popt[2]
    beta2 = popt[3]
    beta3 = popt[4]
    i0 = popt[5]
    s0 = 1-i0-sick0
    x0 = array([s0, i0, sick0])
    print('x0 =',x0)
    # rodando Runge-Kutta de 4ta ordem de passo fixo. Testando o ajuste
    # parameters
    t0 = 0
    tf = N - 1
    h = 1
    t, sol = rk4(lambda t, x: rhs(t, x, mu, gamma, alpha, theta_coef, beta1, beta2, beta3),x0, t0, tf, h)
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
    perr = sqrt(diag(pvoc))
    print('Desvio pardrão:')
    print('---------------')
    print(perr)
    print('Parameters:')
    print('-----------')
    print('mu =', mu)
    print('theta =', theta_coef)
    print('gamma =', gamma)
    print('alpha =', alpha)
    print('beta1 =', beta1)
    print('beta2 =', beta2)
    print('beta3 =', beta3)
    print('s0 =', s0)
    print('i0 =', i0)
    print('Ajuste finalizado... OK!')
    return popt, x0, pvoc, perr
