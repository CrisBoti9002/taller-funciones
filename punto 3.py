# Función para agregar contacto
def agregar_contacto(agenda, nombre, numero):
    agenda[nombre] = numero


# Función para buscar contacto
def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        return agenda[nombre]
    else:
        return "No encontrado"


# Función para eliminar contacto
def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        return "Contacto eliminado"
    else:
        return "No existe"


# Diccionario (agenda)
agenda = {}

# Agregar contactos
agregar_contacto(agenda, "Juan", "123456")
agregar_contacto(agenda, "Ana", "987654")

# Buscar contacto
print("Número de Juan:", buscar_contacto(agenda, "Juan"))

# Eliminar contacto
print(eliminar_contacto(agenda, "Ana"))

# Ver agenda final
print("Agenda:", agenda)