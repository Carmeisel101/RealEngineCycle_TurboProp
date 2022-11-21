

def step1(N_n, w_c_n):

    N_r = N_n /1.05
    N = N_r * 1.1
    w_c = w_c_n * (N / N_n)**2

    return w_c, N

def step2(N, gamma, N_n, pi_c, eff_com):

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

def step3()

