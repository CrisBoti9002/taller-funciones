# Función para contar frecuencia de palabras
def contar_palabras(lista_palabras):
    frecuencias = {}

    for palabra in lista_palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


# Lista de palabras
palabras = ["hola", "adios", "hola", "python", "hola", "adios"]

# Llamar función
resultado = contar_palabras(palabras)

# Mostrar resultado
print(resultado)