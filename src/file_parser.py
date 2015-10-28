#
# Projekt: LPC dekoder do predmetu ZRE 2015
# Autori: Jan Bednarik, Vaclav Stransky, Jana Vyroubalova
#

import numpy as np
from numpy.core.numeric import arange

# vyparsuje knihu LPC koeficientu ze 
# souboru a vrati je v matici
def getLPCBook(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()

    retMat = [[0 for x in range(512)] for x in range(10)]
    for x in range(0, 10):
        retMat[x] = lines[x].split()

    f.close()
    return np.array(retMat).astype(np.float)

# vyparsuje knihu gain hodnot ze
# souboru a vrati je v matici
def getGainBook(fileName):
    f = open(fileName, 'r')
    line = f.readline()
    retLine = line.split()
    f.close()
    return np.array(retLine).astype(np.float)

# vyparsuje data ze zakodovane nahravky
# a vrati je postupne v poradi
# A=LPC koeficienty, G=gainy, L=lagy
def getCod(fileName):
    f = open(fileName, 'r')
    A = []
    G = []
    L = []
    lines = f.readlines()
    for line in lines:
        elements = line.split()
        A.append(int(elements[0]))
        G.append(int(elements[1]))
        L.append(int(elements[2]))
    f.close()
    return A, G, L;

# vrati serazeny vektor hodnot gainu
# dle zakodovane nahravky
# gainBook = kodova kniha
# G = serazene indexy gainu
def getGainVector(gainBook,G):
    retG = []
    for idx in G:
        retG.append(gainBook[idx - 1])
    return retG
    
# vrati matici LPC koeficientu serazenych
# dle zakodovane nahravky
# lpcBook = kodova kniha
# lpcCoeff = indexy koeficientu
def getLPCmatrix(lpcBook, lpcCoeff):
    # preallocate the matrix
    A = np.zeros((10, len(lpcCoeff)))
    for i in range(len(lpcCoeff)):
        A[:, i] = lpcBook[:, lpcCoeff[i] - 1]
    return A


# pro testovani
if __name__ == "__main__":
    # test 1 - getLPCmatrix
    lpcBook = np.arange(50).reshape(10, 5)
    lpcCoeff = [0,2,4,1,3,0,0,0]
    A = getLPCmatrix(lpcBook, lpcCoeff)
    
