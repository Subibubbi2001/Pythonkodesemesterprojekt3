import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

import wfdb

# Read the two ECG signals (raw, filtered) and read
# the related information.
# Samplet fra 0 til 3000
signals, info = wfdb.rdsamp('rec_1', channels=[0, 1],
                              sampfrom=0, sampto=3000)

#Fs (sampling frekvensen) har vi givet ved 500
# Ts (samplingsperioden)
Fs=500
Ts=1/Fs

# Defineret t
t=np.arange(0,3000*Ts,Ts)

ecg0 = signals[:,0]
ecg1 = signals[:,1]



#Designet af Basislinie-drift

#fa og fb står for fnotch givet i artiklen, som står henholdsvis for basislinie-drift og netstøj
fa=0.67
fb=50

#s kan også skrives som f0/5
s=0.67/5
Fs=500

#Filtreret som fjerner basislinie-drift støjen i tidsdomænet
y0,x0=signal.iirnotch(fa,s,Fs)
freq, h = signal.freqz(y0, x0, fs=Fs)

FiltUBSF=signal.filtfilt(y0,x0,ecg0)
plt.title("EKG uden basislinie støj")
plt.plot(FiltUBSF)
plt.show()



#Designet af netstøj
fa=50
s1=50/120
Fs=500


#Filtreret som fjerner netstøj i tidsdomænet
y1,x1=signal.iirnotch(fa,s1,Fs)
freq, h = signal.freqz(y1, x1, fs=Fs)

FiltUBPS=signal.filtfilt(y1,x1,FiltUBSF)
plt.title("EKG uden basislinie + netstøj")
plt.plot(FiltUBPS)
plt.show()



# Plottet det EKG uden basislinie-drift og uden basislinie-drift + netstøj  i frekvensdomænet

#Spectrum for EKG uden baseline wander støj
plt.magnitude_spectrum(FiltUBSF,Fs, color="blue")
plt.title("EKG uden basislinie drift støj")
plt.xlabel("frekvensdomænet")



plt.magnitude_spectrum(FiltUBPS,Fs, color="red")
plt.title("EKG uden basislinie + netstøj")
plt.xlabel("frekvensdomænet")
plt.show()

plt.magnitude_spectrum(FiltUBPS,Fs)