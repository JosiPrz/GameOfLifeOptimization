# Game of Life | Tarea 1

Josimark Pérez

## Descripción del Repositorio

En este repositorio encontrarás dos archivos principales:

1. Juego de la Vida

- Archivo: game_of_life.py
- Descripción: Este archivo implementa el Juego de la Vida de Conway. Se ejecuta el juego y se crea una visualización gráfica de la evolución de las celdas.
- Cómo Ejecutar: Para ejecutar el código, abre la terminal y usa el siguiente comando: python game_of_life.py


2. Rendimiento

- Archivo: rendimiento.py
- Descripción: Este archivo realiza pruebas de rendimiento variando el tamaño de la grilla. Genera una visualización log-log que muestra una gráfica del tiempo promedio por iteración en función del tamaño de entrada (número de celdas).
- Cómo Ejecutar: Para ejecutar el código de pruebas de rendimiento, abre la terminal y usa el siguiente comando: python rendimiento.py

3. Perfilador
- Archivo: g_profileC.py
- Descripción: Muestra los tiempos de ejecucion de cada funcion en game_of_life.py para identificar posibles cuellos de botella.

4. Analisis de escalabilidad fuerte 
- Archivo: strong_scalability_analysis.py
- Descripción: Aplica paralelismo, varia el numero nucleos y muestra los resultados en graficas para saber determinar el speedup, eficiencia y analizar la ganacia .
- 

5. Analisis de escalabilidad debil
- Archivo: weak_scalability_analysis.py
- Descripción: Se aumenta el número de nucleos, escala proporcionalmente el tamaño de la grilla y muestra los resultados en graficas para saber determinar el el tiempo de ejecucion asi como la eficiencia.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas especificadas en el archivo requirements.txt

Puedes instalarlas desde la terminal usando el comando: pip install -r requirements.txt

## Notas
Asegúrate de estar en el directorio correcto donde se encuentran los archivos antes de ejecutar los comandos.
Las visualizaciones se generarán en ventanas emergentes, asegúrate de que tu entorno de desarrollo soporte gráficos.

## Ejecución

### Simulación y Visualización
 Aquí se puede visualizar el Game of Life con un tamaño fijo (50x50) y observar la dinámica del autómata.

https://ulead-my.sharepoint.com/:v:/g/personal/raquel_mora_ulead_ac_cr/EXO9Gl0W06FAs-E-xwUtiMwBcNmyQwofhGzCcCjw6xdXkQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=LrR93l

(Usar Link para ver Visualización)

## Análisis de rendimiento
Se probó la simulación con diferentes tamaños (32, 64, 128, 256, 512, 1024) y 10 iteraciones cada una.

Estos fueron nuestros resultados:

Tamaño: 32x32, Tiempo promedio por iteración: 0.001953 segundos
Tamaño: 64x64, Tiempo promedio por iteración: 0.007990 segundos
Tamaño: 128x128, Tiempo promedio por iteración: 0.031868 segundos
Tamaño: 256x256, Tiempo promedio por iteración: 0.127511 segundos
Tamaño: 512x512, Tiempo promedio por iteración: 0.541824 segundos
Tamaño: 1024x1024, Tiempo promedio por iteración: 2.215804 segundos

Gráfica del rendimiento:
<img width="931" alt="Screenshot 2025-06-18 at 5 03 22 PM" src="https://github.com/user-attachments/assets/a6745d2f-557f-41ec-adf6-06db8bedddac" />

## Análisis Resultados

Los resultados muestran que entre cada incremento de tamaño, el tiempo promedio crece consistentemente. Con cada prueba, se duplica el tamaño del tablero y el tiempo se multiplica aproximadamente por 4, coincidiendo con una complejidad cuadrática O(n²).

| Tamaño (n x n) | Tiempo promedio (segundos) | Incremento relativo |
| -------------- | -------------------------- | ------------------------------ |
| 32 x 32        | 0.00195                    | —                              |
| 64 x 64        | 0.00799                    | \~4.09x tiempo                 |
| 128 x 128      | 0.03187                    | \~3.99x tiempo                 |
| 256 x 256      | 0.12751                    | \~4.00x tiempo                 |
| 512 x 512      | 0.54182                    | \~4.25x tiempo                 |
| 1024 x 1024    | 2.2158                     | \~4.09x tiempo                 |

El cuello de botella en términos de tiempo es la operación que cuenta cuantos vecinos vivos tiene cada celda ya  que se repite para todas las celdas en cada iteración.  Además, el código no tiene elementos de paralelismo que permitiriían dividir el tablero y procesar varias partes al mismo tiempo. 

Si se fuera a implementar esto, el juego podría ser más rápido en proporción a cuantos núcleos disponibles. Conforme la tabla siga creciendo, optimizar sería esencial para tener tiempos de ejecución mejores.
