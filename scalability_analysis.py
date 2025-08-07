import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import time
from game_of_life import GameOfLife

def parallel_step(board_slice):
    new_board_slice = board_slice.copy()
    rows, cols = board_slice.shape
    for i in range(rows):
        for j in range(cols):
            alive_neighbors = count_alive_neighbors(board_slice, i, j)
            if board_slice[i, j] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_board_slice[i, j] = 0
            else:
                if alive_neighbors == 3:
                    new_board_slice[i, j] = 1
    return new_board_slice

def count_alive_neighbors(board_slice, x, y):
    total = 0
    rows, cols = board_slice.shape
    for i in range(max(0, x-1), min(rows, x+2)):
        for j in range(max(0, y-1), min(cols, y+2)):
            if (i, j) != (x, y):
                total += board_slice[i, j]
    return total

def run_parallel_game_of_life(rows, cols, steps, num_processes):
    game = GameOfLife(rows, cols)
    board = game.get_state()
    pool = multiprocessing.Pool(processes=num_processes)
    for _ in range(steps):
        board_slices = np.array_split(board, num_processes)
        results = pool.map(parallel_step, board_slices)
        board = np.vstack(results)
    pool.close()
    pool.join()
    return board

def measure_strong_scalability():
    results = []
    T1 = time.time()
    game = GameOfLife(512, 512)
    game.run(100)  # Tiempo para un solo proceso
    T1 = time.time() - T1

    for num_processes in [1, 2, 4, 8, 16]:
        start_time = time.time()
        run_parallel_game_of_life(512, 512, 100, num_processes)
        end_time = time.time()
        execution_time = end_time - start_time
        speedup = T1 / execution_time
        efficiency = speedup / num_processes
        results.append((num_processes, execution_time, speedup, efficiency))
    
    return results

def measure_weak_scalability():
    results = []
    for num_processes in range(1, 17):
        rows, cols = 100 * num_processes, 100 * num_processes
        start_time = time.time()
        run_parallel_game_of_life(rows, cols, 100, num_processes)
        end_time = time.time()
        execution_time = end_time - start_time
        results.append((num_processes, execution_time))
    
    return results

def plot_results(strong_results, weak_results):
    processes, times, speedups, efficiencies = zip(*strong_results)
    
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(processes, times, marker='o')
    plt.title('Escalamiento Fuerte: Tiempo de Ejecución')
    plt.xlabel('Número de Procesos')
    plt.ylabel('Tiempo (s)')

    plt.subplot(1, 2, 2)
    plt.plot(processes, efficiencies, marker='o')
    plt.title('Escalamiento Fuerte: Eficiencia')
    plt.xlabel('Número de Procesos')
    plt.ylabel('Eficiencia')

    plt.show()

    weak_processes, weak_times = zip(*weak_results)

    plt.figure()
    plt.plot(weak_processes, weak_times, marker='o')
    plt.title('Escalamiento Débil: Tiempo de Ejecución')
    plt.xlabel('Número de Procesos')
    plt.ylabel('Tiempo (s)')
    plt.show()

if __name__ == "__main__":
    strong_results = measure_strong_scalability()
    weak_results = measure_weak_scalability()
    plot_results(strong_results, weak_results)