# Parâmetros da simulação
DATA_MIN = '2020-02-25'         # Data da primeira coleta de dados
DATA_MAX = '2021-03-08'         # Data da última coleta de dados
data_fit_ini = '2020-04-30'     # Data de início para o recorte dos dados para o fitting
data_fit_end = '2020-05-30'     # Data final para o recorte dos dados para o fitting
data_val_ini = data_fit_ini     # Data de início para o recorte dos dados de validação
data_val_end = '2020-06-30'     # Data final para o recorte dos dados de validação
mu = 3.595e-05                  # Taxa diaria de nacimentos e mortes
# No fitting: valores mínimos e máximos que os parâmetros livres podem tomar
gamma_min = 0.0067
gamma_max = 0.02
alpha_min = 0.24
alpha_max = 1.00
beta1_min = 0.1
beta1_max = 0.2
beta2_min = 0.1
beta2_max = 0.3
beta3_min = 0.07
beta3_max = 0.2
#s0_min = 0
#s0_max = 0.9999
# limites para theta
theta_min = 0.35
theta_max = 0.59
