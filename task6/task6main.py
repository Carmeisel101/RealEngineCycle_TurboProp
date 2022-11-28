import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Steps import *
from macGasProp import GasProp
from Iterations import *


if __name__ == '__main__':

    specs_df = pd.read_csv('../task1/BasicSpecs.csv')
    task1_r2_df = pd.read_csv('../task1/results2.csv')
    task1_r1_df = pd.read_csv('../task1/results.csv')
    task2_df = pd.read_csv('../task2/comp_stages.csv')


    TIT = specs_df['TIT [K]'][0]
    eff_turb = specs_df['eff_turbine'][0]
    w_c_n = task1_r2_df['w_c'][0]
    pi_c = specs_df['Compressor Ratio'][0]
    eff_com = specs_df['eff_compressor'][0]
    # eff_com = 0.79
    N_n = task2_df['n'][0]
    m_air = task1_r2_df['m_air'][0]
    T_01 = 288.16 # K
    lamb = task1_r2_df['lambda'][0]
    gamma = 1.4
    minL = 14.66
    eff_combust = 0.95
    m_ref = 1.6087156862745098
    p_03 = task1_r1_df['Pressure [bar]'][5]
    p_01 = task1_r1_df['Pressure [bar]'][1]
    h_03_n = task1_r1_df['Enthalpy [kJ/kg]'][5]
    # cp = 1.004516 # kJ/kgK
    x = 1.4
    pi_d = 0.95
    AreaRatio = 1.2 # A3.5/A5



    w_c, N = step1(N_n, w_c_n, x)
    print('w_c = ', w_c, 'kJ/kg')
    print('N = ', N, 'rpm')

    pi_c_star, eff_com_iter = step2(N, gamma, N_n, pi_c, eff_com, x)
    print('pi_c_star = ', pi_c_star)
    print('eff_com_iter = ', eff_com_iter)

    T_03 = step3(eff_combust, minL, lamb, m_air, T_01, p_03, TIT, p_01, pi_c_star, m_ref)
    print('T_03 = ', T_03)
    r = (1+minL)/(1+minL*lamb)
    q = ((lamb-1)*minL)/(1+minL*lamb)

    h_a = air_tabT(T_03)
    h_stoich = stoich_tabT(T_03)


    h_03 = r  * h_stoich + q * h_a
    print('h_03 = ', h_03)

    ratio1 = w_c/h_03
    ratio2 = w_c_n/(h_03_n)
    print('ratio1 = ', ratio1)
    print('ratio2 = ', ratio2)
#     percent difference in ratio 1 and 2
    print('percent difference in ratio 1 and 2 = ', abs(ratio1-ratio2)/ratio2*100, '%')

    gamma_g_a = 1.260844
    gamma_g_stoich = 1.314339

    gamma_g = r * gamma_g_stoich + q * gamma_g_a
    print('gamma_g = ', gamma_g)
    pi_c_star_crt, eta_cr, N_cr = step4(N_n, pi_d, eff_combust, gamma_g, ratio2, eff_turb, T_01,
                          N, eff_com, gamma, pi_c)
    print('pi_c_star_crt = ', pi_c_star_crt)
    print('eta_cr = ', eta_cr)
    print('N_cr = ', N_cr, 'rpm')

    # n_list = [N_cr*1.025, N_cr*1.05, N_cr*1.075]

    pH_p03, K, ratio3, pi_c_star_5= step5(AreaRatio, eff_combust, pi_d, pi_c_star_crt, eff_turb, ratio1, gamma_g)
    print('pH_p03 = ', pH_p03)
    print('K = ', K)
    print('ratio3 = ', ratio3)

    w_c_p6, N_p6 = step6(w_c_n, x, N_n, N_cr)
    print('w_c_p6 = ', w_c_p6, 'kJ/kg')
    print('N_p6 = ', N_p6, 'rpm')

    h_03_p7 = step7(w_c_p6, ratio3)
    print('h_03_p7 = ', h_03_p7, 'kJ/kg')

    T_03_p8 = step8(h_03_p7, r, q)
    print('T_03_p8 = ', T_03_p8, 'K')

    #### Step 9 read


    T_03_10 = step10(eff_combust, minL, lamb, m_air, T_01, p_03, TIT,p_01, pi_c_star_5, m_ref)
    print('T_03_10 = ', T_03_10, 'K')



