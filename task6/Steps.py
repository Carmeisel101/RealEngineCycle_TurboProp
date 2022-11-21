

def step1(N_n, w_c_n):

    N_r = N_n /1.05
    N = N_r * 1.1
    w_c = w_c_n * (N / N_n)**2

    return w_c, N

def step2(N, gamma, N_n, pi_c):

    pi_c_star = (((pi_c)**((gamma-1)/gamma) - 1) * (N / N_n)**2 + 1)**(gamma/(gamma-1))
    tolerance = 0.01
    print('pi_c_star = ', pi_c_star)


    return pi_c_star


