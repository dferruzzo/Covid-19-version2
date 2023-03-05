"""
Script para fazer o ajuste polinomial dos dados de isolamento
-------------------------------------------------------------
Entrada:
    Data frame com dos dados de isolamento
Saída:
    Objeto polinômio com os coeficientes.
"""
from parameters import *
from numpy.polynomial import polynomial as poly
from numpy import polynomial
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pprint

def fit_isol(dados, order=2, salvar_figs=True) -> object:
    """

    Returns
    -------
    object
    """
    # Ajustando os polinômios com dados crus
    print('Ajuste do polinômio de ordem', order, 'para os dados de isolamento.')
    poly_order = order
    x = dados['Idx'].to_numpy()
    coefs, stats = poly.polyfit(x, dados['Isol'].to_numpy(), poly_order, full=True)

    # cria uma função polynomial com os coeficientes 'coef' que pode ser avaliado diretamente como fitt(t), limitada a 'theta_min' e 'theta_max'
    ffit = polynomial.Polynomial(coefs, domain=[x[0], x[-1]], window=[theta_min, theta_max])
    
    plt.close('all')
    plt.plot(dados.index, dados['Isol'], 'o', label='Dados')
    plt.plot(dados.index, ffit(x), linewidth=3, label='Ajute de ordem ' + str(order))
    plt.ylim((0, 0.6))  # set the ylim to bottom, top
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.title('Ajuste dos dados de isolamento')
    plt.grid()
    plt.legend()
    plt.xticks(rotation=45)
    if salvar_figs:
       timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
       filename = 'figures/ajuste_isolamento_'+timestr+'.png'
       plt.savefig(filename,  bbox_inches='tight')
    plt.show()
    #
    dados = {
        'theta(t)' : ffit,           # polinômio theta(t)
        'theta0' : coefs[0],        # primeiro coeficiente do polinômio para theta(t)
        'theta1' : coefs[1],        # segundo coeficiente do polinômio para theta(t)
        'Residuos': stats[0],       # residuals – sum of squared residuals of the least squares fit
        'rank': stats[1],           # rank – the numerical rank of the scaled Vandermonde matrix
        'sing_values': stats[2],    # singular_values – singular values of the scaled Vandermonde matrix
        'rcond': stats[3]           # Relative condition number of the fit.
    }

    #print('testando a função thets(t), t= ', x[0]-10, 'theta(t>t_max) =', ffit(x[0]-10))
    
    print('\nDados após ajuste do índice de isolamento:\n')
    pprint.pprint(dados, sort_dicts=False)
    print('\nAjuste do índice de isolamento finalizado... OK!')
    # pronto para entregar na saída o dicionário 'dados'
    return dados
