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

bn=BlueNoise(t)
sbn=bn.sample(n)
tbn=bn.times(n)

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


#######  Realizaciones Continuous

bp = BesselProcess(t)
sbp=bp.sample(n)
tbp=bp.times(n)

bb = BrownianBridge(t)
sbb=bb.sample(n)
tbb=bb.times(n)

be = BrownianExcursion(t)
sbe=be.sample(n)
tbe=be.times(n)

bm = BrownianMeander(t)
sbm=bm.sample(n)
tbm=bm.times(n)

bmotion = BrownianMotion(t)
sbmotion=bmotion.sample(n)
tbmotion=bmotion.times(n)

cp = CauchyProcess(t)
scp=cp.sample(n)
tcp=cp.times(n)

fbm = FractionalBrownianMotion(hurst=0.7)
sfbm=fbm.sample(n)
tfbm=fbm.times(n)

gp = GammaProcess(mean=1,variance=1)
sgp=gp.sample(n)
tgp=gp.times(n)

gbmotion = GeometricBrownianMotion(drift=0,volatility=1)
sgbmotion=gbmotion.sample(n)
tgbmotion=gbmotion.times(n)

igp = InverseGaussianProcess(mean=None, scale=1, t=1, rng=None)
sigp=igp.sample(n)
tigp=igp.times(n)

# mpp=MixedPoissonProcess(rate_func=None)
# smpp=mpp.sample(n)
# tmpp=mpp.times(n)

mfbmotion= MultifractionalBrownianMotion(hurst=h)
smfbmotion=mfbmotion.sample(n)
tmfbmotion=mfbmotion.times(n)

pp= PoissonProcess(rate=1)
spp=pp.sample(n)
#tpp=pp.times(n)

squaredbp= SquaredBesselProcess(t)
ssquaredbp=squaredbp.sample(n)
tsquarebp=squaredbp.times(n)

vgp= VarianceGammaProcess(t)
svgp=vgp.sample(n)
tvgp=vgp.times(n)

wp= WienerProcess(t)
swp=wp.sample(n)
twp=wp.times(n)

#######  Realizaciones Processos Difusión

dp = DiffusionProcess(t)
sdp=dp.sample(n)
tdp=dp.times(n)

cevp = ConstantElasticityVarianceProcess(t)
scevp=cevp.sample(n)
tcevp=cevp.times(n)

cirp = CoxIngersollRossProcess(t)
scirp=cirp.sample(n)
tcirp=cirp.times(n)

evp = ExtendedVasicekProcess(t)
sevp=evp.sample(n)
tevp=evp.times(n)

oup = OrnsteinUhlenbeckProcess(t)
soup=oup.sample(n)
toup=oup.times(n)

vp = VasicekProcess(t)
svp=vp.sample(n)
tvp=vp.times(n)


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



# plt.plot(BN.ts,BN.ys)
# plt.legend(['Blue Noise'])
# plt.draw()

# plt.plot(BR.ts,BR.ys)
# plt.legend(['Brownian Noise'])
# plt.draw()

# plt.plot(RN.ts,RN.ys)
# plt.legend(['Red Noise'])
# plt.draw()

# plt.plot(PN.ts,PN.ys)
# plt.legend(['Pink Noise'])
# plt.draw()

# plt.plot(VN.ts,VN.ys)
# plt.legend(['Violet Noise'])
# plt.draw()

# plt.plot(WN.ts,WN.ys)
# plt.legend(['White Noise'])
# plt.draw()

# plt.plot(tgn,sgn)
# plt.legend(['Gaussian Noise'])
# plt.draw()

# plt.plot(tfgn,sfgn)
# plt.legend(['Fractional Gaussian Noise'])
# plt.draw()

# plt.plot(tmgn,smgn)
# plt.legend(['Multi Fractional Gaussian Noise'])
# plt.draw()
# plt.show()


############ Espectros Continuous

#BP = thinkdsp.Wave(sbp,tbp)
#BPspectrum = BP.make_spectrum()
#BN.write(filename='BesselProcess.wav')


# ...etc

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

