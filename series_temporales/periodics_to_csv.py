from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 1000, endpoint=False)

square2pi = signal.square(2 * np.pi * 1 * t)
#square3pi = signal.square(np.pi * 3 * t)
square4pi = signal.square(2 * np.pi * 2 * t)
square8pi = signal.square(2 * np.pi * 4 * t)
#square20pi = signal.square(5 * np.pi * 4 * t)


#plt.plot(t, square2pi)
#plt.plot(t, square4pi)

# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/square_2pi.csv", np.c_[square2pi, t], delimiter=",")
#np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/square_3pi.csv", np.c_[square3pi, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/square_4pi.csv", np.c_[square4pi, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/square_8pi.csv", np.c_[square8pi, t], delimiter=",")
#np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/square_20pi.csv", np.c_[square20pi, t], delimiter=",")
#
sawtooth2pi = signal.sawtooth(2 * np.pi * 1 * t)
sawtooth4pi = signal.sawtooth(2 * np.pi * 2 * t)
sawtooth8pi = signal.sawtooth(2 * np.pi * 4 * t)

#
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sawtooth_2pi.csv", np.c_[sawtooth2pi, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sawtooth_4pi.csv", np.c_[sawtooth4pi, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sawtooth_8pi.csv", np.c_[sawtooth8pi, t], delimiter=",")

#plt.plot(t, sawtooth2pi)
#plt.plot(t, sawtooth20pi)

#np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sawtooth2pi_2pi.csv", np.c_[sawtooth2pi, t], delimiter=",")
#np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sawtooth20pi.csv", np.c_[sawtooth20pi, t], delimiter=",")

i, q, e = signal.gausspulse(t, fc=2, retquad=True, retenv=True)

#plt.plot(t, i,'-', t, q, '--', t, e, '+')

# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/gausian1i.csv", np.c_[i, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/gausian1q.csv", np.c_[q, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/gausian1e.csv", np.c_[e, t], delimiter=",")

#ambiente cte
#a = np.empty(1000)
#a.fill(5,dtype=int)

# a = np.full(1000, 0.5)
# print(a)
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/0punt05.csv", np.c_[a, t], delimiter=",")


a=np.full(1000, 0, dtype='float64')
b=np.full(1000, 0.1, dtype='float64')
c=np.full(1000, 0.2, dtype='float64')
d=np.full(1000, 0.3, dtype='float64')
e=np.full(1000, 0.4, dtype='float64')
f=np.full(1000, 0.5, dtype='float64')
g=np.full(1000, 0.6, dtype='float64')
h=np.full(1000, 0.7, dtype='float64')
i=np.full(1000, 0.8, dtype='float64')
j=np.full(1000, 0.9, dtype='float64')
k=np.full(1000, 1, dtype='float64')

aa=np.full(1000, 0.05, dtype='float64')
bb=np.full(1000, 0.15, dtype='float64')
cc=np.full(1000, 0.25, dtype='float64')
dd=np.full(1000, 0.35, dtype='float64')
ee=np.full(1000, 0.45, dtype='float64')
ff=np.full(1000, 0.55, dtype='float64')
gg=np.full(1000, 0.65, dtype='float64')
hh=np.full(1000, 0.75, dtype='float64')
ii=np.full(1000, 0.85, dtype='float64')
jj=np.full(1000, 0.95, dtype='float64')

aaa=np.full(1000, 0.075, dtype='float64')
bbb=np.full(1000, 0.085, dtype='float64')
ccc=np.full(1000, 0.065, dtype='float64')

#plt.plot(t, a, t, f, t, k)


# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/00.csv", np.c_[a, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/01.csv", np.c_[b, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/02.csv", np.c_[c, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/03.csv", np.c_[d, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/04.csv", np.c_[e, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/05.csv", np.c_[f, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/06.csv", np.c_[g, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/07.csv", np.c_[h, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/08.csv", np.c_[i, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/09.csv", np.c_[j, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/10.csv", np.c_[k, t], delimiter=",")
#
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/005.csv", np.c_[aa, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/015.csv", np.c_[bb, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/025.csv", np.c_[cc, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/035.csv", np.c_[dd, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/045.csv", np.c_[ee, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/055.csv", np.c_[ff, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/065.csv", np.c_[gg, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/075.csv", np.c_[hh, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/085.csv", np.c_[ii, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/095.csv", np.c_[jj, t], delimiter=",")
#
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/0085.csv", np.c_[bbb, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/0075.csv", np.c_[aaa, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/0065.csv", np.c_[ccc, t], delimiter=",")


#plt.plot(t, sine)
sine2 = np.sin(2 * np.pi * t)
sine4 = np.sin(4 * np.pi * t)
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sinewave2.csv", np.c_[sine2, t], delimiter=",")
# np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sinewave4.csv", np.c_[sine4, t], delimiter=",")

#plt.ylim(-2, 2)
#


w = signal.chirp(t, f0=10, f1=1, t1=1, method='linear')
plt.plot(t, w)
plt.title("Linear Chirp, f(0)=6, f(10)=1")
plt.xlabel('t (sec)')
plt.show()
np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/chirp.csv", np.c_[w, t], delimiter=",")

plt.show()
