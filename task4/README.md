## __Task 4__

This folder contains the code for designing a row of the Compressor map for the Axial Compressor. This task is full of tables, which will be broken down into detail down below.

`task4_main.py` is the main file which calls the other files and runs the code. Readers are to run this code to perfom the analysis.


`Table2.1.csv` contains the data from Table 2.1 in Dr. Cizmas' notes. This data is used to calculate the values for the compressor map. This table is read in by `task4_main.py` and is used to calculate the values for the compressor map. Table 2.1 is shown below:

<div align="center">

| $\bar{n}$ | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 | 1.05 | 1.1 |
|:---------:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|:---:|
| $\bar{\eta}_{base}$ | 0.9 | 0.924 | 0.955 | 0.97 | 1.0 | 1.0 | 0.98 | 0.975|  
| $\bar{\dot{m}}_{base}$ | 0.37 | 0.47 | 0.58 | 0.714 | 0.86 | 1.0 | 1.02 | 1.04 |
| $\bar{\pi}_{base}$ | 0.47 | 0.51 | 0.59 | 0.7 | 0.82 | 1.0 | 1.1 | 1.2 |

</div>

Where, 

<div align="center">

$\bar{n}$ = $\frac{n}{n_{ref}}$

$\bar{\eta}_{base} = \frac{\eta_{base}}{\eta_{ref}}$

$\bar{\dot{m}}_{base} = \frac{\dot{m}_{base}}{\dot{m}_{ref}}$

$\bar{\pi}_{base} = \frac{\pi^*_{base}}{\pi^*_{ref}}$

</div>

`Table2.3.csv` contains the data from Table 2.3 in Dr. Cizmas' notes. This data is used to calculate the values for the compressor map. This table is read in by `task4_main.py` and is used to calculate the values for the compressor map. Table 2.3 is shown below:

<div align="center">

| $\frac{\bar{C_{a}}}{\bar{C}_{a_{base}}}$ | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 |
|:----------------------------------------:|:---:|:---:|:---:|:----:|:---:|
| $\frac{\eta}{\eta_{base}}$ | 0.92 | 0.98 | 1 | 0.97 | 0.885 | 
| $\frac{w}{w_{base}}$ | 1.25 | 1.12 | 1 | 0.9 | 0.82 |

</div>

Where,

<div align="center">

$w = \frac{h^*_{1}}{\eta}(\pi^{* \frac{\gamma-1}{\gamma}} - 1)$

$h^{*}_{1} = \frac{w\eta}{\pi^{* \frac{\gamma-1}{\gamma}} - 1}$

</div>

Similarly we can say, 

<div align="center">

$h^{*}_1 = \frac{w_{base}\eta_{base}}{\pi^{* \frac{\gamma-1}{\gamma}}_{base} - 1}$

</div>

Making use of these equations, we can write the following:

<div align="center">

$\pi^{*} = \left[ 1+(\pi^{* \frac{\gamma - 1}{\gamma}}_{base} -1) \frac{w \eta}{w_{base}\eta_{base}}\right]^{\frac{\gamma}{\gamma - 1}}$

</div>

`steps.py` contains the 4 different steps that Dr. Cizmas has outlined in his notes. The steps are as follows:

1. Calculate $\pi^{*} = \pi^{*}(\bar{n}, \frac{\bar{C_{a}}}{\bar{C}_{a_{base}}})$ and $\frac{\pi^{*}}{\pi^{*}_{base}} = f(\bar{n}, \frac{\bar{C_{a}}}{\bar{C}_{a_{base}}})$, where $\bar{n} \in (0.5, 1.1)$ and $\frac{\bar{C_{a}}}{\bar{C}_{a_{base}}} \in (0.8, 1.2)$ producing a table as shown in Table 2.4.1 & Table 2.4.2. (Tables are in `Table_2_4_1.csv` and `Table_2_4_2.csv` respectively)

<div align="center">

