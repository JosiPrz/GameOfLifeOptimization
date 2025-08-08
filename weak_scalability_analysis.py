import time
import matplotlib.pyplot as plt
import multiprocessing as mp
from game_of_life import GameOfLife

def measure_performance(game, steps):
    start_time = time.time()
    game.parallel_step()  # Ejecutar en paralelo
    end_time = time.time()
    return end_time - start_time

def main():
    steps = 100
    results = []
    speeds = []
    efficiencies = []
    max_processes = mp.cpu_count()

    # Escalamiento débil
    for p in range(1, max_processes + 1):
        rows, cols = 100 * p, 100 * p  # Aumentar la grilla proporcionalmente
        game = GameOfLife(rows, cols)

        Tp = measure_performance(game, steps)  # Tiempo paralelo

        # Medir T1 para el tamaño de grilla correspondiente
        T1 = measure_performance(GameOfLife(rows, cols), steps)  # Tiempo secuencial con la misma grilla
        
        efficiency = T1 / Tp  # Calcular eficiencia

        speeds.append(Tp)
        efficiencies.append(efficiency)

        # Almacenar resultados en la lista
        results.append((p, Tp, efficiency))

    # Imprimir tabla de resultados
    print(f"{'Número de Procesos (p)':<25}{'Tiempo de Ejecución (Tp)':<25}{'Eficiencia':<15}")
    for p, tp, eff in results:
        print(f"{p:<25}{tp:.2f} s{eff:<15.2f}")

    # Graficar resultados
    plt.figure(figsize=(12, 5))

    # Gráfica de tiempo vs número de procesos
    plt.subplot(1, 2, 1)
    plt.plot(range(1, max_processes + 1), speeds, marker='o')
    plt.title('Tiempo vs Número de Procesos')
    plt.xlabel('Número de Procesos')
    plt.ylabel('Tiempo (s)')

    # Gráfica de eficiencia
    plt.subplot(1, 2, 2)
    plt.plot(range(1, max_processes + 1), efficiencies, marker='o', color='orange')
    plt.title('Eficiencia vs Número de Procesos')
    plt.xlabel('Número de Procesos')
    plt.ylabel('Eficiencia')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()