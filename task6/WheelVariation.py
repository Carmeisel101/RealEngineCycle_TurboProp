from OL_repeater import*
from Steps import*



def WheelVar(OL_df, w_c_n, N_n, m_air_n, pi_c_n, eff_inlet, h_01_n, eff_combust, AreaRatio, gamma_g, ratio2, eff_turb, eff_noz, lamb):


    gamma = 1.4
    minL = 14.66
    OL_df = OL_df
    df = pd.DataFrame({'pi_c': []})
    df['pi_c'] = [OL_df['pi_c'][0], OL_df['pi_c'][1], 7.99]
    df['N'] = [OL_df['N'][0], OL_df['N'][1], 49000]
    df['eff_c'] = [0.849, 0.877, 0.8325]
    df['w_c'] = w_c_n*(df['N']/N_n)**2
    df['m_air'] = m_air_n*((df['pi_c']/pi_c_n)*(N_n/df['N']))
    df['pi_d'] = eff_inlet*(1)**(gamma/(gamma-1))
    df['h_02'] = h_01_n + df['w_c']

    df['pH_p03'] = 1 / (eff_combust * df['pi_d'] * df['pi_c'])
    df['K'] = ((1 / AreaRatio) ** 2) * ((df['pH_p03']) ** (2 / gamma_g)) * (
                1 - ((df['pH_p03']) ** ((gamma_g - 1) / gamma_g)) - ratio2 * (1 / eff_turb))
    df['ratio3'] = eff_turb * (1 - ((df['pH_p03']) ** ((gamma_g - 1) / gamma_g)) - df['K'] * (AreaRatio ** 2) * (
                1 / (df['pH_p03']) ** (2 / gamma_g)))

    df['h_03'] = df['w_c'] / df['ratio3']
    df['F_sp'] = eff_noz* (np.sqrt((2*(df['h_03']*1e3)*(1-(1/(df['pi_d']*df['pi_c']*eff_combust))**((gamma_g-1)/gamma_g)))- (h_01_n*1e3)*((df['pi_c']**((gamma_g-1)/gamma_g)-1)/(df['eff_c']))))*(1+(1/(lamb*minL)))
    df['TSFC'] = (3600/df['F_sp'])*(1/(lamb*minL))
    df['Thrust'] = df['F_sp']*df['m_air']
    return df

