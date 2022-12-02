import pandas as pd
import numpy as np
from sympy import Eq, solve, var
from Iterations import *

def altspeedvar(pi_d, pi_c_n, eff_noz, eff_combust, AreaRatio, gamma_g, ratio2, eff_turb, h_02_n, eff_com, lamb, h_01_n, m_air_n, p_01):

    variation_df = pd.read_csv('AltSpeedVariation.csv')

    variation_df['gamma'] = variation_df['a']**2 /(287.16 * variation_df['T'])
    variation_df['c_p'] = variation_df['gamma'] * 287.16 / (variation_df['gamma'] - 1)
    variation_df['h'] = variation_df['c_p'] * variation_df['T']




    v_df = pd.DataFrame({'v': variation_df['v']})
    # drop nan values in v_df
    v_df = v_df.dropna()


    # Step 1
    df = pd.DataFrame({'M_H1':[]})
    df['M_H1'] = v_df['v'] / np.sqrt(variation_df['gamma'][0] * 287.16 * variation_df['T'][0])
    df['M_H2'] = v_df['v'] / np.sqrt(variation_df['gamma'][1] * 287.16 * variation_df['T'][1])
    df['M_H3'] = v_df['v'] / np.sqrt(variation_df['gamma'][2] * 287.16 * variation_df['T'][2])
    df['M_H4'] = v_df['v'] / np.sqrt(variation_df['gamma'][3] * 287.16 * variation_df['T'][3])
    df['M_H5'] = v_df['v'] / np.sqrt(variation_df['gamma'][4] * 287.16 * variation_df['T'][4])
    df['M_H6'] = v_df['v'] / np.sqrt(variation_df['gamma'][5] * 287.16 * variation_df['T'][5])
    df['M_H7'] = v_df['v'] / np.sqrt(variation_df['gamma'][6] * 287.16 * variation_df['T'][6])
    df['M_H8'] = v_df['v'] / np.sqrt(variation_df['gamma'][7] * 287.16 * variation_df['T'][7])
    df['M_H9'] = v_df['v'] / np.sqrt(variation_df['gamma'][8] * 287.16 * variation_df['T'][8])

    # Step 2
    pi_d_df = pd.DataFrame({'pi_d_1': []})
    pi_d_df['pi_d_1'] = pi_d * (1 + (variation_df['gamma'][0] - 1) / 2 * df['M_H1'] ** 2) ** (variation_df['gamma'][0] / (variation_df['gamma'][0] - 1))
    pi_d_df['pi_d_2'] = pi_d * (1 + (variation_df['gamma'][1] - 1) / 2 * df['M_H2'] ** 2) ** (variation_df['gamma'][1] / (variation_df['gamma'][1] - 1))
    pi_d_df['pi_d_3'] = pi_d * (1 + (variation_df['gamma'][2] - 1) / 2 * df['M_H3'] ** 2) ** (variation_df['gamma'][2] / (variation_df['gamma'][2] - 1))
    pi_d_df['pi_d_4'] = pi_d * (1 + (variation_df['gamma'][3] - 1) / 2 * df['M_H4'] ** 2) ** (variation_df['gamma'][3] / (variation_df['gamma'][3] - 1))
    pi_d_df['pi_d_5'] = pi_d * (1 + (variation_df['gamma'][4] - 1) / 2 * df['M_H5'] ** 2) ** (variation_df['gamma'][4] / (variation_df['gamma'][4] - 1))
    pi_d_df['pi_d_6'] = pi_d * (1 + (variation_df['gamma'][5] - 1) / 2 * df['M_H6'] ** 2) ** (variation_df['gamma'][5] / (variation_df['gamma'][5] - 1))
    pi_d_df['pi_d_7'] = pi_d * (1 + (variation_df['gamma'][6] - 1) / 2 * df['M_H7'] ** 2) ** (variation_df['gamma'][6] / (variation_df['gamma'][6] - 1))
    pi_d_df['pi_d_8'] = pi_d * (1 + (variation_df['gamma'][7] - 1) / 2 * df['M_H8'] ** 2) ** (variation_df['gamma'][7] / (variation_df['gamma'][7] - 1))
    pi_d_df['pi_d_9'] = pi_d * (1 + (variation_df['gamma'][8] - 1) / 2 * df['M_H9'] ** 2) ** (variation_df['gamma'][8] / (variation_df['gamma'][8] - 1))

    # Step 3 - h_H
    h_df = pd.DataFrame({'h_1': []})
    h_df['h_1'] = variation_df['h'][0] * (1 + (variation_df['gamma'][0] - 1) / 2 * df['M_H1'] ** 2)
    h_df['h_2'] = variation_df['h'][1] * (1 + (variation_df['gamma'][1] - 1) / 2 * df['M_H2'] ** 2)
    h_df['h_3'] = variation_df['h'][2] * (1 + (variation_df['gamma'][2] - 1) / 2 * df['M_H3'] ** 2)
    h_df['h_4'] = variation_df['h'][3] * (1 + (variation_df['gamma'][3] - 1) / 2 * df['M_H4'] ** 2)
    h_df['h_5'] = variation_df['h'][4] * (1 + (variation_df['gamma'][4] - 1) / 2 * df['M_H5'] ** 2)
    h_df['h_6'] = variation_df['h'][5] * (1 + (variation_df['gamma'][5] - 1) / 2 * df['M_H6'] ** 2)
    h_df['h_7'] = variation_df['h'][6] * (1 + (variation_df['gamma'][6] - 1) / 2 * df['M_H7'] ** 2)
    h_df['h_8'] = variation_df['h'][7] * (1 + (variation_df['gamma'][7] - 1) / 2 * df['M_H8'] ** 2)
    h_df['h_9'] = variation_df['h'][8] * (1 + (variation_df['gamma'][8] - 1) / 2 * df['M_H9'] ** 2)



    w_c_df = pd.DataFrame({'w_c_1': []})
    w_c_df['w_c_1'] = (h_02_n*1e3) - h_df['h_1']
    w_c_df['w_c_2'] = (h_02_n*1e3) - h_df['h_2']
    w_c_df['w_c_3'] = (h_02_n*1e3) - h_df['h_3']
    w_c_df['w_c_4'] = (h_02_n*1e3) - h_df['h_4']
    w_c_df['w_c_5'] = (h_02_n*1e3) - h_df['h_5']
    w_c_df['w_c_6'] = (h_02_n*1e3) - h_df['h_6']
    w_c_df['w_c_7'] = (h_02_n*1e3) - h_df['h_7']
    w_c_df['w_c_8'] = (h_02_n*1e3) - h_df['h_8']
    w_c_df['w_c_9'] = (h_02_n*1e3) - h_df['h_9']



    # Step 4
    pi_c_df = pd.DataFrame({'pi_c_1': []})
    pi_c_df['pi_c_1'] = (1 + (variation_df['h'][0]/h_df['h_1'])*((pi_c_n**((variation_df['gamma'][0]-1)/variation_df['gamma'][0]))-1))**(variation_df['gamma'][0]/(variation_df['gamma'][0]-1))
    pi_c_df['pi_c_2'] = (1 + (variation_df['h'][1]/h_df['h_2'])*((pi_c_n**((variation_df['gamma'][1]-1)/variation_df['gamma'][1]))-1))**(variation_df['gamma'][1]/(variation_df['gamma'][1]-1))
    pi_c_df['pi_c_3'] = (1 + (variation_df['h'][2]/h_df['h_3'])*((pi_c_n**((variation_df['gamma'][2]-1)/variation_df['gamma'][2]))-1))**(variation_df['gamma'][2]/(variation_df['gamma'][2]-1))
    pi_c_df['pi_c_4'] = (1 + (variation_df['h'][3]/h_df['h_4'])*((pi_c_n**((variation_df['gamma'][3]-1)/variation_df['gamma'][3]))-1))**(variation_df['gamma'][3]/(variation_df['gamma'][3]-1))
    pi_c_df['pi_c_5'] = (1 + (variation_df['h'][4]/h_df['h_5'])*((pi_c_n**((variation_df['gamma'][4]-1)/variation_df['gamma'][4]))-1))**(variation_df['gamma'][4]/(variation_df['gamma'][4]-1))
    pi_c_df['pi_c_6'] = (1 + (variation_df['h'][5]/h_df['h_6'])*((pi_c_n**((variation_df['gamma'][5]-1)/variation_df['gamma'][5]))-1))**(variation_df['gamma'][5]/(variation_df['gamma'][5]-1))
    pi_c_df['pi_c_7'] = (1 + (variation_df['h'][6]/h_df['h_7'])*((pi_c_n**((variation_df['gamma'][6]-1)/variation_df['gamma'][6]))-1))**(variation_df['gamma'][6]/(variation_df['gamma'][6]-1))
    pi_c_df['pi_c_8'] = (1 + (variation_df['h'][7]/h_df['h_8'])*((pi_c_n**((variation_df['gamma'][7]-1)/variation_df['gamma'][7]))-1))**(variation_df['gamma'][7]/(variation_df['gamma'][7]-1))
    pi_c_df['pi_c_9'] = (1 + (variation_df['h'][8]/h_df['h_9'])*((pi_c_n**((variation_df['gamma'][8]-1)/variation_df['gamma'][8]))-1))**(variation_df['gamma'][8]/(variation_df['gamma'][8]-1))

    # Step 5

    pH_p03_df = pd.DataFrame({'pH_p03_1': []})
    pH_p03_df['pH_p03_1'] = 1/(eff_combust*pi_c_df['pi_c_1']*pi_d_df['pi_d_1'])
    pH_p03_df['pH_p03_2'] = 1/(eff_combust*pi_c_df['pi_c_2']*pi_d_df['pi_d_2'])
    pH_p03_df['pH_p03_3'] = 1/(eff_combust*pi_c_df['pi_c_3']*pi_d_df['pi_d_3'])
    pH_p03_df['pH_p03_4'] = 1/(eff_combust*pi_c_df['pi_c_4']*pi_d_df['pi_d_4'])
    pH_p03_df['pH_p03_5'] = 1/(eff_combust*pi_c_df['pi_c_5']*pi_d_df['pi_d_5'])
    pH_p03_df['pH_p03_6'] = 1/(eff_combust*pi_c_df['pi_c_6']*pi_d_df['pi_d_6'])
    pH_p03_df['pH_p03_7'] = 1/(eff_combust*pi_c_df['pi_c_7']*pi_d_df['pi_d_7'])
    pH_p03_df['pH_p03_8'] = 1/(eff_combust*pi_c_df['pi_c_8']*pi_d_df['pi_d_8'])
    pH_p03_df['pH_p03_9'] = 1/(eff_combust*pi_c_df['pi_c_9']*pi_d_df['pi_d_9'])

    K_df = pd.DataFrame({'K_1': []})
    K_df['K_1'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_1']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_1']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    K_df['K_2'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_2']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_2']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    K_df['K_3'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_3']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_3']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    K_df['K_4'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_4']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_4']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    K_df['K_5'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_5']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_5']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    K_df['K_6'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_6']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_6']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    K_df['K_7'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_7']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_7']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    K_df['K_8'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_8']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_8']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    K_df['K_9'] =  ((1 / AreaRatio) ** 2) * ((pH_p03_df['pH_p03_9']) ** (2 / gamma_g)) * (1 - ((pH_p03_df['pH_p03_9']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))

    ratio3_df = pd.DataFrame({'ratio3_1': []})
    ratio3_df['ratio3_1'] = eff_turb * (1 - ((pH_p03_df['pH_p03_1']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_1'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_1']) ** (2 / gamma_g)))
    ratio3_df['ratio3_2'] = eff_turb * (1 - ((pH_p03_df['pH_p03_2']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_2'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_2']) ** (2 / gamma_g)))
    ratio3_df['ratio3_3'] = eff_turb * (1 - ((pH_p03_df['pH_p03_3']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_3'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_3']) ** (2 / gamma_g)))
    ratio3_df['ratio3_4'] = eff_turb * (1 - ((pH_p03_df['pH_p03_4']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_4'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_4']) ** (2 / gamma_g)))
    ratio3_df['ratio3_5'] = eff_turb * (1 - ((pH_p03_df['pH_p03_5']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_5'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_5']) ** (2 / gamma_g)))
    ratio3_df['ratio3_6'] = eff_turb * (1 - ((pH_p03_df['pH_p03_6']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_6'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_6']) ** (2 / gamma_g)))
    ratio3_df['ratio3_7'] = eff_turb * (1 - ((pH_p03_df['pH_p03_7']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_7'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_7']) ** (2 / gamma_g)))
    ratio3_df['ratio3_8'] = eff_turb * (1 - ((pH_p03_df['pH_p03_8']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_8'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_8']) ** (2 / gamma_g)))
    ratio3_df['ratio3_9'] = eff_turb * (1 - ((pH_p03_df['pH_p03_9']) ** ((gamma_g - 1) / gamma_g)) - K_df['K_9'] * (AreaRatio ** 2) * (1 / (pH_p03_df['pH_p03_9']) ** (2 / gamma_g)))

    h_03_df = pd.DataFrame({'h_03_1': []})
    h_03_df['h_03_1'] = w_c_df['w_c_1']/ratio3_df['ratio3_1']
    h_03_df['h_03_2'] = w_c_df['w_c_2']/ratio3_df['ratio3_2']
    h_03_df['h_03_3'] = w_c_df['w_c_3']/ratio3_df['ratio3_3']
    h_03_df['h_03_4'] = w_c_df['w_c_4']/ratio3_df['ratio3_4']
    h_03_df['h_03_5'] = w_c_df['w_c_5']/ratio3_df['ratio3_5']
    h_03_df['h_03_6'] = w_c_df['w_c_6']/ratio3_df['ratio3_6']
    h_03_df['h_03_7'] = w_c_df['w_c_7']/ratio3_df['ratio3_7']
    h_03_df['h_03_8'] = w_c_df['w_c_8']/ratio3_df['ratio3_8']
    h_03_df['h_03_9'] = w_c_df['w_c_9']/ratio3_df['ratio3_9']

    print('h_03_df = ', h_03_df)

    minL = 14.66

    lamb1 = lamb_solver(h_02_n, eff_combust, h_03_df, 1)
    lamb2 = lamb_solver(h_02_n, eff_combust, h_03_df, 2)
    lamb3 = lamb_solver(h_02_n, eff_combust, h_03_df, 3)
    lamb4 = lamb_solver(h_02_n, eff_combust, h_03_df, 4)
    lamb5 = lamb_solver(h_02_n, eff_combust, h_03_df, 5)
    lamb6 = lamb_solver(h_02_n, eff_combust, h_03_df, 6)
    lamb7 = lamb_solver(h_02_n, eff_combust, h_03_df, 7)
    lamb8 = lamb_solver(h_02_n, eff_combust, h_03_df, 8)
    lamb9 = lamb_solver(h_02_n, eff_combust, h_03_df, 9)

    lamb_df = pd.DataFrame({'lamb_1': lamb1, 'lamb_2': lamb2, 'lamb_3': lamb3, 'lamb_4': lamb4, 'lamb_5': lamb5, 'lamb_6': lamb6, 'lamb_7': lamb7, 'lamb_8': lamb8, 'lamb_9': lamb9})
    # print(lamb_df)

    F_sp_df = pd.DataFrame({'F_sp_1': []})
    F_sp_df['F_sp_1'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_1']) * (
                1 - (1 / (pi_d_df['pi_d_1'] * pi_c_df['pi_c_1'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_1'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_1'] * minL))) - v_df['v']
    F_sp_df['F_sp_2'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_2']) * (
                1 - (1 / (pi_d_df['pi_d_2'] * pi_c_df['pi_c_2'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_2'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_2'] * minL))) - v_df['v']
    F_sp_df['F_sp_3'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_3']) * (
                1 - (1 / (pi_d_df['pi_d_3'] * pi_c_df['pi_c_3'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_3'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_3'] * minL))) - v_df['v']
    F_sp_df['F_sp_4'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_4']) * (
                1 - (1 / (pi_d_df['pi_d_4'] * pi_c_df['pi_c_4'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_4'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_4'] * minL))) - v_df['v']
    F_sp_df['F_sp_5'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_5']) * (
                1 - (1 / (pi_d_df['pi_d_5'] * pi_c_df['pi_c_5'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_5'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_5'] * minL))) - v_df['v']
    F_sp_df['F_sp_6'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_6']) * (
                1 - (1 / (pi_d_df['pi_d_6'] * pi_c_df['pi_c_6'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_6'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_6'] * minL))) - v_df['v']
    F_sp_df['F_sp_7'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_7']) * (
                1 - (1 / (pi_d_df['pi_d_7'] * pi_c_df['pi_c_7'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_7'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_7'] * minL))) - v_df['v']
    F_sp_df['F_sp_8'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_8']) * (
                1 - (1 / (pi_d_df['pi_d_8'] * pi_c_df['pi_c_8'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_8'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_8'] * minL))) - v_df['v']
    F_sp_df['F_sp_9'] = eff_noz * (np.sqrt((2 * (h_03_df['h_03_9']) * (
                1 - (1 / (pi_d_df['pi_d_9'] * pi_c_df['pi_c_9'] * eff_combust)) ** ((gamma_g - 1) / gamma_g))) - (
                                                       h_01_n * 1e3) * (
                                                       (pi_c_df['pi_c_9'] ** ((gamma_g - 1) / gamma_g) - 1) / (
                                                   0.88)))) * (1 + (1 / (lamb_df['lamb_9'] * minL))) - v_df['v']

    print('lambda', lamb_df)
    print('pi_c', pi_c_df)
    print('pi_d', pi_d_df)


    m_dot_air_df = pd.DataFrame({'m_dot_air_1': []})
    m_dot_air_df['m_dot_air_1'] = m_air_n*(pi_c_df['pi_c_1']/pi_c_n)*(variation_df['p'][0]/p_01) *((1+((variation_df['gamma'][0]-1)/2)*df['M_H1']**2)**((variation_df['gamma'][0])/(variation_df['gamma'][0]-1)))
    m_dot_air_df['m_dot_air_2'] = m_air_n*(pi_c_df['pi_c_2']/pi_c_n)*(variation_df['p'][1]/p_01) *((1+((variation_df['gamma'][1]-1)/2)*df['M_H2']**2)**((variation_df['gamma'][1])/(variation_df['gamma'][1]-1)))
    m_dot_air_df['m_dot_air_3'] = m_air_n*(pi_c_df['pi_c_3']/pi_c_n)*(variation_df['p'][2]/p_01) *((1+((variation_df['gamma'][2]-1)/2)*df['M_H3']**2)**((variation_df['gamma'][2])/(variation_df['gamma'][2]-1)))
    m_dot_air_df['m_dot_air_4'] = m_air_n*(pi_c_df['pi_c_4']/pi_c_n)*(variation_df['p'][3]/p_01) *((1+((variation_df['gamma'][3]-1)/2)*df['M_H4']**2)**((variation_df['gamma'][3])/(variation_df['gamma'][3]-1)))
    m_dot_air_df['m_dot_air_5'] = m_air_n*(pi_c_df['pi_c_5']/pi_c_n)*(variation_df['p'][4]/p_01) *((1+((variation_df['gamma'][4]-1)/2)*df['M_H5']**2)**((variation_df['gamma'][4])/(variation_df['gamma'][4]-1)))
    m_dot_air_df['m_dot_air_6'] = m_air_n*(pi_c_df['pi_c_6']/pi_c_n)*(variation_df['p'][5]/p_01) *((1+((variation_df['gamma'][5]-1)/2)*df['M_H6']**2)**((variation_df['gamma'][5])/(variation_df['gamma'][5]-1)))
    m_dot_air_df['m_dot_air_7'] = m_air_n*(pi_c_df['pi_c_7']/pi_c_n)*(variation_df['p'][6]/p_01) *((1+((variation_df['gamma'][6]-1)/2)*df['M_H7']**2)**((variation_df['gamma'][6])/(variation_df['gamma'][6]-1)))
    m_dot_air_df['m_dot_air_8'] = m_air_n*(pi_c_df['pi_c_8']/pi_c_n)*(variation_df['p'][7]/p_01) *((1+((variation_df['gamma'][7]-1)/2)*df['M_H8']**2)**((variation_df['gamma'][7])/(variation_df['gamma'][7]-1)))
    m_dot_air_df['m_dot_air_9'] = m_air_n*(pi_c_df['pi_c_9']/pi_c_n)*(variation_df['p'][8]/p_01) *((1+((variation_df['gamma'][8]-1)/2)*df['M_H9']**2)**((variation_df['gamma'][8])/(variation_df['gamma'][8]-1)))

    F_sp_n = 785.967693
    TSFC_n = 3600/(lamb*minL) *(1/F_sp_n)
    print('TSFC_n', TSFC_n)



    TSFC_df = pd.DataFrame({'TSFC_1': []})
    TSFC_df['TSFC_1'] = (lamb/lamb_df['lamb_1']) * (F_sp_n/F_sp_df['F_sp_1']) * (TSFC_n)
    TSFC_df['TSFC_2'] = (lamb/lamb_df['lamb_2']) * (F_sp_n/F_sp_df['F_sp_2']) * (TSFC_n)
    TSFC_df['TSFC_3'] = (lamb/lamb_df['lamb_3']) * (F_sp_n/F_sp_df['F_sp_3']) * (TSFC_n)
    TSFC_df['TSFC_4'] = (lamb/lamb_df['lamb_4']) * (F_sp_n/F_sp_df['F_sp_4']) * (TSFC_n)
    TSFC_df['TSFC_5'] = (lamb/lamb_df['lamb_5']) * (F_sp_n/F_sp_df['F_sp_5']) * (TSFC_n)
    TSFC_df['TSFC_6'] = (lamb/lamb_df['lamb_6']) * (F_sp_n/F_sp_df['F_sp_6']) * (TSFC_n)
    TSFC_df['TSFC_7'] = (lamb/lamb_df['lamb_7']) * (F_sp_n/F_sp_df['F_sp_7']) * (TSFC_n)
    TSFC_df['TSFC_8'] = (lamb/lamb_df['lamb_8']) * (F_sp_n/F_sp_df['F_sp_8']) * (TSFC_n)
    TSFC_df['TSFC_9'] = (lamb/lamb_df['lamb_9']) * (F_sp_n/F_sp_df['F_sp_9']) * (TSFC_n)



    TSFC_df.to_csv('./resultTables/TSFC.csv')
    m_dot_air_df.to_csv('./resultTables/m_dot_air.csv')
    F_sp_df.to_csv('./resultTables/F_sp.csv')
    lamb_df.to_csv('./resultTables/lamb.csv')
    pi_c_df.to_csv('./resultTables/pi_c.csv')
    variation_df.to_csv('./resultTables/variation.csv')
    df.to_csv('./resultTables/df.csv')
    h_03_df.to_csv('./resultTables/h_03.csv')
    w_c_df.to_csv('./resultTables/w_c.csv')
    h_df.to_csv('./resultTables/h.csv')
    K_df.to_csv('./resultTables/K.csv')
    ratio3_df.to_csv('./resultTables/ratio3.csv')
    pH_p03_df.to_csv('./resultTables/pH_p03.csv')
    v_df.to_csv('./resultTables/v.csv')
    pi_d_df.to_csv('./resultTables/pi_d.csv')










    return df, pi_d_df, h_df, pi_c_df, F_sp_df, v_df, m_dot_air_df, TSFC_df