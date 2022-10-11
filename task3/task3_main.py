import pandas as pd
import numpy as np
from Steps import *


dir = '../task2/comp_stages.csv'
task2_df = pd.read_csv(dir)
# print(task2_df)
w = [28000.0, 34000.0, 43955.1250000000, 36000.0]

''' Task 3 is a multiply step process consisting of 24 parts'''

# Part 1: Calculate delta_w_u_m
D1_m = task2_df['D1'][0]
n = task2_df['n'][0]
w_s_m = w[0]
U_m, delta_w_u_m = step1(D1_m, n, w_s_m)

# Part 2: Calculate Beta_1_m, Beta_2_m
w1u_m = task2_df['w1u'][0]
c1a_m = task2_df['c1a'][0]
Beta_1_m, Beta_2_m, w_u2 = step2(w1u_m, c1a_m, delta_w_u_m)


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
print('z', z)

# Part 6: Assume a value of incidence
incidence = 1.5 # deg

# Part 7: Calculate the Delta_n
Beta_til_1_f = Beta_til_1_m + incidence
Beta_til_2_f = Beta_til_2_m + solidity # Part 8: Calculate Beta_til_2_f
theta_r, Delta_n = step7(Beta_til_1_f, Beta_til_2_f, a_bar, tbar_m)


# Part 9: Calculate the delta_beta
Beta_til_2_n = Beta_til_2_f - Delta_n
delta_beta1, Beta_til_1_n = step9(deviation_ang, incidence, theta_r, Beta_til_1_m, Beta_til_2_m, Beta_til_2_n)

# Part 10: Calculate the theta_s
theta_s = step10(theta_r, Beta_til_2_n)
print('theta_s', theta_s)






