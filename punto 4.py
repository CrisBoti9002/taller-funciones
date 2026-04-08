# Función para agregar producto al inventario
def agregar_producto(inventario, nombre, precio, cantidad):
    inventario.append((nombre, precio, cantidad))


# Función para mostrar inventario
def mostrar_inventario(inventario):
    print("\n--- Inventario ---")
    for nombre, precio, cantidad in inventario:
        print(nombre, "- Precio:", precio, "- Cantidad:", cantidad)


# Función para calcular el valor total
def calcular_valor_total(inventario):
    total = 0
    for nombre, precio, cantidad in inventario:
        total += precio * cantidad
    return total


# Lista del inventario (tuplas)
inventario = []

# Agregar productos
agregar_producto(inventario, "Arroz", 3000, 10)
agregar_producto(inventario, "Leche", 2500, 5)
agregar_producto(inventario, "Pan", 1500, 20)

# Mostrar inventario
mostrar_inventario(inventario)

# Calcular total
total = calcular_valor_total(inventario)
print("Valor total del inventario:", total)