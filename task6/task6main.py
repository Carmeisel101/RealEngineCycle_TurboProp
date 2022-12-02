import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Steps import *
from macGasProp import GasProp
from Iterations import *
from OL_repeater import *
from WheelVariation import *
from mpl_toolkits.axes_grid1 import host_subplot
from AltSpeedVariation import *


if __name__ == '__main__':

    specs_df = pd.read_csv('../task1/BasicSpecs.csv')
    task1_r2_df = pd.read_csv('../task1/results2.csv')
    task1_r1_df = pd.read_csv('../task1/results.csv')
    task2_df = pd.read_csv('../task2/comp_stages.csv')


    TIT = specs_df['TIT [K]'][0]
    eff_turb = specs_df['eff_turbine'][0]
    w_c_n = task1_r2_df['w_c'][0]
    pi_c = specs_df['Compressor Ratio'][0]
    eff_com = specs_df['eff_compressor'][0]
    # eff_com = 0.79
    N_n = task2_df['n'][0]
    m_air = task1_r2_df['m_air'][0]
    T_01 = 288.16 # K
    lamb = task1_r2_df['lambda'][0]
    gamma = 1.4
    minL = 14.66
    eff_combust = 0.90
    m_ref = 1.6087156862745098
    p_03 = task1_r1_df['Pressure [bar]'][5]
    p_03 = p_03 * 10**5
    p_01 = task1_r1_df['Pressure [bar]'][1]
    p_01 = p_01 * 10**5
    h_03_n = task1_r1_df['Enthalpy [kJ/kg]'][5]
    h_01_n = task1_r1_df['Enthalpy [kJ/kg]'][2]
    h_02_n = task1_r1_df['Enthalpy [kJ/kg]'][4]
    eff_noz = specs_df['eff_nozzle'][0]
    # cp = 1.004516 # kJ/kgK
    x = 2.1
    pi_d = 0.93
    AreaRatio = 1.2 # A3.5/A5



    w_c, N, N_r = step1(N_n, w_c_n, x)
    print('w_c = ', w_c, 'kJ/kg')
    print('N = ', N, 'rpm')
    print('N_r = ', N_r, 'rpm')

    pi_c_star, eff_com_iter = step2(N, gamma, N_n, pi_c, eff_com, x)
    print('pi_c_star = ', pi_c_star)
    print('eff_com_iter = ', eff_com_iter)

    T_03 = step3(eff_combust, minL, lamb, m_air, T_01, p_03, TIT, p_01, pi_c_star, m_ref)
    print('T_03 = ', T_03)
    r = (1+minL)/(1+minL*lamb)
    q = ((lamb-1)*minL)/(1+minL*lamb)

    h_a = air_tabT(T_03)
    h_stoich = stoich_tabT(T_03)


    h_03 = r  * h_stoich + q * h_a
    print('h_03 = ', h_03)

    ratio1 = w_c/h_03
    ratio2 = w_c_n/(h_03_n)
    print('ratio1 = ', ratio1)
    print('ratio2 = ', ratio2)
