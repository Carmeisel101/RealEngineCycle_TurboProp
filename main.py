import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from winGasProp import GasProp


if __name__ == '__main__':
    # This is a demo of the winGasProp module
    GP = GasProp()
    GP.combustion(lamb= 1.5)
    GP.air()
    Temp = GP.T(300)
    print(Temp)

