# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:14:55 2021

@author: Tonajul
"""
#RANDOM VARIABLE: Determinar qué edades tienen las mujeres que no estaban embarazadas, que fueron hospitalizadas y que fueran menores a 40
#Tipo de persona = 1 si es ambulatorio y fue a casa o 2 si quedo hospitalizado
# 1 = si, 2 = no
#1 = femenino, 2 = masculino
#sacaremos edad de las personas que son de tipo 1 y sexo 1 con embarazo 1//Tipo Persona, Sexo, Edad, Embarazo
#contaremos cuantas son las personas menores de 40 años que son ambulatorias, sexo femenino y con embarazo 
#EDAD<=40, TIPO:2, SEXO:1, EMBARAZO:1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli 
import seaborn as sb


datos = pd.read_csv('ObesidadCovid.csv',header=0)


def lc(a, c, m, seed):
    return ((a * seed) + c) % m

def generatorTest(a, c, m, seed, n):
    r = []
    xi = [0, seed]
    for i in range(1, n + 1):
        xi.append(lc(a, c, m, xi[i]))
        r.append(xi[i] / (m - 1));
        
    print("ri generados: ")
    print(applyDistribution(r))
    return r 

 
def randomVariable(df):
    #Diferencia la cantidad de mujeres menores con obesidad que fueron ambulatorias sin hospitalizacion y con obesidad con las que no, las obesas = 2, las no obesas = 1
    df['MENORES_OBESOS'] = np.where((df['EDAD']<=40) & (df['TIPO_PACIENTE']==1) & (df['SEXO']==1) & (df['OBESIDAD']==2)    ,1,2)
    #Cuenta la cantidad de mujeres obesas
    obesos = df['MENORES_OBESOS'].apply(str).str.contains('2').value_counts()[True]
    #Histograma de mujeres ambulatorias con obesidad, 1 = no obesas, 2 = obesas
    histogram = df['MENORES_OBESOS'].hist(bins=int(np.sqrt(df.shape[0])))#Shape es la cantidad de filas que hay, entonces el grafico se acomoda a esa cantidad
    plt.xlabel("Girls With No Obesity/ Girls With Obesity")
    plt.ylabel("Quantity")
    plt.show()
    mean = df['MENORES_OBESOS'].mean()
    desviation = df['MENORES_OBESOS'].std(ddof=0)
    variance = df['MENORES_OBESOS'].var(ddof=0)
   # print(obesos)
    print(df)
    return mean,desviation,variance

def applyDistribution(r): #Distribucion discreta porque tiene una cantidad de datos finita y contable
    mean = df['MENORES_OBESOS'].mean()
    p = mean
    print("Funcion de Bernoulli")
    data_bern = bernoulli.rvs(r,p) 
    ax = sb.distplot(data_bern,
                     kde = True,
                     color='crimson',
                     hist_kws={"linewidth":25, 'alpha':1})
    ax.set(xlabel='Bernoulli',ylabel='Frequency')



 


df = pd.DataFrame(datos)
print(randomVariable(df))
print(generatorTest(16807, 0, 2147483647, 1, 1000)) 

df.to_csv('ObesidadCovid.csv',header=True,index=False)




