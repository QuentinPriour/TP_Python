from ast import While
from math import *
from xml.etree.ElementTree import PI

x = False

While x == False :
    interY1 = FONCTION1(10)
    interY2 = Fonction2(10)
    if interY1*interY2 < 0.0 :
        x = True
    else:   
        print ("error , interval doens't work \n")


def FONCTION1 (x):
    resultat = pow(x,3) - exp(x,2) - exp(x,1) - 35

def Fonction2 (x):
   resultat1 = (exp(10*x) - 1 / exp(10*x) + 1 ) - 0,5

def Fonction3 (x):
    resulat3 = cos(x+3*PI/8)



