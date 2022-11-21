import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Steps import *


if __name__ == '__main__':

    specs_df = pd.read_csv('../task1/BasicSpecs.csv')
    task1_r2_df = pd.read_csv('../task1/results2.csv')
    task1_r1_df = pd.read_csv('../task1/results.csv')
    task2_df = pd.read_csv('../task2/comp_stages.csv')


    TIT = specs_df['TIT [K]'][0]
    w_c_n = task1_r2_df['w_c'][0]
    pi_c = specs_df['Compressor Ratio'][0]
    eff_com = specs_df['eff_compressor'][0]
    N_n = task2_df['n'][0]
    m_air = task1_r2_df['m_air'][0]
    T_01 = 288.16 # K
    lamb = task1_r2_df['lambda'][0]
    gamma = 1.4
    minL = 14.66
    eff_combust = 1
    p_03 = task1_r1_df['Pressure [bar]'][5]
    p_01 = task1_r1_df['Pressure [bar]'][1]
    cp = 1.004 # kJ/kgK


    w_c, N = step1(N_n, w_c_n)
    print('w_c = ', w_c, 'kJ/kg')

    pi_c_star, eff_com_list, pi_c_star_list = step2(N, gamma, N_n, pi_c, eff_com)
    print('pi_c_star = ', pi_c_star)

    T_03 = step3(eff_com, minL, lamb, m_air, T_01, p_03, TIT, p_01, pi_c_star)
    print('T_03 = ', T_03)

    print('wc/h3 = ', w_c/(cp*T_03))




