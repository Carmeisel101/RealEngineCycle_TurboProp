import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

v_in = 157.5/157.5 # non-dimensional inlet velocity
rho_in = 1 # non-dimensional inlet density
gamma = 1.4
R = 287.058 # J/kgK
T_in = 288.16 # K
c_in = (np.sqrt(gamma*R*T_in))/(157.5) # m/s
print('c_in = ', c_in)

M_in = v_in/c_in # non-dimensional inlet Mach number
print('M_in = ', M_in)

p_in = (1*c_in**2)/gamma
print('p_in = ', p_in)

p_0_in = p_in*(1+(gamma-1)/2*M_in**2)**(-gamma/(gamma-1))

rho_0_in = rho_in*(1+(gamma-1)/2*M_in**2)**(-1/(gamma-1))

ALPHAD1 = 44.6 # degrees

FLUX = v_in * np.cos(ALPHAD1*np.pi/180) # non-dimensional flux
VTAN = v_in * np.sin(ALPHAD1*np.pi/180) # non-dimensional tangential velocity

UINIT = FLUX
VINIT = VTAN

print("UINIT = ", UINIT)
print("VINIT = ", VINIT)

print("p_0_in = ", p_0_in)
print("rho_0_in = ", rho_0_in)




