import pandas as pd
import numpy as np



def part1(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma):

    n_column = table_2_1['n']
    # find the index where the value of n_tostart is closest to the value of n_tostart
    n_tostart_index = np.argmin(np.abs(n_column - n_tostart))
    # get the value of n_tostart that is closest to the value of n_tostart that we want to use
    pi_base = table_2_1['pi_base'][n_tostart_index]
    pi_star_ref = pi_star_n / pi_base

    ca_cabase = table_2_2['ca/ca_base']
    ca_cabase_index = np.argmin(np.abs(ca_cabase - ca_cabase_start))
    n_nbase = table_2_2['eta/eta_base'][ca_cabase_index]
    w_wbase = table_2_2['w/w_base'][ca_cabase_index]

    pi_star_base = pi_star_ref * table_2_1['pi_base']
    # print('pi_star_base = \n', pi_star_base)
    pi_star = (1+((((pi_star_base)**((gamma-1)/gamma))-1)*(n_nbase*w_wbase)))**(gamma/(gamma-1))

    # print('pi_star = \n', pi_star) ####### deliveable
    pi_star_ratios = pi_star / pi_star_base
    # print('pi_star_ratios = \n', pi_star_ratios) ####### deliveable

    return pi_star_ratios, pi_star

def part2(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios):

    m_mbase = ca_cabase_start*(pi_star_ratios**(1/3))

    return m_mbase

def part3(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios, m_mbase):


    pi_bar = pi_star_ratios * table_2_1['pi_base']
    m_dot_bar = m_mbase * table_2_1['m_base']

    return pi_bar, m_dot_bar

def part4(table_2_1, table_2_2, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios, m_mbase, pi_bar, m_dot_bar, eta_ref):
    eta_base_barless = table_2_1['eta_base'] * eta_ref
    ca_cabase = table_2_2['ca/ca_base']
    ca_cabase_index = np.argmin(np.abs(ca_cabase - ca_cabase_start))
    eta_etabase = table_2_2['eta/eta_base'][ca_cabase_index]

    eta = eta_etabase * eta_base_barless

    return eta

def part5(table_2_1, m_mbase):
    m_dot = table_2_1['m_base'] * m_mbase

    return m_dot