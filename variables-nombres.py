print("Hello World.")

# Crea la variable coches y le da un valor de 100
coches = 100
# Crea la variable espacios_en_un_coche y le da un valor de 4.0
espacios_en_un_coche = 4.0
conductores = 30
pasajeros = 90
# Crea la variable coches_no_conducidos, y le da el valor de coches - conductores,
# que ya hemos definido previamente
coches_no_conducidos = coches - conductores
coches_conducidos = conductores
capacidad_carpool = coches_conducidos * espacios_en_un_coche
media_pasajeros_por_coche = pasajeros / coches_conducidos

print("Hay", coches, "coches disponibles.")
print("Hay solo", conductores, "conductores disponibles.")
print("Hoy habrá", coches_no_conducidos, "coches vacios.")
print("Hoy podemos transportar", capacidad_carpool, "personas.")
print("Hoy tenemos", pasajeros, "pasajeros.")
print("Necesitamos", media_pasajeros_por_coche, "en cada coche.")
