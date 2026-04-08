# Función para encontrar la temperatura más alta
def temperatura_maxima(temperaturas):
    return max(temperaturas)


# Función para encontrar la temperatura más baja
def temperatura_minima(temperaturas):
    return min(temperaturas)


# Diccionario: ciudad → lista de temperaturas
ciudades = {
    "Bogota": [18, 20, 17, 19, 21, 16, 18],
    "Medellin": [25, 27, 26, 28, 29, 27, 26],
    "Cali": [30, 32, 31, 33, 34, 32, 31]
}

# Recorrer ciudades
for ciudad, temperaturas in ciudades.items():
    print("\nCiudad:", ciudad)
    print("Temperatura más alta:", temperatura_maxima(temperaturas))
    print("Temperatura más baja:", temperatura_minima(temperaturas)) 