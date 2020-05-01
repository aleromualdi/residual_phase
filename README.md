# Residual Phase from LP residual

Residual phase calculation from the linear prediction (LP) reidual of a wave signal. 


# Usage

Being y an array containing samples from a wave signal, the residual phase of the sampled wave can be obtained with

```
from residualphase import ResidualPhase

RP = ResidualPhase()
res_phase = RP.calculate(y)
```

# Plot

Plot of the residual signal, as well as the original wave signal and the LP signal. 

![Image description](output/residual_signal.png)




