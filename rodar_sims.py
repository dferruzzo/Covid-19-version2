# Data: 07/03/2023
# Script para produzir as figuras 7 e 8
#
# Carrega as librarias e funções
from loaddata import *
from fit_isol import *
from fitting import *
from validation import *
from save_all import *
from load_all import *
from gerar_figs_param import *
from omega_gamma import *
from simulations import *
from mostrar_dados import *
from mapa1 import *
import pandas as pd
from serie_indice_isolamento import *
from tkinter import W
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from numpy import array
from myfunctions import rhs_vac, rk4, theta_func, rhs_vac_theta, theta_func_1
from numpy import polynomial, trapz
import time

salvar_figs = True

dados_para_fit, dados_para_val = loaddata()

# Carregando dados salvos
csv1 = 'dados_iso-2023-03-06-19-38-55.csv'
csv2 = 'dados_din-2023-03-06-19-38-55.csv'
# pega sempre os últimos gerados
#csv1 = filename_iso
#csv2 = filename_din
dados_fit_isol_saved, dados_fit_din_saved = load_all(csv1, csv2)

dados_din = dados_fit_din_saved
dados_iso = dados_fit_isol_saved

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
print('  theta crítico =', theta_c) 
print('  omega min =', omega_min)
print('  m =', m)
print('  b =', b)

omega_test = omega_theta(theta_test)
print('  theta_test =',theta_test)
print('  omega(theta)=', omega_test)
print('\n')
#

x0 = array([s0, i0, sick0])
t0 = 0
tf = 1500
h = 1

# Esses valores de theta e omega são utilizados para produzir a fig 7
# é preciso comentar toda essa parte para produzir a figura 8
"""
theta_test = 0.59 
omega = 0.00
t, sol = rk4(lambda t, x: rhs_vac_1(t, x, mu, gamma, alpha, theta_test, beta1, beta2, beta3, omega), x0, t0, tf, h)
#
plt.figure()
plt.plot(t[0:1400], sol[0:1400,2]*tot_pop, color='tab:blue')
plt.grid()
plt.ylabel('Confirmed cases')
plt.xlabel('days')
if salvar_figs:
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename = 'figures/sims_confirmed_cases_'+timestr+'.eps'
    plt.savefig(filename, format='eps', bbox_inches='tight')
plt.show()
"""

# Esses valores de theta e omega são utilizados para produzir a fig 8
# é preciso comentar toda essa parte para produzir a figura 7
theta_test = 0.0 
omega = 0.028
t, sol = rk4(lambda t, x: rhs_vac_1(t, x, mu, gamma, alpha, theta_test, beta1, beta2, beta3, omega), x0, t0, tf, h)
#
plt.figure()
fig, ax1 = plt.subplots()
ax1.set_xlabel('days')
ax1.set_ylabel('Confirmed cases', color='tab:blue')
ax1.plot(t[0:400], sol[0:400,2]*tot_pop, color='tab:blue')
ax1.ticklabel_format(axis='y',scilimits=(0,0),style='scientific')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Percentage of vaccinates (%)', color='tab:orange')
ax2.plot(t[0:400], sol[0:400,0]*omega*100, color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')
ax2.xaxis.get_visible()
ax2.grid('x')
if salvar_figs:
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename = 'figures/sims_confirmed_cases_'+timestr+'.eps'
    plt.savefig(filename, format='eps', bbox_inches='tight')
plt.show()

