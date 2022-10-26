import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from steps import *



if __name__ == '__main__':

    table_2_1 = pd.read_csv('Table2.1.csv')
    table_2_2 = pd.read_csv('Table2.3.csv')


    pi_star_n = 9.2
    eta_n = 0.89 # true for real cycles
    n_tostart = 1.05
    eta_tostart = 0.98
    ca_cabase_start = 0.8
    eta_ref  = eta_n/ eta_tostart
    gamma = 1.4

    pi_star_ratios, pi_star =  part1(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma)
    # print('pi_star_ratios = \n', pi_star_ratios) ####### deliveable
    # print('pi_star = \n', pi_star) ####### deliveable
    m_mbase = part2(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios)
    # print('m_mbase = \n', m_mbase)
    pi_bar, m_dot_bar = part3(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios, m_mbase)
    # print('pi_bar = \n', pi_bar)
    # print('m_dot_bar = \n', m_dot_bar)

    eta = part4(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios, m_mbase, pi_bar, m_dot_bar, eta_ref)
    # print('eta = \n', eta)

    ca_cabase_2 = 0.9
    pi_star_ratios2, pi_star2 =  part1(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_2, gamma)
    m_mbase2 = part2(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_2, gamma, pi_star_ratios2)
    pi_bar2, m_dot_bar2 = part3(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_2, gamma, pi_star_ratios2, m_mbase2)
    eta2 = part4(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_2, gamma, pi_star_ratios2, m_mbase2, pi_bar2, m_dot_bar2, eta_ref)
    # print('eta2 = \n', eta2)

    ca_cabase_3 = 1.0
    pi_star_ratios3, pi_star3 =  part1(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_3, gamma)
    m_mbase3 = part2(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_3, gamma, pi_star_ratios3)
    pi_bar3, m_dot_bar3 = part3(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_3, gamma, pi_star_ratios3, m_mbase3)
    eta3 = part4(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_3, gamma, pi_star_ratios3, m_mbase3, pi_bar3, m_dot_bar3, eta_ref)
    # print('eta3 = \n', eta3)

    ca_cabase_4 = 1.1
    pi_star_ratios4, pi_star4 =  part1(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_4, gamma)
    m_mbase4 = part2(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_4, gamma, pi_star_ratios4)
    pi_bar4, m_dot_bar4 = part3(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_4, gamma, pi_star_ratios4, m_mbase4)
    eta4 = part4(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_4, gamma, pi_star_ratios4, m_mbase4, pi_bar4, m_dot_bar4, eta_ref)
    # print('eta4 = \n', eta4)

    ca_cabase_5 = 1.2
    pi_star_ratios5, pi_star5 =  part1(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_5, gamma)
    m_mbase5 = part2(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_5, gamma, pi_star_ratios5)
    pi_bar5, m_dot_bar5 = part3(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_5, gamma, pi_star_ratios5, m_mbase5)
    eta5 = part4(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_5, gamma, pi_star_ratios5, m_mbase5, pi_bar5, m_dot_bar5, eta_ref)

    # print('eta5 = \n', eta5)

    Table_2_4_1 = pd.DataFrame({'0.8': pi_star, '0.9': pi_star2, '1.0': pi_star3, '1.1': pi_star4, '1.2': pi_star5})
    Table_2_4_2 = pd.DataFrame({'0.8': pi_star_ratios, '0.9': pi_star_ratios2, '1.0': pi_star_ratios3, '1.1': pi_star_ratios4, '1.2': pi_star_ratios5})
    print('Table_2_4_1 = \n', Table_2_4_1)
    Table_2_4_1.to_csv('Table_2_4_1.csv')
    print('Table_2_4_2 = \n', Table_2_4_2)
    Table_2_4_2.to_csv('Table_2_4_2.csv')
    Table_2_5 = pd.DataFrame({'0.8': m_mbase, '0.9': m_mbase2, '1.0': m_mbase3, '1.1': m_mbase4, '1.2': m_mbase5})
    print('Table_2_5 = \n', Table_2_5)
    Table_2_5.to_csv('Table_2_5.csv')