#     percent difference in ratio 1 and 2
    print('percent difference in ratio 1 and 2 = ', abs(ratio1-ratio2)/ratio2*100, '%')

    gamma_g_stoich = 1.27134999
    gamma_g_a = 1.3232644

    gamma_g = r * gamma_g_stoich + q * gamma_g_a
    print('gamma_g = ', gamma_g)
    pi_c_star_crt, eta_cr, N_cr, N_lower = step4(N_n, pi_d, eff_combust, gamma_g, ratio2, eff_turb, T_01,
                          N, eff_com, gamma, pi_c, N_r)
    print('pi_c_star_crt = ', pi_c_star_crt)
    print('eta_cr = ', eta_cr)
    print('N_cr = ', N_cr, 'rpm')

    # n_list = [N_cr*1.025, N_cr*1.05, N_cr*1.075]

    pH_p03, K, ratio3, pi_c_star_5 = step5(AreaRatio, eff_combust, pi_d, pi_c_star_crt, eff_turb, ratio2, gamma_g, 0.95)
    print('pH_p03 = ', pH_p03)
    print('K = ', K)
    print('ratio3 = ', ratio3)

    w_c_p6, N_p6 = step6(w_c_n, x, N_n, N_lower)
    print('w_c_p6 = ', w_c_p6, 'kJ/kg')
    print('N_p6 = ', N_p6, 'rpm')

    h_03_p7 = step7(w_c_p6, ratio3)
    print('h_03_p7 = ', h_03_p7, 'kJ/kg')

    T_03_p8 = step8(h_03_p7, r, q)
    print('T_03_p8 = ', T_03_p8, 'K')

    #### Step 9 read
    T_03_10 = step10(eff_combust, minL, lamb, m_air, T_01, p_03, TIT, p_01, pi_c_star_5, m_ref)
    print('T_03_10 = ', T_03_10, 'K')



    loop_df = step1_3loop(w_c_n, x, N_cr, gamma, pi_c, eff_com, N_n, TIT,
                          m_ref, eff_combust, lamb, p_03, m_air, p_01, T_01, ratio2, r, q, gamma_g)
    print(loop_df)

    loop_df.to_csv('step3loop.csv', index=False)

    OL_df = OL_repeater(pi_c_star_crt, pi_d, eff_combust, AreaRatio, gamma_g, eff_turb, ratio2,
                        N_n, w_c_n, x, r, q, lamb, m_ref, m_air, TIT, p_01, T_01, p_03)
    print(OL_df)

    OL_df.to_csv('OL.csv', index=False)

    WheelVar_df = WheelVar(OL_df, w_c_n, N_n, m_air, pi_c, pi_d, h_01_n, eff_combust, AreaRatio, gamma_g, ratio2, eff_turb, eff_noz, lamb)
    print(WheelVar_df)

    WheelVar_df.to_csv('WheelVar.csv', index=False)


    WheelVarPlot_1 = [WheelVar_df['N'][1], WheelVar_df['N'][0], WheelVar_df['N'][2]]
    WheelVarPlot_2 =  [WheelVar_df['Thrust'][0], WheelVar_df['Thrust'][1], WheelVar_df['Thrust'][2]]
    WheelVarPlot_3 = [WheelVar_df['TSFC'][1], WheelVar_df['TSFC'][0], WheelVar_df['TSFC'][2]]

    host = host_subplot(111)
    par = host.twinx()

    host.set_xlabel("N")
    host.set_ylabel("Thrust [N]")
    par.set_ylabel("TSFC [kg/N hours]")

    p1, = host.plot(WheelVarPlot_1, WheelVarPlot_2, label="Thrust")
    p2, = par.plot(WheelVarPlot_1, WheelVarPlot_3, label="TSFC")

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par.axis["right"].label.set_color(p2.get_color())

    plt.show()

    mach_df, pi_d_df, h_df, pi_c_df, F_sp_df, v_df, m_dot_air_df, TSFC_df = altspeedvar(pi_d, pi_c, eff_noz, eff_combust, AreaRatio, gamma_g, ratio2, eff_turb, h_02_n, eff_com, lamb, h_01_n, m_air, p_01)

    print('F_sp_df = ', F_sp_df)

    F_1 = F_sp_df['F_sp_1'] * m_dot_air_df['m_dot_air_1']
    F_2 = F_sp_df['F_sp_2'] * m_dot_air_df['m_dot_air_2']
    F_3 = F_sp_df['F_sp_3'] * m_dot_air_df['m_dot_air_3']
    F_4 = F_sp_df['F_sp_4'] * m_dot_air_df['m_dot_air_4']
    F_5 = F_sp_df['F_sp_5'] * m_dot_air_df['m_dot_air_5']
    F_6 = F_sp_df['F_sp_6'] * m_dot_air_df['m_dot_air_6']
    F_7 = F_sp_df['F_sp_7'] * m_dot_air_df['m_dot_air_7']
    F_8 = F_sp_df['F_sp_8'] * m_dot_air_df['m_dot_air_8']
    F_9 = F_sp_df['F_sp_9'] * m_dot_air_df['m_dot_air_9']

    plt.plot(v_df['v'], F_1, label='H = 0 m')
    plt.plot(v_df['v'], F_2, label='H = 1000 m')
    plt.plot(v_df['v'], F_3, label='H = 3000 m')
    plt.plot(v_df['v'], F_4, label='H = 5000 m')
    plt.plot(v_df['v'], F_5, label='H = 6000 m')
    plt.plot(v_df['v'], F_6, label='H = 7000 m')
    plt.plot(v_df['v'], F_7, label='H = 8000 m')
    plt.plot(v_df['v'], F_8, label='H = 9000 m')
    plt.plot(v_df['v'], F_9, label='H = 10000 m')

    plt.xlabel('v [m/s]')
    plt.ylabel('F [N]')
    plt.title('F vs H-v')
    plt.legend()
    plt.show()

    plt.plot(v_df['v'], TSFC_df['TSFC_1'], label='H = 0 m')
    plt.plot(v_df['v'], TSFC_df['TSFC_2'], label='H = 1000 m')
    plt.plot(v_df['v'], TSFC_df['TSFC_3'], label='H = 3000 m')
    plt.plot(v_df['v'], TSFC_df['TSFC_4'], label='H = 5000 m')
    plt.plot(v_df['v'], TSFC_df['TSFC_5'], label='H = 6000 m')
    plt.plot(v_df['v'], TSFC_df['TSFC_6'], label='H = 7000 m')
    plt.plot(v_df['v'], TSFC_df['TSFC_7'], label='H = 8000 m')
    plt.plot(v_df['v'], TSFC_df['TSFC_8'], label='H = 9000 m')
    plt.plot(v_df['v'], TSFC_df['TSFC_9'], label='H = 10000 m')

    plt.xlabel('v [m/s]')
    plt.ylabel('TSFC [kg/N hours]')
    plt.title('TSFC vs H-v')
    plt.legend()
    plt.show()



