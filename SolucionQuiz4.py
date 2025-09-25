import random
import math

ciudades = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (2, 3),
    'D': (5, 2),
    'E': (6, 6),
    'F': (7, 1),
    'G': (8, 4),
    'H': (9, 9)
}

def distancia(ciudad1, ciudad2):
    """Calcula la distancia euclidiana entre dos ciudades."""
    x1, y1 = ciudades[ciudad1]
    x2, y2 = ciudades[ciudad2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def distancia_ruta(ruta):
    """Calcula la distancia total de una ruta (incluyendo el regreso al inicio)."""
    total = 0.0
    n = len(ruta)
    for i in range(n):
        total += distancia(ruta[i], ruta[(i + 1) % n])
    return total

def crear_poblacion_inicial(tam_poblacion):
    """Crea una población inicial de rutas aleatorias."""
    poblacion = []
    ciudades_lista = list(ciudades.keys())
    for _ in range(tam_poblacion):
        ruta = ciudades_lista.copy()
        random.shuffle(ruta)
        poblacion.append(ruta)
    return poblacion

def selection(poblacion, distancias, k=3):
    """Selección por torneo: elige el mejor de k individuos aleatorios."""
    seleccionado = random.choice(poblacion)
    for individuo in random.sample(poblacion, k-1):
        if distancias[poblacion.index(individuo)] < distancias[poblacion.index(seleccionado)]:
            seleccionado = individuo
    return seleccionado

def cruce(padre1, padre2):
    """Cruce ordenado (OX): preserva el orden relativo de los elementos."""
    size = len(padre1)
    hijo = [None] * size
    start, end = sorted(random.sample(range(size), 2))
    
    # Copiar segmento del padre1
    hijo[start:end] = padre1[start:end]
    
    # Completar con elementos del padre2
    pos = end
    for ciudad in padre2[end:] + padre2[:end]:
        if ciudad not in hijo:
            if pos >= size:
                pos = 0
            hijo[pos] = ciudad
            pos += 1
    return hijo

def mutacion(ruta, tasa_mutacion):
    """Mutación por intercambio: intercambia dos ciudades con una probabilidad."""
    if random.random() < tasa_mutacion:
        i, j = random.sample(range(len(ruta)), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

# Algoritmo genético principal
def algoritmo_genetico(tam_poblacion=50, generaciones=1000, tasa_mutacion=0.1):
    # Crear población inicial
    poblacion = crear_poblacion_inicial(tam_poblacion)
    mejor_ruta = None
    mejor_distancia = float('inf')
    
    for generacion in range(generaciones):
        # Calcular distancias
        distancias = [distancia_ruta(ruta) for ruta in poblacion]
        
        # Encontrar el mejor de la generación
        min_dist = min(distancias)
        if min_dist < mejor_distancia:
            mejor_distancia = min_dist
            mejor_ruta = poblacion[distancias.index(min_dist)]
        
        # Crear nueva población
        nueva_poblacion = []
        for _ in range(tam_poblacion // 2):
            # Selección
            padre1 = selection(poblacion, distancias)
            padre2 = selection(poblacion, distancias)
            
            # Cruce
            hijo1 = cruce(padre1, padre2)
            hijo2 = cruce(padre2, padre1)
            
            # Mutación
            hijo1 = mutacion(hijo1, tasa_mutacion)
            hijo2 = mutacion(hijo2, tasa_mutacion)
            
            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion
    
    return mejor_ruta, mejor_distancia

# Ejecutar el algoritmo
ruta_optima, distancia_optima = algoritmo_genetico()
print("Ruta óptima:", ruta_optima)
print("Distancia óptima:", distancia_optima)