# Función para contar votos
def contar_votos(candidatos, votos):
    resultados = {}
    votos_invalidos = 0

    # Inicializar candidatos en 0
    for candidato in candidatos:
        resultados[candidato] = 0

    # Contar votos
    for voto in votos:
        if voto in candidatos:
            resultados[voto] += 1
        else:
            votos_invalidos += 1

    return resultados, votos_invalidos


# Función para determinar ganador
def obtener_ganador(resultados):
    ganador = max(resultados, key=resultados.get)
    votos_ganador = resultados[ganador]
    total_validos = sum(resultados.values())

    porcentaje = (votos_ganador / total_validos) * 100

    return ganador, porcentaje


# Lista de candidatos
candidatos = ["Ana", "Luis", "Carlos"]

# Lista de votos (algunos inválidos)
votos = ["Ana", "Luis", "Pedro", "Ana", "Carlos", "Luis", "Ana", "Maria"]

# Contar votos
resultados, invalidos = contar_votos(candidatos, votos)

# Obtener ganador
ganador, porcentaje = obtener_ganador(resultados)

# Mostrar resultados
print("Resultados:", resultados)
print("Votos inválidos:", invalidos)
print("Ganador:", ganador)
print("Porcentaje:", porcentaje, "%")