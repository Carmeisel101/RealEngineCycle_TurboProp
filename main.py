# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 07:47:20 2022

@author: Ozzy
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from winGasProp import GasProp
from stages import stage01
from stages import stage02i
from stages import stage02
from stages import stage03
from stages import stage04i

if __name__ == '__main__':
    # Stage 01
    specs = pd.read_csv('BasicSpecs.csv')
    T01 = 288.16  # K
    p01 = 101325  # Pa
    h01, s01 = stage01(T01, p01)
    # print('The enthalpy at stage 01 is: {:.2f} kJ/kg'.format(h01))
    # print('The entropy at stage 01 is: {:.5f} kJ/kg-K'.format(s01))

    # Stage 02i
    # pi_0c = specs['Compressor Ratio'].values[0]
    pi_0c_test = 12
    h02i, w_ci, p02i = stage02i(pi_0c_test, p01, s01, h01)
    # print('The enthalpy at stage 02i is: {:.2f} kJ/kg'.format(h02i))
    # print('The work at stage 02i is: {:.2f} kJ/kg'.format(w_ci))

    # Stage 02
    eff_c = specs['eff_compressor'].values[0]
    s02, w_c, h02 = stage02(p02i, w_ci, h01, eff_c)
    # print('The entropy at stage 02 is: {:.5f} kJ/kg-K'.format(s02))
    # print('The work at stage 02 is: {:.2f} kJ/kg'.format(w_c))
    # print('The enthalpy at stage 02 is: {:.2f} kJ/kg'.format(h02))

    # Stage 03
    T03, p03, h03, s03, excess_air, r, q = stage03(p02i, h02)
    print(T03, p03, h03, s03)
    
    #Stage 04i
    s04i, h04i, T04i, p04i = stage04i(s03, excess_air, w_c, h03, r, q)
    print(s04i, h04i, T04i, p04i)