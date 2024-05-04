import numpy as np
import math as ma

distance = float(input("Ingrese distancia entre las antenas (Km)  "))
frequency = float(input("Ingrese la frecuencia de la señal a transmitir (GHz)  ") )

a = 20 * ma.log(frequency,10)
b = 20 * ma.log(distance,10)

LdB = 92.44 +  a + b
LdBround = np.round(LdB,3)

print("La perdida en el espacio libre es de: ", LdB, "dB")