| $\frac{\bar{C_{a}}}{\bar{C}_{a_{base}}}$ | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | $\bar{n}$ |
|:----------------------------------------:|:---:|:---:|:---:|:----:|:---:|:---------:|
| $\pi^{*}$ | ||||| 0.5 |
| $\pi^{*}$ | ||||| 0.6 |
| $\pi^{*}$ | ||||| 0.7 |
| $\pi^{*}$ | ||||| 0.8 |
| $\pi^{*}$ | ||||| 0.9 |
| $\pi^{*}$ | ||||| 1.0 |
| $\pi^{*}$ | ||||| 1.05 |
| $\pi^{*}$ | ||||| 1.1 |

| $\frac{\bar{C_{a}}}{\bar{C}_{a_{base}}}$ | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | $\bar{n}$ |
|:----------------------------------------:|:---:|:---:|:---:|:----:|:---:|:---------:|
| $\frac{\pi^{ * }}{\pi^{ * }_{base}}$ | ||||| 0.5 |
| $\frac{\pi^{ * }}{\pi^{ * }_{base}}$ | ||||| 0.6 |
| $\frac{\pi^{ * }}{\pi^{ * }_{base}}$ | ||||| 0.7 |
| $\frac{\pi^{ * }}{\pi^{ * }_{base}}$ | ||||| 0.8 |
| $\frac{\pi^{ * }}{\pi^{ * }_{base}}$ | ||||| 0.9 |
| $\frac{\pi^{ * }}{\pi^{ * }_{base}}$ | ||||| 1.0 |
| $\frac{\pi^{ * }}{\pi^{ * }_{base}}$ | ||||| 1.05 |
| $\frac{\pi^{ * }}{\pi^{ * }_{base}}$ | ||||| 1.1 |



</div>

2. Calculate $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}} = f(\frac{\bar{C_{a}}}{\bar{C}_{a_{base}}})$ by making use of:

<div align="center">

$\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}} = \frac{\bar{C_{a}}}{\bar{C}_{a_{base}}}\left[\frac{\pi^{*}}{\pi^{*}_{base}}\right]^{\frac{1}{3}}$

</div>

Simarly to step 1, Table 2.5 is produced. (Table is in `Table_2_5.csv`)

<div align="center">

| $\frac{\bar{C_{a}}}{\bar{C}_{a_{base}}}$ | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | $\bar{n}$ |
|:----------------------------------------:|:---:|:---:|:---:|:----:|:---:|:---------:|
| $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ | ||||| 0.5 |
| $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ | ||||| 0.6 |
| $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ | ||||| 0.7 |
| $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ | ||||| 0.8 |
| $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ | ||||| 0.9 |
| $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ | ||||| 1.0 |
| $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ | ||||| 1.05 |
| $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ | ||||| 1.1 |

</div>

3. Calculate $\bar{\pi} = \bar{\pi}(\bar{n}, \frac{\bar{C_{a}}}{\bar{C}_{a_{base}}})$ and $\bar{\dot{m}} = \bar{\dot{m}}(\bar{n}, \frac{\bar{C_{a}}}{\bar{C}_{a_{base}}})$. Note that:

<div align="center">

$\bar{\pi} = \bar{\pi}_{base} \frac{\pi^{*}}{\pi^{*}_{base}}$

</div>

Where $\bar{\pi}_{base}$ comes from `Table2.1.csv` and $\frac{\pi^{*}}{\pi^{*}_{base}}$ comes from `Table_2_4_2.csv`. Similarly:

<div align="center">

$\bar{\dot{m}} = \bar{\dot{m}}_{base} \frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$

</div>

Where $\bar{\dot{m}}_{base}$ comes from `Table2.1.csv` and $\frac{\bar{\dot{m}}}{\bar{\dot{m}}_{base}}$ comes from `Table_2_5.csv`.

4. Calculate $\eta = \eta (\bar{n}, \frac{\bar{C_{a}}}{\bar{C}_{a_{base}}})$ using tables `Table2.1.csv` and `Table2.3.csv`.

5. Lastly we are to draw the compressor map, with axes $\dot{m}\frac{\sqrt{T^{ * }_{1}}}{p^{ * }_{1}}$.