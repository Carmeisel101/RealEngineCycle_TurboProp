import numpy as np
from sympy import Eq, var, solve

def iteration(cu, Wu, w, U, ca, delta_ca, stage_index, delta_cu_list):
    r = var('r')
    delta_cu = (1 / cu) * ((((Wu - (w[stage_index] / (2 * U))) * (w[stage_index] / U))
                            / (r)) - ca * delta_ca[stage_index] - w[stage_index])
    eq = Eq(delta_cu, delta_cu_list[stage_index])
    sol = solve(eq, r)
    return sol


# U1 = 247.5
# Wu1 = 234.4077216823964
# cu1 = 13.0922783176036
# ca1 = 74.25
# r_init = 0.717
# delta_ca1 = 1
# w = [28000.0, 34000.0, 43955.1250000000, 36000.0]
# stage_index = 0 # stage 1
# delta_cu_list = [1.957, 2.068, 1.278, 3.247]

# sol = iteration(cu1, Wu1, w, U1, ca1, delta_ca1, stage_index, delta_cu_list)
# print(sol)