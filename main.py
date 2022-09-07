import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from winGasProp import GasProp
from stages import stage01
from stages import stage02i
from stages import stage02
from stages import stage03

if __name__ == '__main__':
    # Stage 01
    specs = pd.read_csv('BasicSpecs.csv')
    T01 = 288.16  # K
    p01 = 101325  # Pa
    h01, s01 = stage01(T01, p01)
    print('The enthalpy at stage 01 is: {:.2f} kJ/kg'.format(h01))
    print('The entropy at stage 01 is: {:.5f} kJ/kg-K'.format(s01))

    # Stage 02i
    # pi_0c = specs['Compressor Ratio'].values[0]
    pi_0c_test = 12
    h02i, w_ci, p02i = stage02i(pi_0c_test, p01, s01, h01)
    print('The enthalpy at stage 02i is: {:.2f} kJ/kg'.format(h02i))
    print('The work at stage 02i is: {:.2f} kJ/kg'.format(w_ci))

    # Stage 02
    eff_c = specs['eff_compressor'].values[0]
    s02, w_c, h02 = stage02(p02i, w_ci, h01, eff_c)
    print('The entropy at stage 02 is: {:.5f} kJ/kg-K'.format(s02))
    print('The work at stage 02 is: {:.2f} kJ/kg'.format(w_c))
    print('The enthalpy at stage 02 is: {:.2f} kJ/kg'.format(h02))

    # Stage 03
    comb_pLoss = specs['pres_drop_combustor'].values[0]
    eff_comb = specs['eff_combustor'].values[0]
    eff_comb_test = 0.97
    # TIT = specs['TIT [K]'].values[0]
    p03 = p02i * (1- comb_pLoss)
    TIT_test = 1400
    h03, s03 = stage03(TIT_test, h02, eff_comb_test, p03)
    print('The enthalpy at stage 03 is: {:.2f} kJ/kg'.format(h03))
    print('The entropy at stage 03 is: {:.5f} kJ/kg-K'.format(s03))

    # Stage 04i
    s04i = s03


