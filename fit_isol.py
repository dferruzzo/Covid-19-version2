"""
Script para fazer o ajuste polinomial dos dados de isolamento
-------------------------------------------------------------
Entrada:
    Data frame com dos dados de isolamento
Saída:
    Objeto polinômio com os coeficientes.
"""

from numpy.polynomial import polynomial as poly
from numpy import polynomial
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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
    ffit = polynomial.Polynomial(coefs)
    plt.close('all')
    plt.plot(dados.index, dados['Isol'], 'o', label='Dados')
    plt.plot(dados.index, ffit(dados['Idx'].to_numpy()), linewidth=3, label='Ajute de ordem ' + str(order))
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
    print('Coeficientes:')
    print('-------------')
    print(coefs)
    print('Estatisticas:')
    print('-------------')
    print(stats)
    print('Ajuste...OK!')
    return ffit, stats, coefs
