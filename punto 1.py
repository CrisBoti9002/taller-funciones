# Función para calcular el promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Función para encontrar la nota más alta
def nota_mas_alta(notas):
    return max(notas)

# Función para encontrar la nota más baja
def nota_mas_baja(notas):
    return min(notas)


# Lista de notas (puedes cambiarla)
notas = [3.5, 4.2, 2.8, 4.8, 3.9]

# Llamar funciones
promedio = calcular_promedio(notas)
alta = nota_mas_alta(notas)
baja = nota_mas_baja(notas)

# Mostrar resultados
print("Promedio:", promedio)
print("Nota más alta:", alta)
print("Nota más baja:", baja)