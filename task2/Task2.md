## __Task 2__

This folder contains the code for designing the axial component of a mixed compressor. The code is written in Python. 

* `redo_comp.py` is the main code for Task 2. Users are to run this file to perform the mixed compressor design.

* `Iter.py` is a file that contains the functions for the iterative process for solving for the degree of reaction. 
    * The iterative process is the root of the equation:
    $$ 0 = \frac{1}{C_{u_{1}}} \left[ \frac{\left( W_{u_{1}}-(\frac{W_{s}}{2U}) \right)(\frac{w_{u}}{U})}{R'}-C_{a_{1}}\Delta^sC_{a}-w_{s} \right] - \Delta^sC_{u}$$

* `Data.xlsx` is an Excel file that contains data pulled from task 1. Data from this file is read by the `redo_comp.py` file.

* `comp_stages.csv` contains the results of the mixed compressor design. This file is created by the `redo_comp.py` file.