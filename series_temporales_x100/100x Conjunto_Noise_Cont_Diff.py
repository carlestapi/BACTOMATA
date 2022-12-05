#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:50:26 2019

@author: carlestapi
"""

from __future__ import print_function, division

import thinkdsp
#import thinkplot
import numpy as np
#import pandas as pd
#import scipy.signal
#import math
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

####### Noise libs

from stochastic.processes.noise import BlueNoise
from stochastic.processes.noise import BrownianNoise
from stochastic.processes.noise import RedNoise
from stochastic.processes.noise import PinkNoise
from stochastic.processes.noise import VioletNoise
from stochastic.processes.noise import WhiteNoise
from stochastic.processes.noise import ColoredNoise
from stochastic.processes.noise import GaussianNoise
from stochastic.processes.noise import FractionalGaussianNoise

from fbm import MBM

####### Continuous libs

from stochastic.processes.continuous import BesselProcess
from stochastic.processes.continuous import BrownianBridge
from stochastic.processes.continuous import BrownianExcursion
from stochastic.processes.continuous import BrownianMeander
from stochastic.processes.continuous import BrownianMotion
from stochastic.processes.continuous import CauchyProcess
from stochastic.processes.continuous import FractionalBrownianMotion
from stochastic.processes.continuous import GammaProcess
from stochastic.processes.continuous import GeometricBrownianMotion
from stochastic.processes.continuous import InverseGaussianProcess
from stochastic.processes.continuous import MixedPoissonProcess
from stochastic.processes.continuous import MultifractionalBrownianMotion
from stochastic.processes.continuous import PoissonProcess
from stochastic.processes.continuous import SquaredBesselProcess
from stochastic.processes.continuous import VarianceGammaProcess
from stochastic.processes.continuous import WienerProcess

####### Diffusion libs

from stochastic.processes.diffusion import DiffusionProcess
from stochastic.processes.diffusion import ConstantElasticityVarianceProcess
from stochastic.processes.diffusion import CoxIngersollRossProcess
from stochastic.processes.diffusion import ExtendedVasicekProcess
from stochastic.processes.diffusion import OrnsteinUhlenbeckProcess
from stochastic.processes.diffusion import VasicekProcess

#######  Realizaciones Ruidos

global t
t=1
global n
n=1000

sbn100=[]
tbn100=[]
for i in range(10):
    bn=BlueNoise(t)
    sbn=bn.sample(n)
    tbn=bn.times(n)
    sbn100.append(sbn)
    tbn100.append(tbn)
    np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/blue_noise_"+ str(i) +".csv", np.c_[sbn, tbn], delimiter=",")

br=BrownianNoise(t)
sbr=br.sample(n)
tbr=br.times(n)

rn=RedNoise(t)
srn=rn.sample(n)
trn=rn.times(n)

pn=PinkNoise(t)
spn=pn.sample(n)
tpn=pn.times(n)

vn=VioletNoise(t)
svn=vn.sample(n)
tvn=vn.times(n)

wn=WhiteNoise(t)
swn=wn.sample(n)
twn=wn.times(n)

gn=GaussianNoise(t)
sgn=gn.sample(n)
tgn=gn.times(n)
tgn=np.delete(tgn,np.s_[:1])

fgn=FractionalGaussianNoise(hurst=0.75,t=10000)
sfgn=fgn.sample(n)
tfgn=fgn.times(n)
tfgn=np.delete(tfgn,np.s_[:1])

####### Multi Fractional Gaussian Noise de la librería fbm

# Example Hurst function with respect to time.
def h(t):
    return 0.75 - 0.5 * t

m = MBM(n=1024, hurst=h, length=1, method='riemannliouville')


# Generate a mGn realizations
smgn = m.mgn()

# Get the times associated with the mBm
tmgn = m.times()
tmgn=np.delete(tmgn,np.s_[:1])

############ Espectros Ruidos


BN = thinkdsp.Wave(sbn,tbn)
BNspectrum = BN.make_spectrum()
#BN.write(filename='BlueNoise.wav')

BR = thinkdsp.Wave(sbr,tbr)
BRspectrum = BR.make_spectrum()
#BR.write(filename='BrownianNoise.wav')

RN = thinkdsp.Wave(srn,trn)
RNspectrum = RN.make_spectrum()
#RN.write(filename='RedNoise.wav')

PN = thinkdsp.Wave(spn,tpn)
PNspectrum = PN.make_spectrum()
#PN.write(filename='PinkNoise.wav')

VN = thinkdsp.Wave(svn,tvn)
VNspectrum = VN.make_spectrum()
#VN.write(filename='VioletNoise.wav')

WN = thinkdsp.Wave(swn,twn)
WNspectrum = WN.make_spectrum()
#WN.write(filename='WhiteNoise.wav')

GN = thinkdsp.Wave(sgn,tgn)
GNspectrum = GN.make_spectrum()
#GN.write(filename='GaussianNoise.wav')

FGN = thinkdsp.Wave(sfgn,tfgn)
FGNspectrum = FGN.make_spectrum()
#FGN.write(filename='FractionalGaussianNoise.wav')

MGN = thinkdsp.Wave(smgn,tmgn)
MGNspectrum = MGN.make_spectrum()
#MGN.write(filename='MultiFractionalGaussianNoise.wav')



####### Plot Señal Ruidos

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9) = plt.subplots(9)
fig.suptitle('RUIDOS')
ax1.plot(BN.ts,BN.ys)
ax1.set_title('Blue Noise')
ax2.plot(BR.ts,BR.ys)
ax2.set_title('Brownian Noise')
ax3.plot(RN.ts,RN.ys)
ax3.set_title('Red Noise')
ax4.plot(PN.ts,PN.ys)
ax4.set_title('Pink Noise')
ax5.plot(VN.ts,VN.ys)
ax5.set_title('Violet Noise')
ax6.plot(WN.ts,WN.ys)
ax6.set_title('White Noise')
ax7.plot(tgn,sgn)
ax7.set_title('Gaussian Noise')
ax8.plot(tfgn,sfgn)
ax8.set_title('Fractional Gaussian Noise')
ax9.plot(tmgn,smgn)
ax9.set_title('Multi Fractional Gaussian Noise')

####### CSV Señal Ruidos

np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/blue_noise.csv", np.c_[BN.ys, BN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/brownian_noise.csv", np.c_[BR.ys, BR.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/red_noise.csv", np.c_[RN.ys, RN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/pink_noise.csv", np.c_[PN.ys, PN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/violet_noise.csv", np.c_[VN.ys, VN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/white_noise.csv", np.c_[WN.ys, WN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/gaussian_noise.csv", np.c_[sgn, tgn], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/fractional_gaussian_noise.csv", np.c_[sfgn, tfgn], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales 2/ruidosx100/multi_fractional_gaussian_noise.csv", np.c_[smgn, tmgn], delimiter=",")


plt.show()
