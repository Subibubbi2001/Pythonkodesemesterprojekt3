
import matplotlib.pyplot as plt
import numpy as np
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

# Defineret T
t=np.arange(0,3000*Ts,Ts)

ecg0 = signals[:,0]
ecg1 = signals[:,1]

#Rå EKG data med støj (ecg0) i tidsdomænet
plt.title('Rå signal med støj')
plt.xlabel('tid(s)')
plt.ylabel('milivolts')
plt.plot(t,ecg0)
plt.show()

#Rå EKG data med støj (ecg1) i tidsdomænet
plt.title('Filtrede signal uden støj')
plt.xlabel('tid(s)')
plt.ylabel('milivolts')
plt.plot(t,ecg1)
plt.show()