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
Fs=300
Ts=1/Fs


t=np.arange(0,3000*Ts,Ts)

ecg0 = signals[:,0]
ecg1 = signals[:,1]


#Man fjerner basislinie-drift støjen

#L er numtaps er længden af et filter som giver en flot graf
L=203

#Fc er cutt-off frekvensen som er angivet i artiklen
Fc=0.667

#designet filter
FiltHPF = signal.firwin(numtaps=L, cutoff=0.667, fs=1/Ts, pass_zero=False)

FiltUBF=signal.filtfilt(FiltHPF,1,ecg0)
plt.title("EKG filtret for basislinie-drift")
plt.xlabel("tids")
plt.ylabel("milivolts")
plt.plot(t,FiltUBF)
plt.show()

#Man fjerner nu netstøjen fra det samme ekg-signal som man fjerne basislinie-drift med

fb=50
s1=50/120
Fs=500

#Filtreret som fjerner netstøjen i tidsdomænet
y0,x0=signal.iirnotch(fb,s1,Fs)
freq, h = signal.freqz(y0, x0, fs=Fs)

FiltUBPS=signal.filtfilt(y0,x0,FiltUBF)
plt.title("EKG uden baselinie + net støj")
plt.plot(FiltUBPS)
plt.show()


#Man fjerner nu muskel støjen fra det samme ekg-signal som man fjerner basislinie-drift + netstøjen med
M=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]

FiltUBPES=signal.filtfilt(M,1,FiltUBPS)
plt.plot(FiltUBPES)
plt.ylim([-0.1, 0.4])
plt.title("EKG uden støjtyperne")
plt.xlabel("tid(s)")
plt.ylabel("amplitude")
plt.show()


#Plottet af et spektrum uden basislinie-drift i frekvensdomænet

plt.magnitude_spectrum(FiltUBF,Fs,color="blue")
plt.title("EKG uden baselinie støj")
plt.show()


#Plottet af spektrum uden basislinie-drift og netstøj i frekvensdomænet
plt.magnitude_spectrum(FiltUBPS,Fs, color="red")
plt.title("EKG uden baselinie og net støj")
plt.show()


#Plottet af spektrummet uden de tre former for støjtyper
plt.magnitude_spectrum(FiltUBPES,Fs, color="purple")
plt.title("EKG uden støjtyperne")
plt.show()