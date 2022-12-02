import numpy as np
from sympy import Eq, solve, var
from Iterations import *
from Steps import *
import pandas as pd

def step1_3loop(w_c_n, x, N_cr, gamma, pi_c, eff_com, N_n, TIT, m_ref, eff_combust, lamb,
                p_03, m_air, p_01, T_01, ratio2, r, q, gamma_g):
    '''
    This function perfoms the steps 1-3 3 times for values larger than N_cr
    '''

    N_list = [N_cr*1.05, N_cr*1.1, N_cr*1.15]
    N_list = np.array(N_list)
    df = pd.DataFrame(N_list, columns=['N'])
    # df['N_r'] = df['N_n']/1.05
    # df['N'] = df['N_r']*1.1
    minL = 14.66
    df['w_c'] = w_c_n * (df['N'] / N_n )**x
    df['eff_iter'] = [0.881, 0.879, 0.9]
    df['pi_c_star'] = ((((pi_c) ** ((gamma - 1) / gamma)) - 1) * (df['eff_iter']/eff_com)*(df['N'] / N_n) ** x + 1) ** (gamma / (gamma - 1))
    df['m_bar'] = [.71, .785, .9]
    T1= var('T1')
    T2= var('T2')
    T3= var('T3')
    pi_c_star1 = (((1+(1/(lamb*minL)))/eff_combust)*((p_03)/(((m_air)*(1+(1/(lamb*minL))))*np.sqrt(TIT))))*(m_ref * (np.sqrt(T_01) / p_01) * df['m_bar'][0])*(((T1/T_01)**(1/2)))
    pi_c_star2 = (((1+(1/(lamb*minL)))/eff_combust)*((p_03)/(((m_air)*(1+(1/(lamb*minL))))*np.sqrt(TIT))))*(m_ref * (np.sqrt(T_01) / p_01) * df['m_bar'][1])*(((T2/T_01)**(1/2)))
    pi_c_star3 = (((1 + (1 / (lamb * minL))) / eff_combust) * (
                (p_03) / (((m_air) * (1 + (1 / (lamb * minL)))) * np.sqrt(TIT)))) * (
                             m_ref * (np.sqrt(T_01) / p_01) * df['m_bar'][2]) * (((T3 / T_01) ** (1 / 2)))

    eq1 = Eq(pi_c_star1, df['pi_c_star'][0])
    eq2 = Eq(pi_c_star2, df['pi_c_star'][1])
    eq3 = Eq(pi_c_star3, df['pi_c_star'][2])
    sol = solve((eq1, eq2, eq3), (T1, T2, T3))
    df['T_03'] = [sol[T1], sol[T2], sol[T3]]

    h_03_1 = r*stoich_tabT(float(df['T_03'][0])) + q*air_tabT(float(df['T_03'][0]))
    h_03_2 = r*stoich_tabT(float(df['T_03'][1])) + q*air_tabT(float(df['T_03'][1]))
    h_03_3 = r*stoich_tabT(float(df['T_03'][2])) + q*air_tabT(float(df['T_03'][2]))

    df['h_03'] = [h_03_1, h_03_2, h_03_3]
    df['ratio1'] = df['w_c']/df['h_03']
    df['% diff'] = abs(df['ratio1']-ratio2)/ratio2*100

    return df



def OL_repeater(pi_c_star_crt, pi_d, eff_combust, AreaRatio, gamma_g, eff_turb, ratio2, N_n, w_c_n, x, r,q, lamb, m_ref, m_air, TIT, p_01, T_01, p_03):


    pi_c = [1.1*pi_c_star_crt, 1.3*pi_c_star_crt, 1.5*pi_c_star_crt]
    minL = 14.66
    # pi_c = [0.95*pi_c_star_crt, pi_c_star_crt, pi_c_star_crt]
    pi_c = np.array(pi_c)
    df = pd.DataFrame(pi_c, columns=['pi_c'])
    df['pH_p03'] = 1 / (eff_combust * pi_d * df['pi_c'])
    df['K'] = ((1/AreaRatio)**2)*((df['pH_p03'])**(2/gamma_g))*(1-((df['pH_p03'])**((gamma_g-1)/gamma_g))-ratio2*(1/eff_turb))
    df['ratio3'] = eff_turb*(1- ((df['pH_p03'])**((gamma_g-1)/gamma_g)) - df['K']*(AreaRatio**2)*(1/(df['pH_p03'])**(2/gamma_g)))
    df['N'] = [44500, 40000, 50000]
    df['w_c'] = w_c_n* (df['N'] / N_n )**x

    df['h_03'] = df['w_c']/df['ratio3']
    T1a = Iterate_temp_h(df['h_03'][0], r, q)
    T2a = Iterate_temp_h(df['h_03'][1], r, q)
    T3a = Iterate_temp_h(df['h_03'][2], r, q)
    df['T_03_tables'] = [T1a, T2a, T3a]

    df['m_bar'] = [0.73, 0.96, 0.895]
    T1 = var('T1')
    T2 = var('T2')
    T3 = var('T3')
    pi_c_star1 = (((1 + (1 / (lamb * minL))) / eff_combust) * (
                (p_03) / (((m_air) * (1 + (1 / (lamb * minL)))) * np.sqrt(TIT)))) * (
                             m_ref * (np.sqrt(T_01) / p_01) * df['m_bar'][0]) * (((T1 / T_01) ** (1 / 2)))
    pi_c_star2 = (((1 + (1 / (lamb * minL))) / eff_combust) * (
                (p_03) / (((m_air) * (1 + (1 / (lamb * minL)))) * np.sqrt(TIT)))) * (
                             m_ref * (np.sqrt(T_01) / p_01) * df['m_bar'][1]) * (((T2 / T_01) ** (1 / 2)))
    pi_c_star3 = (((1 + (1 / (lamb * minL))) / eff_combust) * (
            (p_03) / (((m_air) * (1 + (1 / (lamb * minL)))) * np.sqrt(TIT)))) * (
                         m_ref * (np.sqrt(T_01) / p_01) * df['m_bar'][2]) * (((T3 / T_01) ** (1 / 2)))

    eq1 = Eq(pi_c_star1, df['pi_c'][0])
    eq2 = Eq(pi_c_star2, df['pi_c'][1])
    eq3 = Eq(pi_c_star3, df['pi_c'][2])
    sol = solve((eq1, eq2, eq3), (T1, T2, T3))
    df['T_03_solve'] = [sol[T1], sol[T2], sol[T3]]


    return df