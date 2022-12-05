from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 1000, endpoint=False)

#square2pi = signal.square(2 * np.pi * 1 * t)
#square4pi = signal.square(2 * np.pi * 2 * t)

#plt.plot(t, square2pi)
#plt.plot(t, square4pi)

#np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/square_2pi.csv", np.c_[square2pi, t], delimiter=",")
#np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/square_4pi.csv", np.c_[square4pi, t], delimiter=",")

sawtooth2pi = signal.sawtooth(2 * np.pi * 1 * t)
sawtooth20pi = signal.sawtooth(2 * np.pi * 10 * t)

plt.plot(t, sawtooth2pi)
plt.plot(t, sawtooth20pi)

np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sawtooth2pi_2pi.csv", np.c_[sawtooth2pi, t], delimiter=",")
np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sawtooth20pi.csv", np.c_[sawtooth20pi, t], delimiter=",")

#i, q, e = signal.gausspulse(t, fc=5, retquad=True, retenv=True)#
#plt.plot(t, i,'--', t, q, '--', t, e, '--')



#plt.plot(t, sine)
#sine = np.sin(2 * np.pi * t)
##np.savetxt("//Users/carlestapi/Desktop/series temporales test/m-files/series_temporales/periodics/sinewave1.csv", np.c_[sine, t], delimiter=",")

plt.ylim(-2, 2)
plt.show()
