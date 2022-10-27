## __Task 2__

This folder contains the code for designing the axial component of a mixed compressor. The code is written in Python. 

* `redo_comp.py` is the main code for Task 2. Users are to run this file to perform the mixed compressor design.

* `Iter.py` is a file that contains the functions for the iterative process for solving for the degree of reaction. 
    * The iterative process is the root of the equation:
    $$0 = \frac{1}{C_{u_{1}}} \left[ \frac{\left( W_{u_{1}}-(\frac{W_{s}}{2U}) \right)(\frac{w_{u}}{U})}{R'}-C_{a_{1}}\Delta^sC_{a}-w_{s} \right] - \Delta^sC_{u}$$

* `Data.xlsx` is an Excel file that contains data pulled from task 1. Data from this file is read by the `redo_comp.py` file.

* `comp_stages.csv` contains the results of the mixed compressor design. This file is created by the `redo_comp.py` file. The table below shows the columns of this file.

| Stage| c_a | c_u | alpha | degree of reaction | u1m | c1a | w1 | w1u | D1_m | n | D1_t | D1_h|
|------|-----|-----|-------|--------------------|-----|-----|----|-----|------|----|------|-----|
| 1 | c_a1 | c_u1 | alpha1 | r_prime1 | u1m | c1a | w1 | w1u | D1_m | n | D1_t | D1_h|
| 2 | c_a2 | c_u2 | alpha2 | r_prime2 |  |  |  |  |  |  |  |  |
| 3 | c_a3 | c_u3 | alpha3 | r_prime3 |  |  |  |  |  |  |  |  |
| 4 | c_a4 | c_u4 | alpha4 | r_prime4 |  |  |  |  |  |  |  |  |

