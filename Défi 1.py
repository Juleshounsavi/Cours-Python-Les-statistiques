
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

data=np.arange(1,31,1)

#Fonction de calcul de la moyenne
def CalculMoyenne(dt):
    moy = sum(dt)/len(dt)
    return moy
m=CalculMoyenne(data)

#Fonction de calcul de la variance
def CalculVariance(dt):
    sc=0
    for i in data:
        sc=sc+i**2
    vr=(sc/len(dt)) - (CalculMoyenne(dt))**2   
    return vr
v=CalculVariance(data)

#Fonction de calcul de l'ecart-type
def CalculEcartType(dt):
    ect = math.sqrt(CalculVariance(dt))
    return ect
ec=CalculEcartType(data)

print("Moyenne: {}\nVariance: {}\nEcart-type: {}".format(m,v,ec))
