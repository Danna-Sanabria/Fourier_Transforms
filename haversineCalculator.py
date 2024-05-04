from haversine import haversine, Unit

print(f"INGRESE EN LOS RANGOS [-90,90] (lat) y [-180,180] (lon)")

# Latitud, longitud punto de partida
latStartPoint = float(input("Ingrese latitud punto de partida:  "))
lonStartPoint = float(input("Ingrese longitud punto de partida:  ") )

# Latitud, longitud punto final / llegada
latEndPoint = float(input("Ingrese latitud punto final:  "))
lonEndPoint = float(input("Ingrese longitud punto final:  "))


#startingPoint = (5.555451 , 73.355153) # (latitud, longitud) #Usada para el proyecto
startingPoint = (latStartPoint , lonStartPoint) # (latitud, longitud)

endPoint = (latEndPoint, lonEndPoint)

# Haversine in kilometers
HaversineKm = haversine(startingPoint, endPoint)
roundDistance = round(HaversineKm,3)

print("La distancia encontrada es: ",roundDistance, "KM")

# Haversine in miles
Haversinemi = haversine(startingPoint,endPoint, unit=Unit.MILES)
print("La distancia encontrada es: ",Haversinemi, "mi")


