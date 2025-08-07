# Capturas de las herramientas de perfilzado utilizadas
## cProfile

![cprofile](Images\Picture1.png)

**Identificación de Cuellos de Botella**
- count_alive_neighbors es el mayor cuello de botella debido a su alta cantidad de llamadas y el tiempo acumulado que consume. Esto sugiere que optimizar esta función tendría un impacto significativo en el rendimiento general del juego.
- step también es costosa, pero su costo se deriva en gran parte de la llamada a count_alive_neighbors.

## Line_Profiler
![cprofile](Images\Picture2.png)

El mayor costo computacional proviene de la función *count_alive_neighbors*, que podría ser optimizada mediante vectorización, reduciendo significativamente el tiempo de ejecución del método step().