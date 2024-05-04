import numpy as np

distance = float(input("Ingrese distancia entre las antenas (Km)  "))
frequency = float(input("Ingrese la frecuencia de la señal a transmitir (GHz)  ") )

# r = primer zona de frenel 

c = 17.32 
r = c * np.sqrt(distance / (4 * frequency))


rRound = round(r,3)
print (rRound)

# Es necesario tener r al menos como espacio despejado para
# asi disminuir el ruido en la señal o perdida de la misma 

print("Distancia para la primer zona de Fresnel es: ", rRound, "Metros")

