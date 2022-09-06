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

