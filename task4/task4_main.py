import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from steps import *



if __name__ == '__main__':

    table_2_1 = pd.read_csv('Table2.1.csv')
    table_2_3 = pd.read_csv('Table2.3.csv')
    task1_results = pd.read_csv('../task1/results.csv')
    task1_results2 = pd.read_csv('../task1/results2.csv')




    pi_star_n = 9.2
    eta_n = 0.89 # true for real cycles
    n_tostart = 1.05
    eta_tostart = 0.98
    ca_cabase_start = 0.8
    eta_ref  = eta_n/ eta_tostart
    gamma = 1.4
    m_air = task1_results2['m_air'][0] # kg/s

    pi_star_ratios, pi_star =  part1(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma)
    # print('pi_star_ratios = \n', pi_star_ratios) ####### deliveable
    # print('pi_star = \n', pi_star) ####### deliveable
    m_mbase = part2(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios)
    # print('m_mbase = \n', m_mbase)
    pi_bar, m_dot_bar = part3(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios, m_mbase)
    # print('pi_bar = \n', pi_bar)
    # print('m_dot_bar = \n', m_dot_bar)

    eta = part4(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_start, gamma, pi_star_ratios, m_mbase, pi_bar, m_dot_bar, eta_ref)
    # print('eta = \n', eta)

    ca_cabase_2 = 0.9
    pi_star_ratios2, pi_star2 =  part1(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_2, gamma)
    m_mbase2 = part2(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_2, gamma, pi_star_ratios2)
    pi_bar2, m_dot_bar2 = part3(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_2, gamma, pi_star_ratios2, m_mbase2)
    eta2 = part4(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_2, gamma, pi_star_ratios2, m_mbase2, pi_bar2, m_dot_bar2, eta_ref)
    # print('eta2 = \n', eta2)

    ca_cabase_3 = 1.0
    pi_star_ratios3, pi_star3 =  part1(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_3, gamma)
    m_mbase3 = part2(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_3, gamma, pi_star_ratios3)
    pi_bar3, m_dot_bar3 = part3(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_3, gamma, pi_star_ratios3, m_mbase3)
    eta3 = part4(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_3, gamma, pi_star_ratios3, m_mbase3, pi_bar3, m_dot_bar3, eta_ref)
    # print('eta3 = \n', eta3)

    ca_cabase_4 = 1.1
    pi_star_ratios4, pi_star4 =  part1(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_4, gamma)
    m_mbase4 = part2(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_4, gamma, pi_star_ratios4)
    pi_bar4, m_dot_bar4 = part3(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_4, gamma, pi_star_ratios4, m_mbase4)
    eta4 = part4(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_4, gamma, pi_star_ratios4, m_mbase4, pi_bar4, m_dot_bar4, eta_ref)
    # print('eta4 = \n', eta4)

    ca_cabase_5 = 1.2
    pi_star_ratios5, pi_star5 =  part1(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_5, gamma)
    m_mbase5 = part2(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_5, gamma, pi_star_ratios5)
    pi_bar5, m_dot_bar5 = part3(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_5, gamma, pi_star_ratios5, m_mbase5)
    eta5 = part4(table_2_1, table_2_3, pi_star_n, eta_n, n_tostart, ca_cabase_5, gamma, pi_star_ratios5, m_mbase5, pi_bar5, m_dot_bar5, eta_ref)

    # print('eta5 = \n', eta5)

    Table_2_4_1 = pd.DataFrame({'0.8': pi_star, '0.9': pi_star2, '1.0': pi_star3, '1.1': pi_star4, '1.2': pi_star5})
    Table_2_4_2 = pd.DataFrame({'0.8': pi_star_ratios, '0.9': pi_star_ratios2, '1.0': pi_star_ratios3, '1.1': pi_star_ratios4, '1.2': pi_star_ratios5})
    print('Table_2_4_1 = \n', Table_2_4_1)
    Table_2_4_1.to_csv('Table_2_4_1.csv')
    print('Table_2_4_2 = \n', Table_2_4_2)
    Table_2_4_2.to_csv('Table_2_4_2.csv')
    Table_2_5 = pd.DataFrame({'0.8': m_mbase, '0.9': m_mbase2, '1.0': m_mbase3, '1.1': m_mbase4, '1.2': m_mbase5})
    print('Table_2_5 = \n', Table_2_5)
    Table_2_5.to_csv('Table_2_5.csv')

    m_ref = m_air/1.02
    m_dot_1 = part5(table_2_1, m_mbase, m_ref)
    m_dot_2 = part5(table_2_1, m_mbase2, m_ref)
    m_dot_3 = part5(table_2_1, m_mbase3, m_ref)
    m_dot_4 = part5(table_2_1, m_mbase4, m_ref)
    m_dot_5 = part5(table_2_1, m_mbase5, m_ref)


    table_2_2 = pd.DataFrame({'m_dot_bar':[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1],
                                'pi_bar':[0.425, 0.5, 0.57, 0.64, 0.73, 0.83, 0.95, 1.09, 1.22, 1.37]})



    pi_ref = 9.2/1.1
    m_dot_plot = m_ref * table_2_2['m_dot_bar']
    pi_star_surge = pi_ref * table_2_2['pi_bar']


    plot_fun1  = m_dot_1
    plot_fun2  = m_dot_2
    plot_fun3  = m_dot_3
    plot_fun4  = m_dot_4
    plot_fun5  = m_dot_5
    surge_plot = m_dot_plot


    plot_real_fun1 = [plot_fun1[0], plot_fun2[0], plot_fun3[0], plot_fun4[0], plot_fun5[0]]
    plot_real_fun2 = [plot_fun1[1], plot_fun2[1], plot_fun3[1], plot_fun4[1], plot_fun5[1]]
    plot_real_fun3 = [plot_fun1[2], plot_fun2[2], plot_fun3[2], plot_fun4[2], plot_fun5[2]]
    plot_real_fun4 = [plot_fun1[3], plot_fun2[3], plot_fun3[3], plot_fun4[3], plot_fun5[3]]
    plot_real_fun5 = [plot_fun1[4], plot_fun2[4], plot_fun3[4], plot_fun4[4], plot_fun5[4]]
    plot_real_fun6 = [plot_fun1[5], plot_fun2[5], plot_fun3[5], plot_fun4[5], plot_fun5[5]]
    plot_real_fun7 = [plot_fun1[6], plot_fun2[6], plot_fun3[6], plot_fun4[6], plot_fun5[6]]
    plot_real_fun8 = [plot_fun1[7], plot_fun2[7], plot_fun3[7], plot_fun4[7], plot_fun5[7]]

    eta_line1 = [eta[0], eta2[0], eta3[0], eta4[0], eta5[0]]
    eta_line2 = [eta[1], eta2[1], eta3[1], eta4[1], eta5[1]]
    eta_line3 = [eta[2], eta2[2], eta3[2], eta4[2], eta5[2]]
    eta_line4 = [eta[3], eta2[3], eta3[3], eta4[3], eta5[3]]
    eta_line5 = [eta[4], eta2[4], eta3[4], eta4[4], eta5[4]]
    eta_line6 = [eta[5], eta2[5], eta3[5], eta4[5], eta5[5]]
    eta_line7 = [eta[6], eta2[6], eta3[6], eta4[6], eta5[6]]
    eta_line8 = [eta[7], eta2[7], eta3[7], eta4[7], eta5[7]]

    pi_line1 = [pi_star[0], pi_star2[0], pi_star3[0], pi_star4[0], pi_star5[0]]
    pi_line2 = [pi_star[1], pi_star2[1], pi_star3[1], pi_star4[1], pi_star5[1]]
    pi_line3 = [pi_star[2], pi_star2[2], pi_star3[2], pi_star4[2], pi_star5[2]]
    pi_line4 = [pi_star[3], pi_star2[3], pi_star3[3], pi_star4[3], pi_star5[3]]
    pi_line5 = [pi_star[4], pi_star2[4], pi_star3[4], pi_star4[4], pi_star5[4]]
    pi_line6 = [pi_star[5], pi_star2[5], pi_star3[5], pi_star4[5], pi_star5[5]]
    pi_line7 = [pi_star[6], pi_star2[6], pi_star3[6], pi_star4[6], pi_star5[6]]
    pi_line8 = [pi_star[7], pi_star2[7], pi_star3[7], pi_star4[7], pi_star5[7]]

    # Plot all five curves on the same plot
    plt.plot(plot_real_fun1, eta_line1, label = 'n = 0.5')
    plt.plot(plot_real_fun2, eta_line2, label = 'n = 0.6')
    plt.plot(plot_real_fun3, eta_line3, label = 'n = 0.7')
    plt.plot(plot_real_fun4, eta_line4, label = 'n = 0.8')
    plt.plot(plot_real_fun5, eta_line5, label = 'n = 0.9')
    plt.plot(plot_real_fun6, eta_line6, label = 'n = 1.0')
    plt.plot(plot_real_fun7, eta_line7, label = 'n = 1.05')
    plt.plot(plot_real_fun8, eta_line8, label = 'n = 1.1')


    plt.xlabel('$\dot{m}$  $\dfrac{kg}{s}$')
    plt.ylabel('$\eta$')
    plt.legend()
    plt.title('Compressor Map $\eta$ vs mass flow rate')
    plt.show()

    # plt.savefig('CompressorMap1.png', dpi=300)


    plt.plot(plot_real_fun1, pi_line1, label = 'n = 0.5')
    plt.plot(plot_real_fun2, pi_line2, label = 'n = 0.6')
    plt.plot(plot_real_fun3, pi_line3, label = 'n = 0.7')
    plt.plot(plot_real_fun4, pi_line4, label = 'n = 0.8')
    plt.plot(plot_real_fun5, pi_line5, label = 'n = 0.9')
    plt.plot(plot_real_fun6, pi_line6, label = 'n = 1.0')
    plt.plot(plot_real_fun7, pi_line7, label = 'n = 1.05')
    plt.plot(plot_real_fun8, pi_line8, label = 'n = 1.1')

    plt.plot(surge_plot, pi_star_surge, label='Surge Line')
    plt.xlabel('$\dot{m}$  $\dfrac{kg}{s}$')
    plt.ylabel('$\pi^{*}$')
    plt.legend()
    plt.title('Compressor Map $\pi^{*}$ vs mass flow rate')
    plt.show()
    # save the image with a big size
    # plt.savefig('CompressorMap2.png', dpi=300)

    plt.plot(surge_plot, pi_star_surge, label='Surge Line')
    plt.xlabel('$\dot{m}$  $\dfrac{kg}{s}$')
    plt.ylabel('$\pi^{*}$')
    plt.title('Surge Line')
    plt.legend()
    plt.show()
    # plt.savefig('./images/CompressorMap3.png', dpi=300)





