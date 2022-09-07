import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from winGasProp import GasProp
from stages import stage01
from stages import stage02i
from stages import stage02
from stages import stage03
from stages import stage04i
from stages import stage04
from stages import stage045i
from stages import stage045
from stages import stage5i

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
    h03, s03, excess_air, r, q = stage03(TIT_test, h02, eff_comb_test, p03)
    print('The enthalpy at stage 03 is: {:.2f} kJ/kg'.format(h03))
    print('The entropy at stage 03 is: {:.5f} kJ/kg-K'.format(s03))

    # Stage 04i
    s04i = s03
    eff_turbine = specs['eff_turbine'].values[0]
    eff_turbine_test = 0.89
    h04i, w_t, T04i, p04i = stage04i(h03, w_c, excess_air, eff_turbine_test, r, q, s04i)

    # Stage 04
    p04 = p04i
    s04, T04, h04 = stage04(p04, w_t, h03, r, q)
    print('The temperature at stage 04 is: {:.2f} K'.format(T04))
    print('The entropy at stage 04 is: {:.5f} kJ/kg-K'.format(s04))

    # Stage 4.5i
    s045i = s04
    SHP = specs['Shaft horse power [kW]'].values[0]
    eff_free_turbine = specs['eff_free_turbine'].values[0]
    eff_free_turbine_test = 0.88
    SHP_test = 6000
    m_air = specs['m_air'].values[0]
    m_air_test = 20
    w_PT, T045i, h045i, p045i = stage045i(SHP_test, m_air_test, excess_air, eff_free_turbine_test, h04, r, q, s045i)
    print('The power at stage 4.5i is: {:.2f} kJ/kg'.format(w_PT))
    print('The temperature at stage 4.5i is: {:.2f} K'.format(T045i))
    print('The enthalpy at stage 4.5i is: {:.2f} kJ/kg'.format(h045i))
    print('The pressure at stage 4.5i is: {:.2f} bar'.format(p045i))

    # Stage 045
    p045 = p045i
    h045, s045 = stage045(p045, w_PT, h04, r, q)
    print('The enthalpy at stage 045 is: {:.2f} kJ/kg'.format(h045))
    print('The entropy at stage 045 is: {:.5f} kJ/kg-K'.format(s045))

    # Stage 5i
    s05i = s045
    p5i = p01/1e5
    eff_nozzle = specs['eff_nozzle'].values[0]
    eff_propeller = specs['eff_propeller'].values[0]
    eff_propeller_test = 0.8
    eff_nozzle_test = 0.97
    T5i, h5i, c5, Spec_Thrust, m_fuel = stage5i(r, q, s05i, p5i, h045, eff_nozzle_test, m_air_test,
                                                      excess_air, eff_propeller_test, SHP_test)
    print('The temperature at stage 5i is: {:.2f} K'.format(T5i))
    print('The enthalpy at stage 5i is: {:.2f} kJ/kg'.format(h5i))
    print('The speed of gas at stage 5i is: {:.2f} m/s'.format(c5))
    print('The specific thrust at stage 5i is: {:.2f} N'.format(Spec_Thrust))
    print('The fuel mass flow rate at stage 5i is: {:.2f} kg/s'.format(m_fuel))







