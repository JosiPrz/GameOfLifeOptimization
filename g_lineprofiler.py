from line_profiler import LineProfiler
from game_of_life import GameOfLife 

def main():
    rows, cols = 512, 512  # Tamaño de la grilla
    game = GameOfLife(rows, cols)

    profiler = LineProfiler()
    profiler.add_function(game.step)  # Agrega las funciones que deseas perfilar

    profiler.enable()  # Comienza a perfilar

    game.run(100)  # Ejecutar 100 pasos

    profiler.disable()  # Detiene el perfilador

    profiler.print_stats()  # Muestra los resultados en la consola

if __name__ == "__main__":
    main()