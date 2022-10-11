## __Task 1__

This folder contains the code for the engine, as well as the engine specs. The code is written in Python. This code performs a full cycle analysis of the PT6A-114 engine, given the specs specificied in the `BasicSpecs.csv` file. 

* `main.py` is the main code for the engine. Users are to run this file to perform the full cycle analysis.
* `winGasProp.py` is the code for the gas properties. This code is called in the main code to calculate the gas properties. This is the "Cygwin" code provided by the Dr. Cizmas.
* `stoich_tab.csv` is the stoichiometric table for the engine. There are parts of the `winGasProp.py` code that through an error due to a translation issue from Fortran to Python for stoichmetric combustion. This file is a workaround for that issue.
* `stages.py` is the code for the engine stages. This code is called in the main code to calculate the engine stages.
* `Iterations.py` is the code for the iterations. This code is called in the main code to calculate the iterations. This code performs linear interpolation to find the values of the gas properties at the specified conditions from the stoich tables and it iterates gas properties to solve for Temperture.
    * Temperature iteration algorithm is based on the algorithm provided by Dr. Cizmas in his textbook _Example 5.2.4_. The Temperature is the root of the equations (For entropy and enthalpy, respectively),
    $$f(T) = h_{\lambda}-rh_{\lambda=1}(T) -qh_{a}(T) = 0$$
    $$f(T) = s_{\lambda}-rs_{\lambda=1}(T) -qs_{a}(T) = 0$$ 
    Where,
    $$r = \frac{1+minL}{1+\lambda minL}$$
    $$q = \frac{1+maxL}{1+\lambda maxL}$$
* `BasicSpecs.csv` contains the basic engine specs for the PT6A-114 engine. Users are to change the values in this file to perform the full cycle analysis for different engine specs. This file is read by the `main.py` file.
* `results.csv` contains the results of the full cycle analysis. This file is written by the `main.py` file. This `.csv` file is the pressure, enthalpy and temperature values for each stage of the engine. The table below shows the meaning of each column in the `results.csv` file.
    | Stages | Pressure [Pa] | Enthalpy [kJ/kg]  | Entropy [kJ/kg-K] | 
    | ------- | --- | --- | --- |
    | 01 | P_01 | h_01 | s_01 |
    | 02i | P_02i | h_02i | s_02i |
    | 02 | P_02 | h_02 | s_02 |
    | 03 | P_03 | h_03 | s_03 |
    | 04i | P_04i | h_04i | s_04i |
    | 04 | P_04 | h_04 | s_04 |
    | 045i | P_045i | h_045i | s_045i |
    | 045 | P_045 | h_045 | s_045 |
    | 05i | P_05i | h_05i | s_05i |

* `results2.csv` contains results from the cycle code that we plan to carry to task2. This file is written by the `main.py` file. The table below shows the meaning of each column.
    | work_compressor | work_turbine | work_PowerTurbine | SHP | m_air | m_fuel | Spec_Thrust | EBSFC | TIT |
    | --- | --- | --- | --- | --- | --- | --- | --- | --|
    | w_c | w_t | w_PT | SHP | m_air | m_fuel | Spec_Thrust | EBSFC | TIT |
