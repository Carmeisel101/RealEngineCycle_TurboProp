import numpy as np

def step1(D1_m, n, w_s_m):
    '''' Calculate delta_w_u_m '''
    U_m = (D1_m/2)*(2*np.pi)*(n/60) # m/s
    delta_w_u_m = w_s_m / U_m # m/s
    return U_m, delta_w_u_m

def step2(w1u_m, c1a_m, delta_w_u_m):
    '''' Calculate Beta_1_m, Beta_2_m '''
    w_u2 = -delta_w_u_m + w1u_m # the negative in front of delta_w_u_m is for convience
    # arctan in degrees
    Beta_1_m = np.arctan(w1u_m / c1a_m) * 180 / np.pi # deg
    Beta_2_m = np.arctan(w_u2 / c1a_m) * 180 / np.pi # deg

    return Beta_1_m, Beta_2_m, w_u2

def step3(Beta_1_m, Beta_2_m):
    '''' Calculate t_m '''
    Beta_til_1_m = 90 -Beta_1_m  # deg
    Beta_til_2_m = 90 - Beta_2_m # deg

    tbar_m = 3 - (1.15*(Beta_til_2_m - Beta_til_1_m)/((0.2*Beta_til_2_m)-2)) # deg
    return tbar_m, Beta_til_1_m, Beta_til_2_m

def cot(x):
    return 1/np.tan(x)

def step5(D1_t, D1_h, tbar_m, D1_m, Beta_til_1_m, Beta_til_2_m, a_bar):
    ratio = (1/2)*(D1_t-D1_h)
    b_h = ratio/3
    t_bar_h = tbar_m*(D1_h/D1_m)*0.75
    t_h = t_bar_h*b_h
    turn_ang = Beta_til_2_m - Beta_til_1_m
    chi_1 = (turn_ang/2)*(1+2*(1-2*a_bar))
    chi_2 = (turn_ang/2)*(1-2*(1-2*a_bar))

    # make a linspace of r between 0 to 1 qith 10 points
    r = np.linspace(0, 1, 11)
    z = []
    # for each r, calculate z
    for x in range(len(r)):
        z.append((r[x]*(1-r[x]))/((r[x]*(cot(chi_2*(np.pi/180)))+(1-r[x])*cot(chi_1*(np.pi/180)))))
    return ratio, b_h, t_bar_h, t_h, z

def step7(Beta_til_1_f, Beta_til_2_f, a_bar, tbar_m):
    '''' Calculate the Delta_n '''
    theta_r = (Beta_til_2_f - Beta_til_1_f)
    Delta_n = (0.92*(a_bar**2)-0.002*Beta_til_2_f+0.18)/((1/(theta_r*np.sqrt(tbar_m)))-0.002)
    return theta_r, Delta_n

def step9(deviation_ang, incidence, theta_r, Beta_til_1_m, Beta_til_2_m, Beta_til_2_n):
    '''' Calculate the delta_beta1 '''
    delta_beta1 = theta_r + incidence - deviation_ang
    Beta_til_1_n = Beta_til_2_n - delta_beta1
    return delta_beta1, Beta_til_1_n

def step10(theta_r, Beta_til_2_n):
    '''' Calculate the theta_s '''
    theta_s = Beta_til_2_n - 0.4*theta_r
    return theta_s