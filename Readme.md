# 🚀 Algoritmo Genético - Problema del Viajero (TSP)

## 📋 Descripción del Proyecto

Este proyecto implementa un algoritmo genético en Python para resolver el **Problema del Viajero (Travelling Salesman Problem - TSP)**.

El objetivo es encontrar una ruta que recorra todas las ciudades exactamente una vez y regrese al punto de inicio, **minimizando la distancia total del recorrido**.

El sistema utiliza operadores genéticos clásicos:

- **Selección por torneo**
- **Cruce ordenado (OX)**
- **Mutación por intercambio**

## 🎯 Características Principales

### 🔍 Algoritmo Genético

- Generación inicial de rutas aleatorias
- Evaluación de distancias mediante **distancia euclidiana**
- Selección de padres por **torneo**
- Cruce que respeta el orden de las ciudades
- Mutación probabilística por intercambio de posiciones

### 📊 Parámetros Configurables

| Parámetro        | Descripción                  | Valor por defecto |
|------------------|------------------------------|-------------------|
| `tam_poblacion`  | Tamaño de la población       | 50                |
| `generaciones`   | Número de iteraciones        | 1000              |
| `tasa_mutacion`  | Probabilidad de mutación     | 0.1               |

### 📈 Resultados

- ✅ Ruta óptima aproximada encontrada
- ✅ Distancia total mínima calculada

## 🗺️ Ciudades Incluidas

El sistema trabaja con un conjunto de **8 ciudades**, cada una con coordenadas cartesianas:

| Ciudad | Coordenadas |
|--------|-------------|
| A      | (0, 0)      |
| B      | (1, 5)      |
| C      | (2, 3)      |
| D      | (5, 2)      |
| E      | (6, 6)      |
| F      | (7, 1)      |
| G      | (8, 4)      |
| H      | (9, 9)      |

## 🏗️ Estructura del Proyecto

### Funciones Principales

#### `distancia(ciudad1, ciudad2)`
Calcula la distancia euclidiana entre dos ciudades.

#### `distancia_ruta(ruta)`
Evalúa la distancia total de una ruta cerrada.

#### `crear_poblacion_inicial(tam_poblacion)`
Genera un conjunto de rutas aleatorias.

#### `selection(poblacion, distancias, k=3)`
Implementa la selección por torneo.

#### `cruce(padre1, padre2)`
Aplica cruce ordenado (OX) entre dos rutas.

#### `mutacion(ruta, tasa_mutacion)`
Aplica mutación aleatoria por intercambio.

#### `algoritmo_genetico()`
Función principal que ejecuta el proceso evolutivo.

## 🖼️ Ejemplo de Ejecución

Ejecutando el programa:

```bash
python tsp_genetico.py

salida esperada: 
Ruta óptima: ['C', 'D', 'F', 'G', 'H', 'E', 'B', 'A']
Distancia óptima: 23.41
## 📊 Resultados Esperados

El programa proporciona:

- ✅ La mejor ruta encontrada después de todas las generaciones  
- ✅ La distancia mínima calculada  
- ⚠️ Comportamiento probabilístico: los resultados pueden variar en cada ejecución  

## 🧠 Aplicaciones

Este sistema puede ser utilizado como:

- 📚 Base para la enseñanza de algoritmos genéticos  
- 🧪 Herramienta educativa en cursos de optimización y metaheurísticas  
- 🧮 Simulador de soluciones aproximadas para problemas NP-duros  
- 🐍 Ejemplo práctico de Python aplicado a IA y optimización  

## 👥 Autores

**Saira Sharid Sanabria Muñoz** – [sharito202](https://github.com/sharito202)