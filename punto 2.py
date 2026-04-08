# Función que devuelve estudiantes aprobados
def estudiantes_aprobados(lista_estudiantes):
    aprobados = []  # lista vacía donde guardaremos los que pasan
    
    for nombre, nota in lista_estudiantes:
        if nota >= 3.0:
            aprobados.append((nombre, nota))
    
    return aprobados

# Lista de tuplas (nombre, nota)
estudiantes = [
    ("Juan", 3.5),
    ("Ana", 2.8),
    ("Luis", 4.0),
    ("Sofia", 2.5),
    ("Carlos", 3.0)
]

# Llamar la función
resultado = estudiantes_aprobados(estudiantes)

# Mostrar resultados
print("Estudiantes aprobados:")
for nombre, nota in resultado:
    print(nombre, "-", nota)