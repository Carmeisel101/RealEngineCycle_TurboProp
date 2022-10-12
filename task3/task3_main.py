import pandas as pd
import numpy as np
from Steps import *
import warnings
warnings.filterwarnings("ignore")


dir = '../task2/comp_stages.csv'
task2_df = pd.read_csv(dir)
# print(task2_df)
w = [28000.0, 34000.0, 43955.1250000000, 36000.0]

''' Task 3 is a multiply step process consisting of 24 parts'''

# Part 1: Calculate delta_w_u_m
D1_m = task2_df['D1_m'][0]
n = task2_df['n'][0]
w_s_m = w[0]
cu_1_m = task2_df['cu'][0]
U_m, delta_w_u_m = step1(D1_m, n, w_s_m)
print('U_m = ', U_m)
# print('Part 1: delta_w_u_m = ', delta_w_u_m)

# Part 2: Calculate Beta_1_m, Beta_2_m
w1u_m = task2_df['w1u'][0]
c1a_m = task2_df['c1a'][0]
Beta_1_m, Beta_2_m, w_u2 = step2(w1u_m, c1a_m, delta_w_u_m)
print('Part 2: Beta_1_m = ', Beta_1_m, 'Beta_2_m = ', Beta_2_m)


# Part 3: Calculate t_m
tbar_m, Beta_til_1_m, Beta_til_2_m = step3(Beta_1_m, Beta_2_m)
solidity = 1/tbar_m
deviation_ang = (Beta_1_m - Beta_2_m)/(4*np.sqrt(solidity))
print('deviation_ang', deviation_ang)

# Part 5: Calculate b = b(r)
D1_t = task2_df['D1_t'][0]
D1_h = task2_df['D1_h'][0]
a_bar = 0.4
ratio, b_h, t_bar_h, t_h, z = step5(D1_t, D1_h, tbar_m, D1_m, Beta_til_1_m, Beta_til_2_m, a_bar)
# print('z', z)
print('Beta_1_m', Beta_1_m)
# Part 6: Assume a value of incidence
incidence = 1.5 # deg

# Part 7: Calculate the Delta_n
Beta_til_1_f = Beta_til_1_m + incidence
print('Beta_til_1_m', Beta_til_1_m)
print('Beta_til_1_f', Beta_til_1_f)
Beta_til_2_f = Beta_til_2_m + solidity # Part 8: Calculate Beta_til_2_f
theta_r, Delta_n = step7(Beta_til_1_f, Beta_til_2_f, a_bar, tbar_m)


# Part 9: Calculate the delta_beta
Beta_til_2_n = Beta_til_2_f - Delta_n
delta_beta1_til, Beta_til_1_n = step9(deviation_ang, incidence, theta_r, Beta_til_1_m, Beta_til_2_m, Beta_til_2_n)
print('Metal Turning angle of the blade =', Beta_til_1_n)

# Part 10: Calculate the theta_s
theta_s, delta_alpha_til = step10(theta_r, Beta_til_2_n, delta_beta1_til, incidence, deviation_ang)
print('Metal Turning angle of the vane =', delta_alpha_til)

alpha_til_1_m = 90-delta_alpha_til
r_blade = np.linspace(0, 1, 5)
r_vane = np.linspace(0, 1, 3)
c_U1, U_1, W_U_1, alpha_til, Beta_til, c1a, alpha= step13(alpha_til_1_m, cu_1_m, w_s_m, r_vane, r_blade, Beta_til_1_m, delta_w_u_m)
Beta_til_f_r, Beta = step14(incidence, Beta_til, r_blade)
# print('Beta_til', Beta_til)
# print('Beta', Beta)
# print('Beta_til_f_r', Beta_til_f_r)
print('c_U1', c_U1)
print('alpha_til', alpha_til)
print('alpha', alpha)
print('ca', c1a)









