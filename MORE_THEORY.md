# PLUMED Masterclass 22.3: OPES method

## Calculating the temperatures at which to run the simulations

We choose 3 temperatures $T_0, T_1, T_2$, ranging from 300 K to 1000 K, and setup our GROMACS simulation to run at $T_0=300$ K.
Our target distribution is then:
$$
        p^{\text{tg}}(\mathbf{x})=\frac{1}{3}\left[\frac{e^{-\frac{1}{k_BT_0}U(\mathbf{x})}}{Z_0}+ \frac{e^{-\frac{1}{k_BT_1}U(\mathbf{x})}}{Z_1}+\frac{e^{-\frac{1}{k_BT_2}U(\mathbf{x})}}{Z_2}\right]
$$
This can be rewritten highlighting $P(\mathbf{x})$
$$
        p^{\text{tg}}(\mathbf{x})=P(\mathbf{x})\frac{1}{3}\left[1+ e^{-\left(\frac{1}{k_BT_1}-\frac{1}{k_BT_0}\right)U(\mathbf{x})}\frac{Z_0}{Z_1}+e^{-\left(\frac{1}{k_BT_2}-\frac{1}{k_BT_0}\right)U(\mathbf{x})}\frac{Z_0}{Z_2}\right]
$$ 
and then using $\Delta F_i = -k_B T_0 \log \frac{Z_i}{Z_0}$:
$$
        p^{\text{tg}}(\mathbf{x})=P(\mathbf{x})\frac{1}{3}\left[1+ e^{-\frac{1-T_0/T_1}{k_BT_0}U(\mathbf{x})+\frac{1}{k_BT_0}\Delta F_1}+e^{-\frac{1-T_0/T_2}{k_BT_0}U(\mathbf{x})+\frac{1}{k_BT_0}\Delta F_2}\right]
$$
so we just need to know $\Delta F_1$ and $\Delta F_2$, and we can sample the target multithermal distribution by using the following bias:
$$
  V(U) = - k_B T_0 \log \frac{1}{3}\left[1+ e^{-\frac{1-T_0/T_1}{k_BT_0}U(\mathbf{x})+\frac{1}{k_BT_0}\Delta F_1}+e^{-\frac{1-T_0/T_2}{k_BT_0}U(\mathbf{x})+\frac{1}{k_BT_0}\Delta F_2}\right]
$$
that is a function only of the potential energy $U=U(\mathbf{x})$.
In the OPES spirit, we estimate on-the-fly these free energy differences using a simple reweighting, and iteratively reach the target distribution.

The final bias expression is determined by these quantities $\frac{1-T_0/T_i}{k_BT_0}U(\mathbf{x})$, that we call [expansion_cv](https://www.plumed.org/doc-master/user-doc/html/expansion__c_v.html) (ECVs).
There are several types of expanded ensembles that might be of interest, and in order to sample them with OPES one simply needs to find the explicit form of the corresponding ECVs.
To sample the same expanded ensemble with replica exchange, one has to run a different replica of the system for each of the ECVs.
