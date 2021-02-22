import matplotlib.pyplot as plt
import pandas as pd
import pywt

# reading the dataset
train = pd.read_csv('dataQus.json')

print(train.head())

print(pywt.WaveletPacket(data=train, wavelet="db02"))
