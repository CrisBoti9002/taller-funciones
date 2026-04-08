# Función para convertir nota a letra
def convertir_nota(nota):
    rangos = [
        (4.5, 5.0, "A"),
        (4.0, 4.4, "B"),
        (3.0, 3.9, "C"),
        (2.0, 2.9, "D"),
        (0.0, 1.9, "F")
    ]

    for minimo, maximo, letra in rangos:
        if minimo <= nota <= maximo:
            return letra


# Función para generar reporte
def generar_reporte(estudiantes):
    for nombre, nota in estudiantes:
        letra = convertir_nota(nota)
        print(nombre, "- Nota:", nota, "- Letra:", letra)


# Lista de estudiantes (nombre, nota)
estudiantes = [
    ("Juan", 4.7),
    ("Ana", 3.8),
    ("Luis", 2.5),
    ("Sofia", 1.9),
    ("Carlos", 4.2)
]

# Mostrar reporte
generar_reporte(estudiantes)