# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 07:47:30 2022

@author: Ozzy
"""
import pandas as pd
import numpy as np
from winGasProp import GasProp

def stage01(T01, p01):
    # This is a demo of the winGasProp module
    GP = GasProp()
    GP.air()
    h01 = GP.h(T=T01)
    s01_1bar = GP.s(T=T01, p=1) # s01 at 1 bar (p is in units of bar)
    s01 = s01_1bar - 0.28716* np.log(p01/1e5) # s01 at p01
    return h01, s01

def stage02i(pi_0c, p01, s01, h01):
    p01 = p01/1e5 # p01 in units of bar
    p02i = pi_0c * p01
    s02i = s01
    s2prime = s02i + 0.28716 * np.log(p02i)
    GP = GasProp()
    h02i = GP.h(s=s2prime, p=1)
    w_ci = h02i - h01
    return h02i, w_ci, p02i

def stage02(p02i, w_ci, h01, eff_c):
    GP = GasProp()
    GP.air()
    w_c = w_ci / eff_c
    p02 = p02i
    h02 = h01 + w_c
    s02_1bar = GP.s(h=h02, p=1)
    s02 = s02_1bar - 0.28716 * np.log(p02)
    return s02, w_c, h02

def stage03(p02, h02):
    pres_drop_comb = 0.03
    T03 = 1400
    minL = 14.66
    LHV = 43500
    comb_eff = 0.97
    p03 = p02 * (1 - pres_drop_comb)
    GP = GasProp()
    
    GP.air()
    h03_air = GP.h(T=T03)
    s03_air = GP.s(T=T03, p=1)
    
    GP.combustion(lamb=1)
    h03_lam1 = GP.h(T=T03)
    s03_lam1 = GP.s(T=T03, p=1)
    
    excess_air = (h03_lam1 * (1 + minL) - comb_eff * LHV - h03_air * minL) / (minL * (h02 - h03_air))
    r = (1 + minL) / (1 + excess_air * minL)
    q = ((excess_air - 1) * minL) / (1 + excess_air * minL)
    
    h03 = r * h03_lam1 + q * h03_air
    s03_lam = r * s03_lam1 + q * s03_air
    s03 = s03_lam - 0.28716 * np.log(11.791) #Dont know what 11.791 just copied from page 243
    return T03, p03, h03, s03, excess_air, r, q

def stage04i(s03, excess_air, w_c, h03, r, q):
    minL = 14.66
    turbine_eff = 0.92
    s04i = s03
    w_T = w_c * (1 / (1 + (1 / (excess_air * minL))))
    w_Ti = w_T / turbine_eff
    h04i = h03 - w_Ti
    
    #Iterative Process I dont understand
    T04i = 1093.4
    GP = GasProp()
    GP.air()
    s04i_air = GP.s(T=T04i)
    GP.combustion(lam=1)
    s04i_lam = GP.s(T=T04i)
    s04i_p1_lam = r * s04i_lam + q * s04i_air
    p04i = np.exp(-(s04i - s04i_p1_lam) / 0.28716)
    
    return s04i, h04i, T04i, p04i
    
    
    