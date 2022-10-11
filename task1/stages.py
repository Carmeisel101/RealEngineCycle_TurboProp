import pandas as pd
import numpy as np
from math import *
from winGasProp import GasProp
from Iterations import Iterate_temp_h
from Iterations import Iterate_temp_ps
from Iterations import stoich_tabs

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
    return h02i, w_ci, p02i, s02i

def stage02(p02i, w_ci, h01, eff_c):
    GP = GasProp()
    GP.air()
    w_c = w_ci / eff_c
    p02 = p02i
    h02 = h01 + w_c
    s02_1bar = GP.s(h=h02, p=1)
    s02 = s02_1bar - 0.28716 * np.log(p02)
    return s02, w_c, h02, p02

def stage03( TIT, h02, eff_comb, p03):
    minL = 14.66
    LHV = 43.5e3
    GP = GasProp()
    GP.air()
    h03_air = GP.h(T=TIT)
    GP.combustion(lamb=1)
    h03_stoich = GP.h(T=TIT)
    excess_air = (h03_stoich*(1+minL)-(eff_comb*LHV)-(h03_air*minL)) / (minL*(h02 - h03_air))
    r = (1+minL)/(1+(excess_air*minL))
    q= 1-r
    h03 = r*h03_stoich + q*h03_air
    s03_stoich_1bar = GP.s(T=TIT, p=1)
    GP.air()
    s03_air_1bar = GP.s(T=TIT, p=1)
    s03_1bar_mix = r*s03_stoich_1bar + q*s03_air_1bar
    s03 = s03_1bar_mix - 0.28716 * np.log(p03)
    return h03, s03, excess_air, r, q

def stage04i(h03, w_c, excess_air, eff_turbine, r, q, s04i):
    minL = 14.66
    w_t = w_c*(1/(1+(1/(minL*excess_air))))
    w_ti = w_t/eff_turbine
    h04i = h03 - w_ti
    T04i = Iterate_temp_h(h04i, r, q)
    GP = GasProp()
    GP.air()
    s04i_1bar_air = GP.s(T=T04i, p=1)
    GP.combustion(lamb=1)
    s04i_1bar_stoich = GP.s(T=T04i, p=1)
    s04i_1bar_mix = r*s04i_1bar_stoich + q*s04i_1bar_air
    p04i = exp(-(s04i - s04i_1bar_mix)/0.28716)

    return h04i, w_t, T04i, p04i

def stage04(p04, w_t, h03, r, q):
    h04 = h03 - w_t
    T04 = Iterate_temp_h(h04, r, q)
    GP = GasProp()
    GP.air()
    s04_1bar_air = GP.s(T=T04, p=1)
    GP.combustion(lamb=1)
    s04_1bar_stoich = GP.s(T=T04, p=1)
    s04_1bar_mix = r*s04_1bar_stoich + q*s04_1bar_air
    s04 = s04_1bar_mix - 0.28716 * np.log(p04)
    return s04, T04, h04

def stage045i(SHP, m_air, excess_air, eff_free_turbine, h04, r, q, s045i):
    minL = 14.66
    f = 1 / (minL * excess_air)
    w_PT = SHP/(m_air*(1+(1/(minL*excess_air))))
    # print('w_PT = ', w_PT)
    w_PTi = w_PT/eff_free_turbine
    m_g = SHP/w_PT # mass flow rate of gas
    m_fuel = m_air * f
    # m_air_sol = m_g*(1+(1/(minL*excess_air)))
    h045i = h04 - w_PTi
    T045i = Iterate_temp_h(h045i, r, q)
    GP = GasProp()
    GP.air()
    s045i_1bar_air = GP.s(T=T045i, p=1)
    GP.combustion(lamb=1)
    s045i_1bar_stoich = GP.s(T=T045i, p=1)
    s045i_1bar_mix = r*s045i_1bar_stoich + q*s045i_1bar_air
    p045i = exp(-(s045i - s045i_1bar_mix)/0.28716)
    return w_PT, T045i, h045i, p045i, m_g, m_fuel

def stage045(p045, w_PT, h04, r, q):
    h045 = h04 - w_PT
    # print('h045', h045)
    T045 = Iterate_temp_h(h045, r, q)
    # print('T045', T045)
    GP = GasProp()
    GP.air()
    s045_1bar_air = GP.s(T=T045, p=1)
    # print('s045_1bar_air', s045_1bar_air)
    GP.combustion(lamb=1)
    s045_1bar_stoich = GP.s(T=T045, p=1)
    # print('s045_1bar_stoich', s045_1bar_stoich)
    s045_1bar_mix = r*s045_1bar_stoich + q*s045_1bar_air
    # print('s045_1bar_mix', s045_1bar_mix)
    s045 = s045_1bar_mix - 0.28716 * np.log(p045)
    return h045, s045, T045


def stage5i(r, q, s05i, p5i, h045, eff_nozzle, m_air, excess_air, eff_propeller, SHP, m_fuel):
    s05i_1bar = s05i + 0.28716 * np.log(p5i)
    minL = 14.66
    GP = GasProp()
    GP.air()
    T5i_air = GP.T(s=s05i_1bar, p=1)
    GP.combustion(lamb=1)
    # T5i_stoich = GP.T(s=s05i_1bar, p=1)
    # print('s05i_1bar', s05i_1bar)
    T5i_stoich = stoich_tabs(s05i_1bar)

    # T5i_stoich = 859.16 # HARDCODED VALUE FIX THIS LATER
    T5i = r*T5i_stoich + q*T5i_air

    # T5i = Iterate_temp_ps(s05i_1bar, r, q)
    h5i_stoich = GP.h(T=T5i)
    GP.air()
    h5i_air = GP.h(T=T5i)
    h5i = r*h5i_stoich + q*h5i_air

    c5i = sqrt(2*((h045*1000) - (h5i*1000)))
    c5 = c5i * eff_nozzle
    Spec_Thrust = m_air*c5*(1+(1/(minL*excess_air)))
    equiv_shaftPower = eff_propeller*SHP+(Spec_Thrust/11.1)
    # print('m_fuel', m_fuel*60*60)
    print('equiv_shaftPower =', equiv_shaftPower, 'kW')
    EBSFC = (m_fuel*60*60)/equiv_shaftPower

    return T5i, h5i, c5, Spec_Thrust, EBSFC