import cProfile
import pstats
import io
from game_of_life import GameOfLife 

def main():
    rows, cols = 512, 512  # Tamaño de la grilla
    game = GameOfLife(rows, cols)

    # Profiling
    pr = cProfile.Profile()
    pr.enable()  # Comienza a perfilar

    game.run(100)  # Ejecutar 100 pasos

    pr.disable()  # Detiene el perfilador

    # Exportar resultados en formato .prof para analisis con snakeviz
    pr.dump_stats("profiling_results.prof")
    
    # Exportar resultados
    s = io.StringIO()
    sortby = pstats.SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    
    with open("profiling_results.txt", "w") as f:
        f.write(s.getvalue())

if __name__ == "__main__":
    main()