import numpy as np
from sympy import Eq, solve, var

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

    return w_c, N

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

    tolerance = 0.000000009
    eff_com_list = []
    pi_c_star_list = []
    eff_com_iter = eff_com - tolerance

    pi_c_star = ((((pi_c) ** ((gamma - 1) / gamma)) - 1) * (eff_com_iter/eff_com)*(N / N_n) ** x + 1) ** (gamma / (gamma - 1))

    return pi_c_star, eff_com_iter
def step3(eff_combust, minL, lamb, m_air, T_01, p_03, TIT, p_01, pi_c_star):
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
    mass_const = m_air * (np.sqrt(T_01) / p_01)

    T = var('T')
    pi_c = const*mass_const*(((T/T_01)**(1/2)))
    eq = Eq(pi_c, pi_c_star)
    sol = solve(eq, T)
    sol = float(sol[0])


    return sol


def step4(N_n, pi_d, eff_combust, gamma_g, ratio1, eff_turb, T_01, N, eff_com, gamma, pi_c):
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
    pi_c_star_crt = (1/(pi_d*eff_combust))*((((gamma_g+1)/2))/(1-(ratio1*(1/eff_turb))))**((gamma_g)/((gamma_g-1)))
    eta_cr = eff_com*(1.0093)
    N_cr = N_n * ((eff_com / eta_cr) ** (1 / 2)) * (((pi_c_star_crt ** ((gamma - 1) / gamma)) - 1) /
                                              ((pi_c**((gamma-1)/gamma))-1))

    # N_lower = N*(1-0.15)
    # N_upper = N*(1+0.15)
    # N_list = np.linspace(N_lower, N_upper, 100)
    # eta_list = []
    # N_cr_list = []
    #
    # for i in N_list:
    #     eta_cr = var('eta_cr')
    #     N_cr = N_n*((eff_com/eta_cr)**(1/2))*(((pi_c_star_crt**((gamma-1)/gamma))-1)/
    #                                           ((pi_c**((gamma-1)/gamma))-1))
    #     eq = Eq(N_cr, i)
    #     sol = solve(eq, eta_cr)
    #     sol = float(sol[0])
    #     eta_list.append(sol)
    #     N_cr_list.append(i)
    return pi_c_star_crt, eta_cr, N_cr


def step5(AreaRatio):
    '''

    :param AreaRatio: Area ratio
    :return AreaRatio: Area ratio
    '''


    return AreaRatio

