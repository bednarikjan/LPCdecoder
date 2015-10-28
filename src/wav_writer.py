#
# Projekt: LPC dekoder do predmetu ZRE 2015
# Autori: Jan Bednarik, Vaclav Stransky, Jana Vyroubalova
#

import wave
import struct

def writeWav(fileName, samples):
    #print("zapisuju wavko")
    
    wavFile = wave.open(fileName, 'w')
    samplesLenght = len(samples);
    wavFile.setparams((1, 2, 8000, 0, 'NONE', 'not compressed'))

    for i in range(0, samplesLenght):
        sample = min(int(samples[i]*32767), 32767)
        sample = max(sample, -32767)
        packedValue = struct.pack('h', sample)
        wavFile.writeframes(packedValue)

    wavFile.close()

