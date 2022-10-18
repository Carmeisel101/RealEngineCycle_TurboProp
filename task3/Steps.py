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
    Beta_til_1_m = 90 - Beta_1_m  # deg
    Beta_til_2_m = 90 - Beta_2_m # deg

    tbar_m = 3 - (1.15*(Beta_til_2_m - Beta_til_1_m)/((0.2*Beta_til_2_m)-2)) # deg
    return tbar_m, Beta_til_1_m, Beta_til_2_m

def cot(x):
    return 1/np.tan(x)

def step5(D1_t, D1_h, tbar_m, D1_m, Beta_til_1_m, Beta_til_2_m, a_bar, r):
    ratio = (1/2)*(D1_t-D1_h)
    b_h = ratio/3
    t_bar_h = tbar_m*(D1_h/D1_m)*0.75
    t_h = t_bar_h*b_h
    turn_ang = Beta_til_2_m - Beta_til_1_m
    chi_1 = (turn_ang/2)*(1+2*(1-2*a_bar))
    chi_2 = (turn_ang/2)*(1-2*(1-2*a_bar))

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
    delta_beta1_til = theta_r + incidence - deviation_ang
    Beta_til_1_n = Beta_til_2_n - delta_beta1_til
    return delta_beta1_til, Beta_til_1_n

def step10(theta_r, Beta_til_2_n, delta_beta1_til, incidence, deviation_ang):
    '''' Calculate the theta_s '''
    theta_s = Beta_til_2_n - 0.4*theta_r
    delta_alpha_til = theta_s - incidence + deviation_ang
    return theta_s, delta_alpha_til

def step13(alpha_til_1_m, cu_1_m, w_s_m, r_vane, r_m, Beta_til_1_m, delta_w_u_m, r):
    c_U1 = []
    U_1 = []
    W_U_1 = []
    alpha_til = []
    alpha = []
    Beta_til = []
    Beta = []
    c1a = []

    for x in range(len(r)):
        c_U1.append((r_m / r[x]) * cu_1_m)
        U_1.append((w_s_m * r[x]) / ((r_m) * (delta_w_u_m)))
        W_U_1.append(U_1[x] - c_U1[x])
        alpha_til.append(np.arctan((r[x] / r_m) * np.tan(alpha_til_1_m * np.pi / 180)) * 180 / np.pi)
        alpha.append(90 - alpha_til[x])
        Beta_til.append(np.arctan((r[x] / r_m) * np.tan(Beta_til_1_m * np.pi / 180)) * 180 / np.pi)
        c1a.append(c_U1[x] * np.tan(alpha_til[x] * np.pi / 180))
        Beta.append(np.arctan(W_U_1[x]/c1a[x])*180/np.pi)
    return c_U1, U_1, W_U_1, alpha_til, Beta_til, c1a, alpha, Beta

def step14(incidence, Beta_til, U_1, c1a, r, W_U_1):
    Beta_til_f_r = []
    for x in range(len(r)):
        Beta_til_f_r.append(incidence+Beta_til[x])
    return Beta_til_f_r

def step15(r, ca1, c_U1, h_01, m_air):
    c_r = []
    h_r = []
    rho_r = []
    p_r = []
    for x in range(len(r)):
        c_r.append(np.sqrt((ca1[x]**2)+(c_U1[x]**2)))
        h_r.append(h_01 - c_r[x]/2) # J/kg
        rho_r.append(m_air/(np.pi*r[x]**2*ca1[x])) # kg/m^3
        p_r.append(abs((c_U1[x]**2)*rho_r[x]*(np.log(r[x]))))
    return c_r, h_r, rho_r, p_r

def step16(r, delta_w_u_m , h_02, r_m, cu_1_m, w_s_m, c1a, m_air, incidence):
     cu_2_m = delta_w_u_m+cu_1_m
     c_u_2 = []
     U_2 = []
     W_U_2 = []
     Beta2 = []
     Beta_2_f_r = []
     Beta_til_2 = []
     alpha_2 = []
     h_r2 = []
     rho_r2 = []
     p_r2 = []
     c_r2 = []
     for x in range(len(r)):
         c_u_2.append((r_m/r[x])*cu_2_m)
         U_2.append((w_s_m*r[x])/(r_m*delta_w_u_m))
         W_U_2.append(U_2[x]-c_u_2[x])
         alpha_2.append((np.arctan(c_u_2[x]/c1a[x]))*180/np.pi)
         Beta2.append((np.arctan(W_U_2[x]/c1a[x]))*180/np.pi)
         Beta_til_2.append(90-Beta2[x])
         Beta_2_f_r.append(incidence+Beta_til_2[x])
         c_r2.append(np.sqrt((c1a[x]**2)+(c_u_2[x]**2)))
         h_r2.append(h_02+c_r2[x]/2)
         rho_r2.append(m_air/(np.pi*r[x]**2*c1a[x]))
         p_r2.append(abs((c_u_2[x]**2)*rho_r2[x]*(np.log(r[x]))))
     return  c_u_2, U_2, alpha_2, c_r2, h_r2, rho_r2, p_r2, W_U_2, Beta2, Beta_til_2, Beta_2_f_r

def step17(r_m, r, r_prime1):
    degreeOfReact = 1- (1-r_prime1)*((r_m/r)**2)
    return degreeOfReact

def step18(r, tbar_m, r_hub):
    tbar_r = []
    for x in range(len(r)):
        tbar_r.append(tbar_m*(r[x]/r_hub)*(1/(1-(r[x]/2))))
    return tbar_r

def step19(r, a_bar, t_bar_r, Beta_2_f_r, Beta_til_f_r):
    Delta_n_r = []
    for x in range(len(r)):
        Delta_n_r.append(((0.92*(a_bar**2))-(0.002*Beta_2_f_r[x])+
                          (0.18))/((1/((Beta_2_f_r[x]-Beta_til_f_r[x])*np.sqrt(t_bar_r[x])))-0.002))
    return Delta_n_r

def step20(r, Beta_til_f_r,  Beta_2_f_r, Delta_n_r):
    Theta_r = []
    Beta_2_n_r = []
    Theta_s_r = []
    for x in range(len(r)):
        Theta_r.append(Beta_2_f_r[x] - Beta_til_f_r[x])
        Beta_2_n_r.append(Beta_2_f_r[x] - Delta_n_r[x])
        Theta_s_r.append(Beta_2_n_r[x] - 0.4*Theta_r[x])
    return Theta_r, Beta_2_n_r, Theta_s_r

