# PLUMED Masterclass 22.3: OPES theory

## Introduction to the theory

The OPES method aims at sampling a given target distribution over the configuration space, $p^{\text{tg}}(\mathbf{x})$,
different from the equilibrium Boltzmann distribution, $P(\mathbf{x})\propto e^{-\beta U(\mathbf{x})}$.
To do so, it iteratively builds a bias potential $V(\mathbf{x})$, by estimating on-the-fly the needed probability distributions:

$$ V(\mathbf{x}) = -\frac{1}{\beta}\log\frac{p^{\text{tg}}(\mathbf{x})}{P(\mathbf{x})} .$$

The bias quickly becomes quasi-static and the desired properties, such as the free energy, can be calculated with a simple reweighting.
For any given observable $O=O(\mathbf{x})$ one can write the expectation value as:

$$ \langle O \rangle_{P} = \frac{\langle O e^{\beta V}\rangle_{p^{\text{tg}}}}{\langle e^{\beta V}\rangle_{p^{\text{tg}}}} .$$

There are two ways to define an OPES target distribution, a metadynamics-like and a replica-exchange-like.
A replica-exchange-like target distribution is an expanded ensemble defined as a sum of overlapping probability distributions:

$$ p^{\text{tg}}_{\{\lambda\}}(\mathbf{x})=\frac{1}{N_{\{\lambda\}}}\sum_{\lambda} P_{\lambda}(\mathbf{x}) .$$

A typical example is the temperature expanded ensemble, where each $P_{\lambda}(\mathbf{x})$ is the same system, but at a different temperature.
This kind of target distribution can be defined via a set of expansion collective variables (ECVs).
The action [OPES_EXPANDED](https://www.plumed.org/doc-master/user-doc/html/_o_p_e_s__e_x_p_a_n_d_e_d.html) can be used to sample this kind of target distributions.

A metadynamics-like target distribution, is defined by its marginal over a set of collective variables (CVs), $\mathbf{s}=\mathbf{s}(\mathbf{x})$.
A typical choice for this marginal distribution is the well-tempered one:

$$ p^{\text{WT}}(\mathbf{s})=\left[P(\mathbf{s})\right]^{1/\gamma} ,$$

where $P(\mathbf{s})$ is the marginal over the CVs of the Boltzmann distribution, and $\gamma>1$ is the bias factor.
The well-tempered distribution is a smoother version of the original one, and in the limit of $\gamma=\infty$ it become a uniform distribution.
The actions [OPES_METAD](https://www.plumed.org/doc-master/user-doc/html/_o_p_e_s__m_e_t_a_d.html) and [OPES_METAD_EXPLORE](https://www.plumed.org/doc-master/user-doc/html/_o_p_e_s__m_e_t_a_d__e_x_p_l_o_r_e.html) 
can be used to sample this kind of target distributions.
