"""
Data: 06/03/2023

Script para realizar simulações do sistema com vacina
com os parâmetros obtidos pelo ajuste feito.

"""
from tkinter import W
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from numpy import array
from myfunctions import rhs_vac, rk4, theta_func, rhs_vac_theta, theta_func_1
from numpy import polynomial, trapz
import time


def simulations(dados_para_fit, dados_para_val, dados_iso, dados_din, save_figs=True):
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
    theta0 = float(dados_iso.loc['theta0']['Valor'])
    theta1 = float(dados_iso.loc['theta1']['Valor'])
    theta_coef = polynomial.Polynomial([theta0, theta1])
    #
    tot_pop = tot_pop = dados_para_val['Pop'].to_numpy()[0]
    #
    # Calcular theta_c e omega_min
    theta_c = 1-((beta1+beta2+mu)/alpha)
    omega_min = ((alpha/(beta1+beta2+mu))-1)*(mu+gamma)
    m = alpha*(gamma+mu)/(beta1+beta2+mu)
    b = ((alpha/(beta1+beta2+mu))-1)*(gamma+mu)
    def omega_theta(theta_t):return -m*theta_t+b
    print('\n')
    print('  omega = -m*theta+b')
    print('  theta critical =', theta_c) 
    print('  omega min =', omega_min)
    print('  m =', m)
    print('  b =', b)
    #theta_test = 0.45
    theta_test = 0.6
    omega_test = omega_theta(theta_test)
    print('  theta_test =',theta_test)
    print('  omega(theta)=', omega_test)
    print('\n')
    #
    omega = 0.004
    #
    x0 = array([s0, i0, sick0])
    # 
    t0 = 0
    tf = 10000
    h = 1
    t, sol = rk4(lambda t, x: rhs_vac(t, x, mu, gamma, alpha, theta_coef, beta1, beta2, beta3, omega), x0, t0, tf, h)
    #t, sol = rk4(lambda t, x: rhs_vac_theta(t, x, mu, gamma, alpha, theta_coef, beta1, beta2, beta3, omega), x0, t0, tf, h)
    #
    # casos confirmados e vacinação juntos num gráfico.
    """
    plt.figure()
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('days')
    ax1.set_ylabel('Confirmed cases', color='tab:blue')
    ax1.plot(t, sol[:,2]*tot_pop, color='tab:blue')
    ax1.ticklabel_format(axis='y',scilimits=(0,0),style='scientific')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Percentage of vaccinates (%)', color='tab:orange')
    ax2.plot(t, sol[:,0]*omega*100, color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')
    ax2.xaxis.get_visible()
    ax2.grid('x')
    """
    #
    # gráfico dos susceptíveis e dos sicks
    plt.figure()
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('days')
    ax1.set_ylabel('Confirmed cases', color='tab:blue')
    #ax1.plot(t, sol[:,2]*tot_pop, color='tab:blue')
    ax1.plot(t[0:1000], sol[0:1000,2]*tot_pop, color='tab:blue')
    ax1.ticklabel_format(axis='y',scilimits=(0,0),style='scientific')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Susceptivel population', color='tab:orange')
    ax2.plot(t[0:1000], sol[0:1000,0]*tot_pop, color='tab:orange')
    #ax2.plot(t, sol[:,0]*tot_pop, color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')
    ax2.ticklabel_format(axis='y',scilimits=(0,0),style='scientific')
    #ax2.xaxis.get_visible()
    ax2.grid('x')    
    #plt.title('Número de casos confirmados, $\omega=$'+str(omega))
    #plt.ylabel('Confirmed cases')
    #plt.ticklabel_format(axis='y',scilimits=(0,0),style='scientific')
    #plt.xlabel('days')
    #plt.grid()
    if save_figs:
        timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
        filename = 'figures/sims_num_casos_'+timestr+'.eps'
        plt.savefig(filename, format='eps', bbox_inches='tight')
    #plt.show()
    # Número de vacinados
    #Num_vacc = trapz(sol[:,0]*omega, dx=1)
    #print('Porcentagem acumulado de vacinados =', Num_vacc)
    #plt.figure()
    #plt.plot(t, sol[:,0]*omega*100)
    #plt.xlabel('days')
    #plt.ylabel('Percentage of vaccinated')
    #plt.grid()
    #
    # Isolamento
    #plt.figure()
    #plt.plot(t[0:1000], theta_func_1(t[0:1000]))
    #plt.grid()
    #plt.title('Índice de Isolamento')
    #plt.ylabel('Isolation Index')
    #plt.xlabel('dias')
    #plt.axis([0, 1000, 0, 0.6])
    #if save_figs:
    #   timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    #   filename = 'figures/sims_isolamento_'+timestr+'.png'
    #   plt.savefig(filename,  bbox_inches='tight')
    #plt.show()
    
    # Diagrama de fase sicks x susceptíveis
    plt.figure()
    #plt.plot(sol[:,2], sol[:,0])
    plt.plot(sol[:,2]*tot_pop, sol[:,0]*tot_pop)
    plt.grid()
    plt.xlabel('$s_{ick}(t)$')
    #ax2.ticklabel_format(axis='y',scilimits=(0,0),style='scientific')
    plt.ticklabel_format(axis='x',scilimits=(0,0),style='scientific')
    plt.ylabel('$s(t)$')
    if save_figs:
       timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
       filename = 'figures/sims_fase_'+timestr+'.eps'
       plt.savefig(filename, format='eps', bbox_inches='tight')
    plt.show()
    return None
