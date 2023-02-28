"""
Script para avaliar de forma gráfica a desigualdade que estabelece a estabilidade 
do equilibrio endêmico no modelo com vacina.

    w-((alpha(1-theta)/(beta1+beta2+mu))-1)(mu+gamma) <= 0

    ESSE SCRIPT NÃO É MAIS NECESSÁRIO!!!!

"""
from numpy import arange, array, meshgrid
import matplotlib.pyplot as plt

def omega_gamma(params_df):
    def condicao(omega, theta):
        params_val = params_df['Valor'].to_numpy()
        mu = params_val[0]
        gamma = params_val[1]
        alpha = params_val[2]
        beta1 = params_val[3]
        beta2 = params_val[4]
        beta3 = params_val[5]
        return omega-((alpha*(1-theta)/(beta1+beta2+mu))-1)*(mu+gamma)
    #
    omegas = arange(0, 1, 0.01)
    thetas = arange(0, 1, 0.01)
    Om, Th = meshgrid(omegas, thetas)
    Co = condicao(Om, Th)    
    #
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(Om, Th, Co, 50, cmap='binary')
    ax.set_xlabel('omega')
    ax.set_ylabel('theta')
    ax.set_zlabel('Condi')
    plt.show()
    return None
