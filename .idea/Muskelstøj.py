import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

import wfdb

# Read the two ECG signals (raw, filtered) and read
# the related information.
# Samplet fra 0 til 3000
signals, info = wfdb.rdsamp('rec_1', channels=[0, 1],
                              sampfrom=0, sampto=3000)


#Fs (sampling frekvensen) har vi givet ved 300
# Ts (samplingsperioden)
Fs= 300
Ts=1/Fs


# Defineret T ud fra sampleperioden
t=np.arange(0,3000*Ts,Ts)

ecg0 = signals[:,0]
ecg1 = signals[:,1]


#Indsat et n-point moving average med er array på 8 som givet i artiklen
MA=np.array([1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8])



#EKG signal hvor muskelstøjen er filtreret i tidsdomænet
FiltSUB=signal.filtfilt(MA,1,ecg0)
plt.plot(FiltSUB)
plt.title("EKG uden muskel støj")
plt.xlabel("tid(s)")
plt.ylabel("amplitude")
plt.show()



#EKG signal hvor muskelstøjen er filtreret i frekvensdomænet
plt.magnitude_spectrum(FiltSUB,Fs)
plt.title("EKG uden muskel støj")
plt.show()