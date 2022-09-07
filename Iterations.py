import pandas as pd
from winGasProp import GasProp



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
    T_comb2 = 711.6 # HARDCODED VALUE FIX THIS LATER
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


# p = 1
# s = 7.8622
# r = 0.35
# q = 0.65
#
# T = Iterate_temp_ps(s, r, q)
# print(T)


