import numpy as np
from sympy import Eq, solve, var
from macGasProp import GasProp
from Iterations import *

def step1(N_n, w_c_n, x):
    '''

    :param N_n: Nominal angular speed
    :param w_c_n: Nominal compressor work
    :return w_c: compressor work
    :return N: angular speed
    '''

    N_r = N_n /1.05
    N = N_r * 1.1
    w_c = w_c_n * (N / N_n)**x

    return w_c, N, N_r

def step2(N, gamma, N_n, pi_c, eff_com, x):
    '''

    :param N: Angular speed
    :param gamma: ratio of specific heats
    :param N_n: Nominal angular speed
    :param pi_c: pressure ratio
    :param eff_com: combustion efficiency
    :return pi_c_star1: pressure ratio
    :return eff_com_iter: compressor efficiency after iteration
    '''

    # tolerance = 0.00009
    eff_com_iter = 0.878213

    pi_c_star = ((((pi_c) ** ((gamma - 1) / gamma)) - 1) * (eff_com_iter/eff_com)*(N / N_n) ** x + 1) ** (gamma / (gamma - 1))

    return pi_c_star, eff_com_iter
def step3(eff_combust, minL, lamb, m_air, T_01, p_03, TIT, p_01, pi_c_star, m_ref):
    '''

    :param eff_combust: combustion efficiency
    :param minL: minL
    :param lamb: excess air
    :param m_air: mass flow rate of air
    :param T_01: T_01
    :param p_03: p_03
    :param TIT: Turbine inlet temperature
    :param p_01: p_01
    :param pi_c_star: pressure ratio
    :return sol : T_03
    '''

    const = ((1+(1/(lamb*minL)))/eff_combust)*((p_03)/(((m_air)*(1+(1/(lamb*minL))))*np.sqrt(TIT)))
    mass_const = m_ref * (np.sqrt(T_01) / p_01) *  1.03 #1.08
    # mass_const = 0.00041
    T = var('T')
    pi_c = const*mass_const*(((T/T_01)**(1/2)))
    eq = Eq(pi_c, pi_c_star)
    sol = solve(eq, T)
    sol = float(sol[0])


    return sol


def step4(N_n, pi_d, eff_combust, gamma_g, ratio2, eff_turb, T_01, N, eff_com, gamma, pi_c, N_r):
    '''

    :param N_n: Nominal angular speed
    :param pi_d: efficiency of diffuser
    :param eff_combust: efficiency of combustion
    :param gamma_g: ratio of specific heats of the mixture
    :param ratio1: ratio of work to enthalpy
    :param eff_turb: efficiency of turbine
    :param T_01: T_01
    :param N: angular speed
    :param eff_com: efficiency of compressor
    :param gamma: ratio of specific heats
    :param pi_c: pressure ratio
    :return critical pressure ratio
    :return eta_cr  critical efficiency
    :return N_cr critical angular speed
    '''
    pi_c_star_crt = (1/(pi_d*eff_combust))*((((gamma_g+1)/2))/(1-(ratio2*(1/eff_turb))))**((gamma_g)/((gamma_g-1)))
    N_lower = N_r *0.9 #different n
    print('N_lower:', N_lower)
    eta_cr = 0.879
    N_cr = N_n * (((eff_com / eta_cr) ) * (((pi_c_star_crt ** ((gamma - 1) / gamma)) - 1) /
                                              ((pi_c**((gamma-1)/gamma))-1)))** (1 / 2)


    return pi_c_star_crt, eta_cr, N_cr, N_lower


def step5(AreaRatio, eff_combust, pi_d, pi_c_star_crt, eff_turb, ratio2, gamma_g, weight):
    '''

    :param AreaRatio: Area ratio
    :return pH_p03: pressure ratio
    :return K: operating line constant
    :return ratio3: ratio of work to enthalpy
    '''
    pi_c_star = pi_c_star_crt*weight
    print('pi_c_star step 5:', pi_c_star)
    pH_p03 = 1/(eff_combust*pi_d*pi_c_star)
    K = ((1/AreaRatio)**2)*((pH_p03)**(2/gamma_g))*(1-((pH_p03)**((gamma_g-1)/gamma_g))-ratio2*(1/eff_turb))
    ratio3 = eff_turb*(1- ((pH_p03)**((gamma_g-1)/gamma_g)) - K*(AreaRatio**2)*(1/(pH_p03)**(2/gamma_g)))

    return pH_p03, K, ratio3, pi_c_star


def step6(w_c, x, N_n, N_lower):
    '''

    :param w_c: compressor work
    :param x: constant
    :param N_n: nominal angular speed
    :param N_cr: critical angular speed
    :return w_c_p6: compressor work for part 6
    :return N_p6: angular speed for part 6
    '''
    # N_p6 = N_lower
    N_p6 = 44500
    w_c_p6 = w_c * (N_p6/N_n) ** x

    return w_c_p6, N_p6

def step7(w_c_p6, ratio3):
    '''
    :param w_c_p6: compressor work for part 6
    :param ratio3: ratio of work to enthalpy
    :return h_03_p7: enthalpy at 03 for part 7
    '''

    h_03_p7 = w_c_p6/ratio3

    return h_03_p7


def step8(h_03_p7, r, q):
    '''
    :param h_03_p7: enthalpy at 03 for part 7
    :param r: weighting function r
    :param q: weighting function q
    :return T: temperature at 03 for part 8
    '''
    T = Iterate_temp_h(h_03_p7, r, q)
    return T


def step10(eff_combust, minL, lamb, m_air, T_01, p_03, TIT, p_01, pi_c_star, m_ref):
    '''

    :param eff_combust: combustion efficiency
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

    const = ((1+(1/(lamb*minL)))/eff_combust)*((p_03)/(((m_air)*(1+(1/(lamb*minL))))*np.sqrt(TIT)))
    mass_const = m_ref * (np.sqrt(T_01) / p_01) * 0.63
    # mass_const =
    T = var('T')
    pi_c = const*mass_const*(((T/T_01)**(1/2)))
    eq = Eq(pi_c, pi_c_star)
    sol = solve(eq, T)
    sol = float(sol[0])


    return sol
