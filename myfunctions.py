def rk4(f, x0, t0, tf, h):
    # Implementa algoritmo Runge-Kutta de 4ta ordem
    # dotx = f(t,x)
    # x0 = numpy.array([x1,...,xn]),
    # t0 : tempo inicial
    # tf : tempo final
    # h : passo de integração
    # as saídas são:
    # t : o vetor tempo 
    # x : o vetor de estados
    from numpy import zeros, absolute, floor
    N = absolute(floor((tf - t0) / h)).astype(int)
    x = zeros((N + 1, x0.size))
    t = zeros(N + 1)
    x[0, :] = x0
    t[0] = t0
    for i in range(0, N):
        k1 = f(t[i], x[i])
        k2 = f(t[i] + h / 2, x[i] + (h * k1) / 2)
        k3 = f(t[i] + h / 2, x[i] + (h * k2) / 2)
        k4 = f(t[i] + h, x[i] + h * k3)
        x[i + 1, :] = x[i, :] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t[i + 1] = t[i] + h
    return t, x


def modelo_1(t, x, p):
    import numpy as np
    # O lado direito da função    
    # ds/dt = mu + gamma - alpha(1-theta)*s*i - (mu + gamma)*s - gamma*i - gamma*sick
    # di/dt = alpha*(1-theta)*s*i - (beta1 + beta2 + mu)*i
    # dsick/dt = beta2*i - (beta3 + mu)* sick
    #
    # this is the right-hand side funtion, implemented for numertical integration
    s = x[0]
    i = x[1]
    sick = x[2]
    mu = p[0]
    gamma = p[1]
    alpha = p[2]
    theta = p[3]
    beta1 = p[4]
    beta2 = p[5]
    beta3 = p[6]
    return np.array([mu + gamma - alpha * (1 - theta) * s * i - (mu + gamma) * s - gamma * i - gamma * sick,
                     alpha * (1 - theta) * s * i - (beta1 + beta2 + mu) * i,
                     beta2 * i - (beta3 + mu) * sick])


def modelo_vac_1(t, x, p):
    import numpy as np
    # O lado direito da função    
    # ds/dt = mu + gamma - alpha(1-theta)*s*i - (mu + gamma + omega)*s - gamma*i - gamma*sick
    # di/dt = alpha*(1-theta)*s*i - (beta1 + beta2 + mu)*i
    # dsick/dt = beta2*i - (beta3 + mu)* sick
    #
    # this is the right-hand side funtion, implemented for numertical integration
    s = x[0]
    i = x[1]
    sick = x[2]
    mu = p[0]
    gamma = p[1]
    alpha = p[2]
    theta = p[3]
    beta1 = p[4]
    beta2 = p[5]
    beta3 = p[6]
    omega = p[7]
    return np.array([mu + gamma - alpha * (1 - theta) * s * i - (mu + gamma + omega) * s - gamma * i - gamma * sick,
                     alpha * (1 - theta) * s * i - (beta1 + beta2 + mu) * i,
                     beta2 * i - (beta3 + mu) * sick])


def vacinados(t, x, p):
    import numpy as np
    # função para ser avaliada durante a integração numérica
    s = x[0]
    # i = x[1]
    # sick = x[2]
    # mu = p[0]
    # gamma = p[1]
    # alpha = p[2]
    # theta = p[3]
    # beta1 = p[4]
    # beta2 = p[5]
    # beta3 = p[6]
    omega = p[7]
    return np.array([omega * s])

def rhs_vac_theta(t, x, *p):
    from parameters import theta_min, theta_max
    # O lado direito da função    
    # ds/dt = mu + gamma - alpha(1-theta)*s*i - (mu + gamma + omega)*s - gamma*i - gamma*sick
    # di/dt = alpha*(1-theta)*s*i - (beta1 + beta2 + mu)*i
    # dsick/dt = beta2*i - (beta3 + mu)* sick
    #
    # this is the right-hand side funtion, implemented for numertical integration

    from numpy import array
    # verificando número de argumentos
    if len(p) != 8:
        raise Exception("Erro no número de parâmetros!")
    s = x[0]
    i = x[1]
    sick = x[2]
    #
    mu = p[0]
    gamma = p[1]
    alpha = p[2]
    theta = p[3]
    beta1 = p[4]
    beta2 = p[5]
    beta3 = p[6]
    omega = p[7]
    # limitar theta
    def theta_lim(t):
        if theta(t) <= theta_min:
            return theta_min    
        elif theta(t) >= theta_max:
            return theta_max
        else:
            return theta(t)
    #print('theta(t)=',theta_lim(t))
    #
    return array([mu + gamma - alpha * (1 - theta_func_1(t)) * s * i - (mu + gamma + omega) * s - gamma * i - gamma * sick,
                  alpha * (1 - theta_func_1(t)) * s * i - (beta1 + beta2 + mu) * i,
                  beta2 * i - (beta3 + mu) * sick])


