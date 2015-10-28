#
# Projekt: LPC dekoder do predmetu ZRE 2015
# Autori: Jan Bednarik, Vaclav Stransky, Jana Vyroubalova
#

import random
import scipy
from scipy.signal  import butter, lfilter, tf2ss
import math

def synthesize(A, G, L, P, frameLength):    
    # Number of frames
    framesNumber = len(G)   
        
    # Peedalokace vystupniho signalu
    signal = [0 for i in range(framesNumber * frameLength)]

    init = [0] * P
        
    nextvoiced = 0; 
    
    # Indexy vzorku jednotlivych ramcu
    start = 0
    stop = start + frameLength - 1

    for i in range(framesNumber):
        a = [1]
        a.extend(A[:,i])            
        
        g = [G[i]]
        lag = L[i]
        
        # Neznele ramce - generovani sumu
        if lag == 0:            
            excit = [random.gauss(0, 1) for i in range(frameLength)]                        
        # Znele ramce - generovani impulsu s frekvenci lagu
        else:
            where = range(nextvoiced, frameLength, lag)
            nextvoiced = max(where) + lag - frameLength     
            excit = [0 for i in range(frameLength)]
            for i in where:
                excit[i] = 1.0                            
        
        # Normalizace
        weight = math.sqrt(sum([sample**2 for sample in excit]) / frameLength)
        excit = [sample / weight for sample in excit]    

        synt, final = scipy.signal.lfilter(g, a, excit, -1, init)    
        
        signal[start:stop] = synt
        
        init = final

        start = start + frameLength
        stop = start + frameLength - 1
    
    return signal
    

    
# pro testovani
if __name__ == "__main__":
    a = [ 1,
         -2.1262083e+00,
          3.0602877e+00,  
         -3.4821424e+00,  
          3.5360120e+00,  
         -3.1634716e+00,  
          2.7123022e+00,  
         -1.8573243e+00,  
          1.0552398e+00,  
         -4.8460154e-01,  
          1.5360509e-01]  

    g = [3.4869756e-05]

    init = [0] * 10

    excit = [random.gauss(0, 1) for i in range(160)]                        

    synt , final = scipy.signal.lfilter(g, a, excit, -1, init)

