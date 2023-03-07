"""
mapa1(params_df, salvar_figs=False)

A função recebe os parâmetros do modelo,
cria uma grade de valores theta e omega
para cada um desses pares, roda uma simulação
de 0 a T e calcula o valor máximo dos sick.
devolve a grade theta - omega e a matriz 
com os valores pico dos sicks.
"""

from myfunctions import rk4, rhs_vac_1
from numpy import array, polynomial, linspace, meshgrid, shape, empty, nan, max
import matplotlib.pyplot as plt
import time

def mapa1(dados_para_val, dados_iso, dados_din, salvar_figs=False):
    
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
    # theta_coef = polynomial.Polynomial([theta0, theta1])
    
    tot_pop = tot_pop = dados_para_val['Pop'].to_numpy()[0]
 
    x0 = array([s0, i0, sick0])
    t0 = 0
    tf = 1000
    h = 1
    
    thetas = linspace(0, 0.5, 21)
    omegas = linspace(0, 0.05, 21)
    tt, ww = meshgrid(thetas, omegas, indexing='ij')
    sick_peaks = empty((len(tt),len(ww),))
    sick_peaks[:] = nan
    #print('shape of tt=', shape(tt))
    #print('shape of ww=', shape(ww))
    #print('len of tt=',len(tt))
    for i in range(len(tt)):
        for j in range(len(ww)):
            theta = tt[i,j]
            omega = ww[i,j]
            t, sol = rk4(lambda t, x: rhs_vac_1(t, x, mu, gamma, alpha, theta, beta1, beta2, beta3, omega), x0, t0, tf, h)
            sick_peaks[i,j] =  max(sol[:,2])*100 # em porcentagem
            #print('theta=',theta,' omega=',omega,' peak=',sick_peaks[i,j])
    h = plt.contour(tt, ww, sick_peaks, 10, colors='black')#cmap='RdGy')
    plt.clabel(h, inline=True,fontsize=8)
    #plt.imshow(sick_peaks
    #plt.colorbar()
    plt.xlabel('Isolation index')
    plt.ylabel('Vaccination rate')
    plt.plot([0, 0.59],[0.028,0],'--')
    #
    plt.annotate('$\omega_{min}$',(0,0.028),(-0.045,0.024),\
                 arrowprops=dict(arrowstyle="->"))
    plt.annotate('$\\theta_{c}$',(0.59,0),(0.58,0.004),\
                 arrowprops=dict(arrowstyle="->"))
    if salvar_figs:
       timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
       filename = 'figures/mapa_'+timestr+'.eps'
       plt.savefig(filename, format='eps', bbox_inches='tight')    
    plt.show()
    return None 