def rhs_vac_1(t, x, *p):
    from parameters import theta_min, theta_max
    # O lado direito da função    
    # ds/dt = mu + gamma - alpha(1-theta)*s*i - (mu + gamma + omega)*s - gamma*i - gamma*sick
    # di/dt = alpha*(1-theta)*s*i - (beta1 + beta2 + mu)*i
    # dsick/dt = beta2*i - (beta3 + mu)* sick
    #
    # this is the right-hand side funtion, implemented for numertical integration

    from numpy import array
    # verificando número de argumentos
    if len(p) != 8:
        raise Exception("Erro no número de parâmetros!")
    s = x[0]
    i = x[1]
    sick = x[2]
    #
    mu = p[0]
    gamma = p[1]
    alpha = p[2]
    theta = p[3]
    beta1 = p[4]
    beta2 = p[5]
    beta3 = p[6]
    omega = p[7]
    #
    return array([mu + gamma - alpha * (1 - theta) * s * i - (mu + gamma + omega) * s - gamma * i - gamma * sick,
                  alpha * (1 - theta) * s * i - (beta1 + beta2 + mu) * i,
                  beta2 * i - (beta3 + mu) * sick])

def rhs_vac(t, x, *p):
    from parameters import theta_min, theta_max
    # O lado direito da função    
    # ds/dt = mu + gamma - alpha(1-theta)*s*i - (mu + gamma + omega)*s - gamma*i - gamma*sick
    # di/dt = alpha*(1-theta)*s*i - (beta1 + beta2 + mu)*i
    # dsick/dt = beta2*i - (beta3 + mu)* sick
    #
    # this is the right-hand side funtion, implemented for numertical integration

    from numpy import array
    # verificando número de argumentos
    if len(p) != 8:
        raise Exception("Erro no número de parâmetros!")
    s = x[0]
    i = x[1]
    sick = x[2]
    #
    mu = p[0]
    gamma = p[1]
    alpha = p[2]
    theta = p[3]
    beta1 = p[4]
    beta2 = p[5]
    beta3 = p[6]
    omega = p[7]
    # limitar theta
    """
    def theta_lim(t):
        if theta(t) <= theta_min:
            return theta_min
        elif theta(t) >= theta_max:
            return theta_max
        else:
            return theta(t)
    print('theta(t)=',theta_lim(t))
    """
    theta_c = 0.0 
    def theta_lim(t):
        return theta_c
    #
    return array([mu + gamma - alpha * (1 - theta_lim(t)) * s * i - (mu + gamma + omega) * s - gamma * i - gamma * sick,
                  alpha * (1 - theta_lim(t)) * s * i - (beta1 + beta2 + mu) * i,
                  beta2 * i - (beta3 + mu) * sick])


def rhs(t, x, *p):
    from parameters import theta_min, theta_max
    # O lado direito da função    
    # ds/dt = mu + gamma - alpha(1-theta)*s*i - (mu + gamma)*s - gamma*i - gamma*sick
    # di/dt = alpha*(1-theta)*s*i - (beta1 + beta2 + mu)*i
    # dsick/dt = beta2*i - (beta3 + mu)* sick
    #
    # this is the right-hand side funtion, implemented for numertical integration

    from numpy import array
    # verificando número de argumentos
    if len(p) != 7:
        raise Exception("Erro no número de parâmetros!")
    s = x[0]
    i = x[1]
    sick = x[2]
    #
    mu = p[0]
    gamma = p[1]
    alpha = p[2]
    theta = p[3]
    beta1 = p[4]
    beta2 = p[5]
    beta3 = p[6]

    # Não é necessário limitar theta 
    # limitar theta
    #def theta_lim(t):
    #    if theta(t) <= theta_min:
    #        return theta_min
    #    elif theta(t) >= theta_max:
    #        return theta_max
    #    else:
    #        return theta(t)

    #
    return array([mu + gamma - alpha * (1 - theta(t)) * s * i - (mu + gamma) * s - gamma * i - gamma * sick,
                  alpha * (1 - theta(t)) * s * i - (beta1 + beta2 + mu) * i,
                  beta2 * i - (beta3 + mu) * sick])


def f(x, gamma, alpha, beta1, beta2, beta3, i0, s0, sick0, theta, mu, N):
    # A função de chamada do optimizador
    from numpy import array
    # in this version I adjust the initial condition so s0 + i0 + r0 = 1
    x0 = array([s0, i0, sick0])  # initial condition
    t0 = 0  # simulação comeza no dia 0
    tf = N - 1  # até N-1 dias
    h = 1  # o paso de integração é um dia
    t, sol = rk4(lambda t, x: rhs(t, x, mu, gamma, alpha, theta, beta1, beta2, beta3), x0, t0, tf, h)
    return sol[:, 2]

def theta_func(t):
    from numpy import pi, sin
    T = 7       # dias
    w = 2*pi/T  # freq. angular
    A = 0.05    # amplitude da oscilação
    Vm = 0.45   # Valor médio da oscilação
    return Vm+A*sin(w*t) 

def theta_func_1(t):
    from numpy import pi, sin
    T1 = 7       # dias
    w1 = 2*pi/T1  # freq. angular
    A1 = 0.05    # amplitude da oscilação
    Vm = 0.45   # Valor médio da oscilação
    T2 = 6*30       # dias
    w2 = 2*pi/T2  # freq. angular
    A2 = 0.075    # amplitude da oscilação
    #return Vm+0.08*sin(2*pi*t/(6*30))
    #return Vm+A*sin(w*t) + 0.08*sin(2*pi*t/(6*30))
    #return Vm+A*sin(w*t)
    return Vm+A1*sin(w1*t)+A2*sin(w2*t) 
