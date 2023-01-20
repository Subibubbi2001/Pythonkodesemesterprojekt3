import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

import wfdb

# Read the two ECG signals (raw, filtered) and read
# the related information.
# Samplet fra 0 til 3000
signals, info = wfdb.rdsamp('rec_1', channels=[0, 1],
                              sampfrom=0, sampto=3000)


ecg0 = signals[:,0]
ecg1 = signals[:,1]


#Fs (sampling frekvensen) er givet ved 360 i artiklen
# Ts (samplingsperioden)
Fs=360
Ts=1/Fs


# Defineret t
t=np.arange(0,3000*Ts,Ts)

ecg0 = signals[:,0]
ecg1 = signals[:,1]



#Designet af basislinie-drift FIR-filter støj

#L er numtaps er længden af et filter som giver en flot graf
L=203

#Fc er cutt-off frekvensen som er angivet i artiklen
Fc=0.667

#designet filter
FiltHPF = signal.firwin(numtaps=L, cutoff=0.667, fs=1/Ts, pass_zero=False)




#EKG signal hvor basislinie-drift er filtreret i tidsdomænet
FiltUBF=signal.filtfilt(FiltHPF,1,ecg0)
plt.title(" EKG filtret for basislinie-drift")
plt.xlabel("tidsdomænet")
plt.ylabel("milivolts")
plt.plot(t,FiltUBF)
plt.show()

#EKG signal hvor basislinie-drift er filtreret i frekvensdomænet
plt.magnitude_spectrum(FiltUBF,Fs)
plt.title("Uden basislinie-drift")
plt.xlabel("frekvensdomænet")
plt.show()