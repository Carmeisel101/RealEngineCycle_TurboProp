import pandas as pd
from winGasProp import GasProp
import numpy as np
from sympy import Eq, var, solve



def Iterate_temp_h(h, r, q):

    # i = 1
    GP = GasProp()
    GP.air()
    T_air1 = GP.T(h=h)
    GP.combustion(lamb=1)
    h_air1 = h
    h_stoich1 = GP.h(T=T_air1)
    f1 = h -r*h_stoich1 - q*h_air1

    GP.combustion(lamb=1)
    T_comb2 = GP.T(h=h)
    GP.air()
    h_air2 = GP.h(T=T_comb2)
    h_stoich2 = h
    f2 = h -r*h_stoich2 - q*h_air2

    # linear interpolation
    T = (T_air1*f2 - T_comb2*f1)/(f2-f1)
    return T


def Iterate_temp_ps(s, r, q):
    # i = 1
    GP = GasProp()
    GP.air()
    T_air1 = GP.T(p=1, s=s)
    GP.combustion(lamb=1)
    s_air1 = s
    s_stoich1 = GP.s(T=T_air1, p=1)
    f1 = s -r*s_stoich1 - q*s_air1
    # print('f1 = ', f1)
    GP.combustion(lamb=1)
    T_comb2 = GP.T(p=1, s=s) # HARDCODED VALUE FIX THIS LATER
    GP.air()
    s_air2 = GP.s(T=T_comb2, p=1)
    s_stoich2 = s
    f2 = s -r*s_stoich2 - q*s_air2
    # print('f2 = ', f2)

    # linear interpolation
    T = (T_air1*f2 - T_comb2*f1)/(f2-f1)
    s_air3 = GP.s(T=T, p=1)
    GP.combustion(lamb=1)
    s_stoich3 = GP.s(T=T, p=1)
    f3 = s -r*s_stoich3 - q*s_air3
    # print('f3 = ', f3)

    # numerically solve for T
    T = T - f3/(s_air3 - s_stoich3)

    return T

def stoich_tabs(s):
     s=s
     import pandas as pd
     table = pd.read_csv('stoich_tab.csv', index_col=0)

     # find the closest value to s
     # find the index of the closest value to s
     idx = (table['s']-s).abs().idxmin()
     # find the closest value to s
     s_closest = table['s'][idx]
     T_closest = table['T '][idx]
     T_up = table['T '][idx+1]
     s_up = table['s'][idx+1]
     T_down = table['T '][idx-1]
     s_down = table['s'][idx-1]
     T = T_down + (s - s_down) * (T_up - T_down) / (s_up - s_down)
     return T


def stoich_tabh(h):
    h=h
    import pandas as pd
    table = pd.read_csv('stoich_tab.csv', index_col=0)

    # find the closest value to h
    # find the index of the closest value to h
    idx = (table['h']-h).abs().idxmin()
    # find the closest value to h
    h_closest = table['h'][idx]
    T_closest = table['T '][idx]
    T_up = table['T '][idx+1]
    h_up = table['h'][idx+1]
    T_down = table['T '][idx-1]
    h_down = table['h'][idx-1]
    T = T_down + (h - h_down) * (T_up - T_down) / (h_up - h_down)
    return T


# def m_dot_air(p04):
#
#     )
#
#     return gamma
#
# gamma = m_dot_air(4.506)




# p = 1
# s = 7.8622
# # r = 0.35
# # q = 0.65
# h = 765.675
# T = stoich_tabs(s)
# T_h = stoich_tabh(h)
# # T = Iterate_temp_ps(s, r, q)
# print(T)
# print(T_h)