np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/blue_noise.csv", np.c_[BN.ys, BN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/brownian_noise.csv", np.c_[BR.ys, BR.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/red_noise.csv", np.c_[RN.ys, RN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/pink_noise.csv", np.c_[PN.ys, PN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/violet_noise.csv", np.c_[VN.ys, VN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/white_noise.csv", np.c_[WN.ys, WN.ts], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/gaussian_noise.csv", np.c_[sgn, tgn], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/fractional_gaussian_noise.csv", np.c_[sfgn, tfgn], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/ruidos/multi_fractional_gaussian_noise.csv", np.c_[smgn, tmgn], delimiter=",")

####### Plot Señal Continuous

fig, axs = plt.subplots(8,2)
fig.suptitle('CONTINUOUS')
axs[0,0].plot(tbp,sbp)
axs[0,0].set_title('Bessel Process')
axs[1,0].plot(tbb,sbb)
axs[1,0].set_title('Brownian Bridge')
axs[2,0].plot(tbe,sbe)
axs[2,0].set_title('Brownian Excursion')
axs[3,0].plot(tbm,sbm)
axs[3,0].set_title('Brownian Meander')
axs[4,0].plot(tbm,sbmotion)
axs[4,0].set_title('Brownian Motion')
axs[5,0].plot(tcp,scp)
axs[5,0].set_title('Cauchy Process')
axs[6,0].plot(tfbm,sfbm)
axs[6,0].set_title('Fract. Brownian Mot. h=0.5')
axs[7,0].plot(tgp,sgp)
axs[7,0].set_title('Gamma Process')
axs[0,1].plot(tbm,sgbmotion)
axs[0,1].set_title('Geometric Brownian Motion')
axs[1,1].plot(tigp,sigp)
axs[1,1].set_title('Inverse Gaussian Process')
# axs[2,1].plot(tmpp,smpp)
axs[2,1].set_title('Mixed Poisson Process')
axs[3,1].plot(tmfbmotion,smfbmotion)
axs[3,1].set_title('Multi Fractional Brownian Motion')
axs[4,1].plot(tbm,spp)
axs[4,1].set_title('Poisson Process')
axs[5,1].plot(tsquarebp,ssquaredbp)
axs[5,1].set_title('Squared Bessel Process')
axs[6,1].plot(tvgp,svgp)
axs[6,1].set_title('Variance Gamma Process')
axs[7,1].plot(twp,swp)
axs[7,1].set_title('Wiener Process')

####### CSV Señal Continuous

np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/bessel_process.csv", np.c_[sbp, tbp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/brownian_bridge.csv", np.c_[sbb, tbb], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/brownian_excursion.csv", np.c_[sbe, tbe], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/brownian_meander.csv", np.c_[sbm, tbm], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/brownian_motion.csv", np.c_[sbmotion, tbm], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/cauchy_process.csv", np.c_[scp, tcp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/fractional_brownian_motion_h05.csv", np.c_[sfbm, tfbm], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/gamma_process.csv", np.c_[sgp, tgp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/geometric_brownian_motion.csv", np.c_[sgbmotion, tbm], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/inverse_gaussian_process.csv", np.c_[sigp, tigp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/multi_fractional_brownian_motion.csv", np.c_[smfbmotion, tmfbmotion], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/poisson_process.csv", np.c_[spp, tbm], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/squared_bessel_process.csv", np.c_[ssquaredbp, tsquarebp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/variance_gamma_process.csv", np.c_[svgp, tvgp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/continuos/wiener_process.csv", np.c_[swp, twp], delimiter=",")


####### Plot Señal Difussion

fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6)
fig.suptitle('DIFUSIÓN')
ax1.plot(tdp,sdp)
ax1.set_title('Diffusion Process (Generalized)')
ax2.plot(tcevp,scevp)
ax2.set_title('Constant Elasticity Variance Process')
ax3.plot(tcirp,scirp)
ax3.set_title('Cox Ingersoll Ross Process')
ax4.plot(tevp,sevp)
ax4.set_title('Extended Vasicek Process')
ax5.plot(toup,soup)
ax5.set_title('Ornstein Uhlenbeck Process')
ax6.plot(tvp,svp)
ax6.set_title('Vasicek Process')

####### CSV Señal Difusion

np.savetxt("/Users/carlestapi/Desktop/series_temporales/difusion/diffusion_process_generalized.csv", np.c_[sdp, tdp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/difusion/constant_elasticity_variance_process.csv", np.c_[scevp, tcevp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/difusion/cox_ingersoll_ross_process.csv", np.c_[scirp, tcirp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/difusion/extended_vasicek_process.csv", np.c_[sevp, tevp], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/difusion/ornstein_uhlenbeck_process.csv", np.c_[soup, toup], delimiter=",")
np.savetxt("/Users/carlestapi/Desktop/series_temporales/difusion/vasicek_process.csv", np.c_[svp, tvp], delimiter=",")

###### Slope Espectro

# slopeBN = BNspectrum.estimate_slope().slope
# slopeBR = BRspectrum.estimate_slope().slope
# slopeRN = RNspectrum.estimate_slope().slope
# slopePN = PNspectrum.estimate_slope().slope
# slopeVN = VNspectrum.estimate_slope().slope
# slopeWN = WNspectrum.estimate_slope().slope
# slopeGN = GNspectrum.estimate_slope().slope
# slopeFGN = FGNspectrum.estimate_slope().slope
# slopeMGN = MGNspectrum.estimate_slope().slope

# print('Slopes:')
# print('BN',slopeBN)
# print('RN',slopeRN)
# print('PN',slopePN)
# print('VN',slopeVN)
# print('WN',slopeWN)
# print('GN',slopeGN)
# print('FGN',slopeFGN)
# print('MGN',slopeMGN)

# ######## Plot Espectro

# BRspectrum.plot_power(linewidth=.75,label=('beta BR',slopeBR))
# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
# plt.show()

# BNspectrum.plot_power(linewidth=.75,label=('beta BN',slopeBN))
# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
# plt.show()

# RNspectrum.plot_power(linewidth=.75,label=('beta RN',slopeRN))
# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
# plt.show()

# PNspectrum.plot_power(linewidth=.75,label=('beta PN',slopePN))
# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
# plt.show()

# VNspectrum.plot_power(linewidth=.75,label=('beta VN',slopeVN))
# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
# plt.show()

# WNspectrum.plot_power(linewidth=.75,label=('beta WN',slopeWN))
# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
# plt.show()

# GNspectrum.plot_power(linewidth=.75,label=('beta GN',slopeGN))
# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
# plt.show()

# FGNspectrum.plot_power(linewidth=.75,label=('beta FGN',slopeFGN))
# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
# plt.show()

# MGNspectrum.plot_power(linewidth=.75,label=('beta MGN',slopeMGN))

# thinkplot.config(xlabel='Frequency (1/s)', ylabel='Power',
#                  xscale='log',yscale='log',low=0)
plt.show()
