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

def mapa1(params_df, salvar_figs=False):
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
    #theta_coef = polynomial.Polynomial([theta0, theta1])
 
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
    plt.show()
    return None 
