# Tarea 2 - Josimark Perez

## Capturas de las herramientas de perfilzado utilizadas

### cProfile

![cprofile](Images\Picture1.png)

**Identificación de Cuellos de Botella**
- count_alive_neighbors es el mayor cuello de botella debido a su alta cantidad de llamadas y el tiempo acumulado que consume. Esto sugiere que optimizar esta función tendría un impacto significativo en el rendimiento general del juego.
- step también es costosa, pero su costo se deriva en gran parte de la llamada a count_alive_neighbors.

### Line_Profiler
![lineprofiler](Images\Picture2.png)

El mayor costo computacional proviene de la función *count_alive_neighbors*, que podría ser optimizada mediante vectorización, reduciendo significativamente el tiempo de ejecución del método step().

## Capturas de escalamiento fuerte y debil 

### Fuerte 
![graph-strong](Images\Picture3.png)

### Debil 
![graph-weak](Images\Picture4.png)

## Tablas comparativas de tiempo

### Escalamiento Fuerte 
![table-strong](Images\Picture5.jpg)

### Escalamiento Debil 
![table-weak](Images\Picture6.jpg)

## Análisis Crítico de los Resultados

### Cuellos de Botella

Función count_alive_neighbors:

- Se identificó que la función count_alive_neighbors es el principal cuello de botella en la ejecución del programa, acumulando el 92% del tiempo total (121.994 segundos de un total de 131.397 segundos). Esto indica que el conteo de vecinos vivos es intensivo en cómputo y presenta oportunidades de optimización.
- Además, se realizaron 26,214,400 llamadas a la función count_alive_neighbors, lo que sugiere que se está invocando repetidamente para cada celda en cada paso. Este alto volumen de llamadas puede ser un factor crítico que afecta el rendimiento general.
- Las funciones incorporadas min y max también contribuyen al tiempo acumulado, lo que sugiere que su uso repetido en un contexto de alto volumen podría estar impactando negativamente el rendimiento.

### Efecto de la Paralelización en el Rendimiento
- En el análisis de escalamiento débil, se observó que la eficiencia se mantiene bastante alta, especialmente con 2 a 4 procesos, donde la eficiencia se aproxima a 1. Esto sugiere que la paralelización está funcionando de manera efectiva en estas configuraciones.
- Sin embargo, a partir de 5 procesos, la eficiencia comienza a variar, lo que puede indicar que la sobrecarga de comunicación o la contención de recursos empiezan a afectar el rendimiento.
- En el análisis de escalamiento fuerte, los resultados muestran que el speedup no es lineal. Para 2 procesos, se registró un speedup significativo (34.69), pero a medida que se incrementa el número de procesos, el speedup se reduce drásticamente (por ejemplo, 26.24 para 8 procesos). Esto sugiere que la paralelización no está aprovechando eficientemente los recursos más allá de cierto punto.

## Propuestas de Optimización Basadas en la Evidencia Observada

### Optimización de Algoritmos
- Optimizar la función count_alive_neighbors: Revisar la lógica de esta función podría llevar a mejoras significativas en el rendimiento. Se podria considerar un enfoque alternativo para contar vecinos, como almacenar el estado de los vecinos en una estructura de datos más eficiente lo que podría permitir un acceso más rápido.
- Además, sería beneficioso minimizar las llamadas a esta función. En lugar de contar vecinos en cada paso, se podría implementar un enfoque en el que solo se cuenten los vecinos cuando cambian (por ejemplo, cuando una celda nace o muere). Esto podría reducir considerablemente el número de invocaciones a count_alive_neighbors.

### Optimización de Estructura de Datos
- Aprovechar al máximo las capacidades de NumPy, utilizando operaciones vectorizadas en lugar de realizar operaciones en bucles. Esto podría mejorar el rendimiento al permitir que se realicen cálculos en todo el array a la vez.

### Optimización de Paralelización
- Para reducir la sobrecarga de comunicación, se podria implementar que los procesos hagan el menor número posible de llamadas entre sí. Dividir el tablero en secciones más grandes que se procesen de manera independiente podría ser una estrategia efectiva.
- También se puede considerar la implementación de un esquema de carga balanceada, donde cada proceso trabaje en un bloque de celdas que se adapte a su carga de trabajo, ayudando así a evitar que algunos procesos terminen mucho antes que otros.