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

Check to see if the ratio $\frac{w_{c}}{h_{3}^{ * }}$ is equal to the nominal ratio. If not, iterate until it is. Allow a tolerance of 1%.
