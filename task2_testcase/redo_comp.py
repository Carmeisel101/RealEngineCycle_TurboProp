from math import *
import numpy as np
import pandas as pd
from sympy import Eq, var, solve
from Iter import iteration

w_total = 283.91025 / 2
gamma = 1.4
#assume half the pressure is done in the axial and half in the centrifugal
p_a_comp = 9.321900/2
















def stages(w_s, w_total):
    w_s1 = .7 * w_s
    w_s2 = .85 * w_s
    w_sn = .9 * w_s
    n = var('n')
    eq = Eq((w_total-w_s1-w_s2-w_sn) / (n-3),w_s)
    num_of_stages = floor(solve(eq)[0])
    w_stages = (w_total-w_s1-w_s2-w_sn) / (num_of_stages-3)

    return (w_s1,w_s2,w_stages,w_sn)

works = stages(40,w_total)
w = [works[0]*1000, works[1]*1000, works[2]*1000, works[3]*1000]
print(w)
nabla = [.98,.98,.98]


data = pd.read_excel("Data.xlsx")
#print(data)

u1_t = data.iat[0,1]
d1_bar = data.iat[1,1]
phi_m = data.iat[2,1]
phi_t = data.iat[3,1]
gamma = data.iat[4,1]
h01 = data.iat[5,1]
alpha_bar_m = radians(data.iat[6,1])
m_f_rate = data.iat[7,1]
T01 = data.iat[8,1]
p01 = data.iat[9,1]
R = data.iat[10,1]






u1_m = (u1_t * (1 + d1_bar)) / 2
c1a_m = u1_m * phi_m
c1a_t = u1_t * phi_t
lamda_1a_m = c1a_m / (sqrt(2 * ((gamma -1)/(gamma + 1)) * h01*1000))
lamda_1u_m = u1_m / (sqrt(2 * ((gamma -1)/(gamma + 1)) * h01*1000))
lamda_1_m = lamda_1a_m / sin(alpha_bar_m)

c1_m = lamda_1_m * sqrt(2 *((gamma - 1)/(gamma + 1)) * h01*1000 )
c1u_m = sqrt(c1_m **2 - c1a_m**2 )
w1_u =u1_m - c1u_m
w1 = sqrt(w1_u**2 + c1u_m**2)
q_lamda_1_m = lamda_1_m*((((gamma + 1) / 2) * (1 - (((gamma-1)/(gamma+1)) * lamda_1_m**2)))**(1/(gamma-1)))
A_1 = ((m_f_rate* sqrt(T01)) / (p01 *100000)) * (1 / (q_lamda_1_m * sin(alpha_bar_m) * sqrt((gamma/R) *(2/(gamma+1))**((gamma+1)/(gamma-1)))))


D1_t = sqrt((4 * A_1) / (pi * (1 - d1_bar**2)))
D1_h = d1_bar * D1_t
D1_m = (D1_h + D1_t) / 2
n = (60 * u1_m) / (pi * D1_m)

delta_cu_list = [1.957, 3.02336, 1.278, 3.247]
delta_ca_list = [1, 1.5, 2, 2.5]
#stage 1
ca1 = c1a_m
cu1 = c1u_m
U1 = (D1_m / 2) * (2 * pi) * (n/60)
print('THis is U1',U1)
Wu1 = U1 - cu1
stage_index = 0

theta = (1 - (.4/2.4) * lamda_1_m**2)
a = 1/(sqrt((2.4/2) * theta))
m_w1 = a**2 * (lamda_1_m**2 + lamda_1u_m**2 - 2 * lamda_1_m * lamda_1u_m * cos(radians(alpha_bar_m)))

print('THis is m_w1',sqrt(m_w1))


r_prime = iteration(cu1, Wu1, w, U1, ca1, delta_ca_list, stage_index, delta_cu_list)
T0 = [288.16, 316.16, 350.4, 393.5]
h = [288.3, 316.3, 350.3, 394.255]




def comp_stages(ca,delta_ca_list,cu, delta_cu_list,h, w,T0,nabla,p01, gamma,R,mfr, dt, n,i):
    ca_new = ca - delta_ca_list[i]


    cu_new = cu - delta_cu_list[i]
    C_new = sqrt(cu_new**2 + ca_new**2)

    alpha = atan(cu_new / ca_new)
    real_alpha = radians(90) - alpha
    enthalpy = h[i]
    eff_comp = (1 + nabla[i-1] * ((w[i-1] / 1000)/(h[i-1])))**(gamma/ (gamma-1))

    P_new = p01 * eff_comp
    acr = sqrt((2) * ((gamma - 1)/(gamma + 1)) * enthalpy * 1000)
    lamda = (C_new) / (acr)
    q_lamda = lamda * ((((gamma + 1) / 2) * (1 - (((gamma - 1) / (gamma + 1)) * lamda ** 2))) ** (1 / (gamma - 1)))
    A_1 = ((mfr * sqrt(T0[i])) / (P_new * 100000)) * (1 / (q_lamda * sin(real_alpha) * sqrt((gamma / R) * (2 / (gamma + 1)) ** ((gamma + 1) / (gamma - 1)))))
    dh = sqrt(dt**2 - ((4 * A_1) / pi))
    dm = .5 * (dh + dt)
    U_new = (dm /2) * (2*pi) * (n/60)
    Wu_new = U_new - cu_new

    r_prime = iteration(cu_new, Wu_new, w, U_new, ca_new, delta_ca_list, i, delta_cu_list)


    return ca_new, cu_new, P_new,real_alpha,r_prime, U_new

#stage 2
ca_2, cu_2, P_2, real_alpha, r_prime2, U_2  = comp_stages(ca1,delta_ca_list,cu1,delta_cu_list,h,w,T0,nabla,p01,gamma,287.16,m_f_rate,D1_t,n,1)

# stage 3
ca_3, cu_3, P_3, real_alpha3, r_prime3, U_3 = comp_stages(ca_2, delta_ca_list, cu_2, delta_cu_list, h, w, T0, nabla, P_2, gamma, 287.16, m_f_rate, D1_t, n, 2)

# stage 4
ca_4, cu_4, P_4, real_alpha4, r_prime4, U_4 = comp_stages(ca_3, delta_ca_list, cu_3, delta_cu_list, h, w, T0, nabla, P_3, gamma, 287.16, m_f_rate, D1_t, n, 3)


df = pd.DataFrame({'stage': [1,2,3,4], 'ca': [ca1, ca_2, ca_3, ca_4], 'cu': [cu1, cu_2, cu_3, cu_4],
                   'P': [p01, P_2, P_3, P_4], 'alpha': [alpha_bar_m, real_alpha, real_alpha3, real_alpha4],
                   'r_prime': [r_prime, r_prime2, r_prime3, r_prime4], 'U': [U1, U_2, U_3, U_4]})


# to csv


df_2 = pd.DataFrame({'u1m': [u1_m], 'c1a': [c1a_m], 'c1u': [c1u_m], 'w1': [w1], 'w1u': [w1_u], 'D1_m': [D1_m], 'n': [n], 'D1_t': [D1_t], 'D1_h': [D1_h] })
# concatinate w to df_2
df= pd.concat([df, df_2], axis=1)
df.to_csv('comp_stages.csv', index=False)
print(df)

print(w)
print(df.loc[0])
