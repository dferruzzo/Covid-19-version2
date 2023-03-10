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
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from numpy import array, sqrt
from myfunctions import rhs, rk4
from numpy import polynomial
import time

salvar_figs = False

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
#Calcular o RMSE para a validação

def rmse(predictions, targets):
    return sqrt(((predictions - targets) ** 2).mean())

predictions = sol[:,2]*tot_pop
targets = dados_para_val['Casos'].to_numpy()

print('RMSE da validação normalizado com a população total=', rmse(predictions, targets)/tot_pop)