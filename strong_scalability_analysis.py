import numpy as np
import multiprocessing as mp
import time
import matplotlib.pyplot as plt
from game_of_life import GameOfLife

def measure_performance(game, steps, p):
    start_time = time.time()
    if p == 1:
        game.run(steps)  # Modo secuencial
    else:
        game.parallel_step()  # Modo paralelo
    end_time = time.time()
    return end_time - start_time

def main():
    rows, cols = 512, 512
    steps = 100

    # Medir el tiempo para el juego secuencial - T1
    single_process_game = GameOfLife(rows, cols)
    T1 = measure_performance(single_process_game, steps, 1)  # T1
    results = []
    speeds = []
    efficiencies = []
    max_processes = mp.cpu_count()

    # Medir tiempos para diferentes números de procesos
    for p in range(1, max_processes + 1):
        game = GameOfLife(rows, cols)
        Tp = measure_performance(game, steps, p)  # Tp
        speedup = T1 / Tp
        efficiency = speedup / p
        speeds.append(speedup)
        efficiencies.append(efficiency)
        
        # Almacenar resultados en la lista
        results.append((p, speedup, efficiency))

    # Imprimir tabla de resultados
    print(f"{'Número de Procesos (p)':<25}{'Speedup':<25}{'Eficiencia':<15}")
    for p, speedup, eff in results:
        print(f"{p:<25}{speedup:.2f} s{eff:<15.2f}")


    # Graficar resultados
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(range(1, max_processes + 1), speeds, marker='o')
    plt.title('Speedup vs Número de Procesos')
    plt.xlabel('Número de Procesos')
    plt.ylabel('Speedup')

    plt.subplot(1, 2, 2)
    plt.plot(range(1, max_processes + 1), efficiencies, marker='o', color='orange')
    plt.title('Eficiencia vs Número de Procesos')
    plt.xlabel('Número de Procesos')
    plt.ylabel('Eficiencia')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()