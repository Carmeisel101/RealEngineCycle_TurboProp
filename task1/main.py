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

    # Stage 02i
    pi_0c = specs['Compressor Ratio'].values[0]
    h02i, w_ci, p02i, s02i = stage02i(pi_0c, p01, s01, h01)

    # Stage 02
    eff_c = specs['eff_compressor'].values[0]
    s02, w_c, h02, p02 = stage02(p02i, w_ci, h01, eff_c)
    print('Compressor Work:', w_c)

    # Stage 03
    comb_pLoss = specs['pres_drop_combustor'].values[0]
    eff_comb = 1
    TIT = specs['TIT [K]'].values[0]
    p03 = p02i * (1- comb_pLoss)
    h03, s03, excess_air, r, q = stage03(TIT, h02, eff_comb, p03)

    # Stage 04i
    s04i = s03
    eff_turbine = specs['eff_turbine'].values[0]
    h04i, w_t, T04i, p04i = stage04i(h03, w_c, excess_air, eff_turbine, r, q, s04i)

    # Stage 04
    p04 = p04i
    s04, T04, h04 = stage04(p04, w_t, h03, r, q)

    # Stage 04.5i
    s045i = s04
    SHP = specs['Shaft horse power [kW]'].values[0]
    eff_free_turbine = specs['eff_free_turbine'].values[0]
    m_air = 1.64089 #1.365303689 # kg/s
    w_PT, T045i, h045i, p045i, m_g, m_fuel = stage045i(SHP, m_air, excess_air, eff_free_turbine, h04, r, q, s045i)

    # Stage 045
    p045 = p045i
    h045, s045, T045 = stage045(p045, w_PT, h04, r, q)

    # Stage 5i
    s5i = s045
    # p5i = p01/1e5
    p5i = 1.128  # calculated the critical pressure
    eff_nozzle = specs['eff_nozzle'].values[0]
    eff_propeller = specs['eff_propeller'].values[0]
    T5i, h5i, c5, Spec_Thrust, EBSFC = stage5i(r, q, s5i, p5i, h045, eff_nozzle, m_air,
                                                      excess_air, eff_propeller, SHP, m_fuel)



    # Make a Table of the results for each stage
    stages = ['01', '02i', '02', '03', '04i', '04', '045i', '045', '5i']
    p = [p01/1e5, p02i, p02, p03, p04i, p04, p045i, p045, p5i]
    h = [h01, h02i, h02, h03, h04i, h04, h045i, h045, h5i]
    s = [s01, s02i, s02, s03, s04i, s04, s045i, s045, s5i]

    print('m_air = ', m_air, 'kg/s')
    print('m_fuel = ', m_fuel, 'kg/s')
    print('Specific Thrust = ', Spec_Thrust, 'N')
    print('EBSFC = ', EBSFC)
    print('TIT = ', TIT, 'K')

    df = pd.DataFrame({'Stage': stages, 'Pressure [Pa]': p, 'Enthalpy [kJ/kg]': h, 'Entropy [kJ/kg-K]': s})
    print(df)

#     df to csv
    df.to_csv('results.csv')

    df2 = pd.DataFrame({'w_c': w_c, 'w_t': w_t, 'w_PT': w_PT, 'SHP': SHP, 'm_air': m_air, 'm_fuel': m_fuel, 'Spec_Thrust': Spec_Thrust, 'EBSFC': EBSFC, 'TIT': TIT}, index=[0])
    df2.to_csv('results2.csv')
    







