# Función para agregar productos
def agregar_producto(carrito, nombre, precio):
    carrito.append((nombre, precio))


# Función para calcular total
def calcular_total(carrito):
    total = 0
    for nombre, precio in carrito:
        total += precio
    return total


# Función para aplicar descuento
def aplicar_descuento(total, descuento):
    return total - (total * descuento / 100)


# Función para mostrar carrito
def mostrar_carrito(carrito):
    print("\n--- Carrito ---")
    for nombre, precio in carrito:
        print(nombre, "-", precio)


# Carrito
carrito = []

# Agregar productos
agregar_producto(carrito, "Arroz", 3000)
agregar_producto(carrito, "Leche", 2500)
agregar_producto(carrito, "Pan", 1500)

# Mostrar carrito
mostrar_carrito(carrito)

# Calcular total
total = calcular_total(carrito)
print("Total sin descuento:", total)

# Aplicar descuento (ej: 10%)
total_final = aplicar_descuento(total, 10)
print("Total con descuento:", total_final)