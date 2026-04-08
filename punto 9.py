# Función para agrupar productos por categoría
def agrupar_productos(lista_productos):
    categorias = {}

    for producto, categoria in lista_productos:
        if categoria in categorias:
            categorias[categoria].append(producto)
        else:
            categorias[categoria] = [producto]

    return categorias


# Lista de tuplas (producto, categoría)
productos = [
    ("Arroz", "Granos"),
    ("Lentejas", "Granos"),
    ("Leche", "Lacteos"),
    ("Queso", "Lacteos"),
    ("Manzana", "Frutas"),
    ("Banano", "Frutas")
]

# Llamar función
resultado = agrupar_productos(productos)

# Mostrar resultado
print(resultado)