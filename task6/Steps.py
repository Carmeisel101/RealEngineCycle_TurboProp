import numpy as np
from sympy import Eq, solve, var

def step1(N_n, w_c_n):
    '''

    :param N_n: Nominal angular speed
    :param w_c_n: Nominal compressor work
    :return w_c: compressor work
    :return N: angular speed
    '''

    N_r = N_n /1.05
    N = N_r * 1.1
    w_c = w_c_n * (N / N_n)**2

    return w_c, N

def step2(N, gamma, N_n, pi_c, eff_com):
    '''

    :param N: Angular speed
    :param gamma: ratio of specific heats
    :param N_n: Nominal angular speed
    :param pi_c: pressure ratio
    :param eff_com: combustion efficiency
    :return pi_c_star1: pressure ratio
    :return eff_com_list: list of compressor efficiencies
    :return pi_c_star_list: list of pressure ratios
    '''

    tolerance = 0.01
    eff_com_list = []
    pi_c_star_list = []

    pi_c_star = (((pi_c) ** ((gamma - 1) / gamma) - 1) * (eff_com/eff_com)*(N / N_n) ** 2 + 1) ** (gamma / (gamma - 1))
    eff_com_list.append(eff_com)
    pi_c_star_list.append(pi_c_star)

    pi_c_star1 = (((pi_c) ** ((gamma - 1) / gamma) - 1) * ((eff_com-0.001) / eff_com) * (N / N_n) ** 2 + 1) ** (
                gamma / (gamma - 1))
    eff_com_list.append(eff_com-0.001)
    pi_c_star_list.append(pi_c_star1)

    while abs(pi_c_star - pi_c_star1) > tolerance:

        eff_com = eff_com - 0.001
        pi_c_star1 = (((pi_c) ** ((gamma - 1) / gamma) - 1) * ((eff_com) / eff_com) * (N / N_n) ** 2 + 1) ** (
                    gamma / (gamma - 1))
        eff_com_list.append(eff_com)
        pi_c_star_list.append(pi_c_star1)

    return pi_c_star1, eff_com_list, pi_c_star_list

def step3(eff_com, minL, lamb, m_air, T_01, p_03, TIT, p_01, pi_c_star):
    '''

    :param eff_com: combustion efficiency
    :param minL: minL
    :param lamb: excess air
    :param m_air: mass of air
    :param T_01: T_01
    :param p_03: p_03
    :param TIT: Turbine inlet temperature
    :param p_01: p_01
    :param pi_c_star: pressure ratio
    :return sol : T_03
    '''

    const = ((1+(1/(lamb*minL)))/eff_com)*((p_03)/(((m_air)*(1+(1/(lamb*minL))))*np.sqrt(TIT)))
    mass_const = m_air * (np.sqrt(T_01) / p_01)

    T = var('T')
    pi_c = const*mass_const*(((T/T_01)**(1/2)))
    eq = Eq(pi_c, pi_c_star)
    sol = solve(eq, T)
    sol = float(sol[0])

    return sol


