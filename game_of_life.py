import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import multiprocessing as mp

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        # Inicializa el estado del tablero
        if initial_state is None:
            self.board = np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])
        else:
            self.board = initial_state

    # @profile
    def step(self):
        new_board = self.board.copy()
        for i in range(self.rows):
            for j in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(i, j)
                if self.board[i, j] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_board[i, j] = 0  # Muere
                else:
                    if alive_neighbors == 3:
                        new_board[i, j] = 1  # Nace
        self.board = new_board

    def count_alive_neighbors(self, x, y):
        total = 0
        for i in range(max(0, x-1), min(self.rows, x+2)):
            for j in range(max(0, y-1), min(self.cols, y+2)):
                if (i, j) != (x, y):  # No contar la celda misma
                    total += self.board[i, j]
        return total

    def get_state(self):
        return self.board

    def run(self, steps):
        for _ in range(steps):
            self.step()

    def visualize(self, steps):
        fig, ax = plt.subplots()
        img = ax.imshow(self.board, cmap='binary')

        def update(frame):
            self.step()
            img.set_array(self.board)
            return img,

        ani = animation.FuncAnimation(fig, update, frames=steps, interval=100, blit=True)
        plt.title("Juego de la vida")
        plt.show()
    
    
    def parallel_step(self):
        with mp.Pool(mp.cpu_count()) as pool:
            results = pool.map(self.process_cell, [(i, j) for i in range(self.rows) for j in range(self.cols)])
            new_board = np.zeros_like(self.board)
            for (i, j), state in results:
                new_board[i, j] = state
            self.board = new_board

    def process_cell(self, pos):
        x, y = pos
        alive_neighbors = self.count_alive_neighbors(x, y)
        if self.board[x, y] == 1:
            return (x, y), 1 if alive_neighbors in [2, 3] else 0
        else:
            return (x, y), 1 if alive_neighbors == 3 else 0

if __name__ == "__main__":
    rows, cols = 50, 50  # Tamaño de la grilla
    game = GameOfLife(rows, cols)
    game.visualize(100)  # Ejecutar y visualizar 100 pasos
