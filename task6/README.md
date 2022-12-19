## Task 6 - OLVHN

### Methodology for Computing the Operating Line 

1. Calculate the compressor work $w_{c}$ given a angular speed calculated in Task 2, as a function of nominal compressor work and nominal angular speed.

<div align="center">

$$w_{c} = w_{c,n} \left( \frac{N}{N_{n}} \right)^{x}$$

</div>

Usually, $x \in [1.9, 2.1]$, for convience, we start with $x = 2$.

2. Estimate the compressor efficiency $\eta_{c}$ given a angular speed calculated in Task 2, as a function of nominal compressor efficiency and nominal angular speed. We start by calculating the pressure ratio $\pi_{c}$:

<div align="center">

$$\pi_{c} = \left[ \left( \pi_{c,n}^{\frac{\gamma-1}{\gamma}} -1 \right) \frac{\eta_{c}}{\eta_{c,n}} \left( \frac{N}{N_{n}} \right)^{x} + 1\right]^{\frac{\gamma}{\gamma-1}}$$

</div>


For starting we can assume that $\eta_{c} = \eta_{c,n}$. From here we have the pressure ratio $\pi_{c}$, and the angular speed $N$, we can calculate the compressor efficiency $\eta_{c}$ by reading from the compressor map. If the efficiency is not equal to the nominal efficiency, iterate until it is. Allow a tolerance of 0.01%.

3. Calculate the $T_{3}^{ * }$ from:

<div align="center">

$$\pi_{c} = \frac{1+f}{\sigma_{comb}}\left( \frac{p_{3}^{ * }}{\dot{m}\sqrt{T_{3}^{ * }}} \right)_{n} \sqrt{\frac{T_{3}^{ * }}{T_{1}^{ * }}} \frac{\dot{m}\sqrt{T_{1}^{ * }}}{p_{1}^{ * }}$$

</div>

From here calculate $h_{3}^{ * }$:

<div align="center">

$$h_{3}^{ * } = \left(\frac{1+minL}{1+\lambda minL} \right) h_{\lambda = 1} + \left(\frac{(\lambda - 1)minL}{1+\lambda minL}\right)h_{air}$$

</div>

Check to see if the ratio $\frac{w_{c}}{h_{3}^{ * }}$ is equal to the nominal ratio. If not, iterate $x$ until it is. Allow a tolerance of 1%.

4. Now we move to critical conditions:

<div align="center">

$$\pi_{c_{cr}}^{ * } = \frac{1}{\sigma_{comb} \pi_{D}} \left[ \frac{\frac{\gamma_{g}+1}{2}}{1 - \frac{w_{c}}{h_{3}^{ * }} \frac{1}{\eta_{turbine}}} \right]^{\frac{\gamma_{g}}{\gamma_{g}-1}}$$

$$N_{cr} = N_{n} \sqrt{\frac{\eta_{c_{n}}}{\eta_{c_{cr}}}} \frac{\pi_{c_{cr}}^{\frac{\gamma - 1}{\gamma}} -1}{\pi_{c_{n}}^{\frac{\gamma -1}{\gamma}} - 1}$$

</div>

5. Once we are at critical conditions, our ratio $\frac{w_{c}}{h_{3}^{ * }}$ is no longer constant, to calculate it we now:

<div align="center">

$$\frac{w_{c}}{h_{3}^{ * }} = \eta_{turbine} \left[ 1 - \left(\frac{p_{H}}{p_{3}^{*}}\right)^{\frac{\gamma_{g}-1}{\gamma_{g}}} - K \left(\frac{A_{3.5}}{A_{5}}\right)^{2} \left(\frac{p_{3}^{ * }}{p_{H}}\right)^{\frac{2}{\gamma_{g}}} \right]$$

</div>

Where $K$ is calculated:

<div align="center">

$$K = \left(\frac{A_{5}}{A_{3.5}}\right)^{2} \left(\frac{p_{H}}{p_{3}^{ * }}\right)^{\frac{2}{\gamma_{g}}}\left[1 - \left(\frac{p_{H}}{p_{3}^{ * }}\right)^{\frac{\gamma_{g}-1}{\gamma_{g}}} \frac{w_{c}}{h_{3}^{ * }} \frac{1}{\eta_{turbine}}\right]$$

</div>

And $\frac{p_{H}}{{p_{3}^{ * }}}$ is calculated:

<div align="center">
 
 $$\frac{p_{H}}{p_{3}^{ * }} = \frac{1}{\sigma_{combustion}^{ * } \pi_{c}^{ * } \pi_{D}}$$

</div>

Recall:

<div align="center">

$$\pi_{D} = \frac{p_{1}^{ * }}{p_{H}}$$

</div>

User's are to choose a $\pi_{c}^{ * }$ that is less than the critical pressure ratio $\pi_{c_{cr}}^{ * }$

6. Now we are to choose an $N$ value smaller than the critical value $N_{cr}$, and calculate $w_{c}$.
  We chose a $N$ value that was 1\% less than the critical value.

<div align="center">

$$N < N_{cr}$$

</div>

7. Now calculate $h_{3}^{ * }$ from step 5, and the $w_{c}$ from step 6.

8. Now we are to calculate the $T_{3}^{ * }$ the stoichmetric and air gas tables. This step is performed in the `Iterate_temp_h` function in `Iterations.py`


```python
    def Iterate_temp_h(h, r, q):
        '''
        Iterates to find the temperature given the enthalpy and the stoichiometric ratio
        :param h: enthalpy
        :param r: stoichiometric ratio weighting factor
        :param q: air ratio weighting factor
        :return T: temperature
        '''


        T_air1 = air_tabh(h)
        h_air1 = h
        h_stoich1 = stoich_tabT(T_air1)
        f1 = h -r*h_stoich1 - q*h_air1

        T_comb2 = stoich_tabh(h_air1)
        h_air2 = air_tabT(T_comb2)
        h_stoich2 = h
        f2 = h -r*h_stoich2 - q*h_air2

        # linear interpolation
        T = (T_air1*f2 - T_comb2*f1)/(f2-f1)
        return T
```

The purpose of this function is to perform the alogrithm provided by Dr.Cizmas in _Example 5.2.4_ of his textbook. The temperature is the root of the equation:

<div align="center">

$$f(T) = h - r h_{stoich} - q h_{air} = 0$$

</div>

9. For a known value of $\pi_{c}^{ * }$ and $N$, read from the compressor map the value of the correctedmass flow rate.

10. Now determine $T_{3}^{ * }$ from the same equation in step 3.

11. Compare the values of $T_{3}^{ * }$ from step 8 to $T_{3}^{ * }$ from step 10, if they differ by more than 10 degrees K, then iterate until with different $N$ value.

12. Now choose another value of $\pi_{c}^{ * }$ and go back to step 5 and repeat the process to get other points on the operating line at $\frac{p_{H}}{p_{3}^{ * }}$ 