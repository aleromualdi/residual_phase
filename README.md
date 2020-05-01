# Residual Phase from LP residual

Residual phase calculation from the linear prediction (LP) residual of a wave signal. <br>

The calculation of LP residual is equal to the error between the original signal and the LP-predicted signal.
From the LP residual, the residual phase is defined as the cosine of the phase function of the analytic signal.

# Usage

Being y an array containing samples from a wave signal, the residual phase of the sampled wave can be obtained with

```
from residualphase import ResidualPhase

RP = ResidualPhase()
res_phase = RP.calculate(y)
```

# Plot

Plot of the original signal (y), LP-predicted signal (lp) and LP residual (r). 


![Image description](output/residual_signal.png)




