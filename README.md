# BACTOMATA 

.- an heterotic hybrid computing device based on a coevolving system composed of (in vivo) bacterial plasmid populations and (in silico) elementary cellular automata (ECA) rules that update the physical state of the bacterial growth environment. 

The system acts as an autonomous unsupervised installation with the capacity of generating a responsive dialog between an evolving primordial open-ended biological entity and a simple algorithmic rule whose computational complexity is Turing complete. 

The device is physically actuated by a micro-pipetting robot that performs serial transfers of bacterial populations in discrete intervals and also inoculates its growth substrate in 96-well plates. The sensory feedback layer of the system is based on an open microscope working on a RaspPi that measures bacterial optical density at each time-step and performs an update in the ECA rule. 

This cross-domain association involves the combination of two computational substrates in one computational system whose output cannot be expressed as the sum of its individual components.  In addition, this dual propagation in time of entangled bacterial-bit states may be framed as an instantiation of a novel communication modality allying two primordial intelligences without an explicit anthropocentric interference.

## System Diagram

![alt text](https://github.com/carlestapi/BACTOMATA/blob/main/bactomata%20diagram.png)

## // Plasmid Population Dynamics Model under ECA Environments //

* Parameters:

params.conj_rate= 0;
params.S0= 1;
params.T= 24;
params.d= 0.1;
params.cs= [877563800 984410100];
params.Ks= [1 1];
params.species={'E'  'E'};
params.plasmids= {'TC'  'WT'};
params.strains={'X1'  'X1'};
params.numStrains= 1;
params.MIC_AMC=[dose_max*MIC, 32]; 
#params.MIC_AMC= [32768 32];
params.MIC_MER= [4 1];
params.MIC_IMP= [16 0.5000];
params.MIC_ERT= [16 0.5000];
params.conj_freq= [0 0];
dose_max=32768; 
params.seg_rate=seg_rate;
params.Vs= [cost*Vmax Vmax];
params.extinction_threshold=1e1;

* Limited-resource coupled non-linear differential equation model parameters:

```math
\begin{gathered}
$$
\bar{B}=\left(B_p^1, B_p^2, \ldots, B_p^N, B_0^1, B_0^2, \ldots, B_0^N\right) \\
\frac{d R}{d t}=-\sum_{j=1}^N\left(U\left(R(t) ; \psi_p^j\right) \cdot B_p^j(t)+U\left(R(t) ; \psi_0^j\right) \cdot B_0^j(t)\right) \\
\frac{d A}{d t}=-\alpha A(t) \cdot \sum_{j=1}^N\left(B_p^j(t)+B_0^i(t)\right) . \\
\frac{d B_0^i}{d t}=\left(G\left(R ; \psi_0^i\right)-\kappa_0 A\right) \cdot B_0^i(t)+\sigma G\left(R ; \psi_p^i\right) \cdot B_p^i(t)-\gamma^i B_0^i(t) \sum_{j=1}^N B_p^j(t) \\
\frac{d B_p^i}{d t}=\left(G\left(R ; \psi_p^i\right)-\kappa_p A-\sigma\right) \cdot B_p^i(t)+\gamma^i B_0^i(t) \sum_{j=1}^N B_p^j(t)
$$
\end{gathered}
```

## // Simulations under ECA Environments //

* Population Dynamics in Serial Transfer Times

![alt text](https://github.com/carlestapi/BACTOMATA/blob/main/rule30_50.gif)

* Evolving ECA Plasmid Fractions

![alt text](https://github.com/carlestapi/BACTOMATA/blob/main/AC_Bactomatons.gif)

