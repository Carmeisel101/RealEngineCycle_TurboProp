import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Steps import *


if __name__ == '__main__':

    specs_df = pd.read_csv('../task1/BasicSpecs.csv')
    task1_r2_df = pd.read_csv('../task1/results2.csv')
    task2_df = pd.read_csv('../task2/comp_stages.csv')


    TIT = specs_df['TIT [K]'][0]
    w_c_n = task1_r2_df['w_c'][0]
    pi_c = specs_df['Compressor Ratio'][0]
    eff_com = specs_df['eff_compressor'][0]
    N_n = task2_df['n'][0]
    T_01 = 288.16 # K
    gamma = 1.4


    w_c, N = step1(N_n, w_c_n)
    print('w_c = ', w_c, 'kJ/kg')

    pi_c_star, eff_com_list, pi_c_star_list = step2(N, gamma, N_n, pi_c, eff_com)




