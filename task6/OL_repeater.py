import numpy as np
from sympy import Eq, solve, var
from Iterations import *
from Steps import *
import pandas as pd

# def step1_3loop(w_c_n, x, N_cr, gamma, pi_c, eff_com):
#     '''
#     This function perfoms the steps 1-3 3 times for values larger than N_cr
#     '''
#
#     N_list = [N_cr*1.05, N_cr*1.1, N_cr*1.15]
#     N_list = np.array(N_list)
#     df = pd.DataFrame(N_list, columns=['N_n'])
#     df['N_r'] = df['N_n']/1.05
#     df['N'] = df['N_r']*1.1
#     df['w_c'] = w_c_n * (df['N'] / df['N_n'])**x
#     df['eff_iter'] = [0.881, 0.9, 0.9]
#     df['pi_c_star'] = ((((pi_c) ** ((gamma - 1) / gamma)) - 1) * (df['eff_iter']/eff_com)*(df['N'] / df['N_n']) ** x + 1) ** (gamma / (gamma - 1))
#
#     return df