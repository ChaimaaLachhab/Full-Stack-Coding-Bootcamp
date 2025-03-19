import time
import os

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        if initial_state:
            for i, j in initial_state:
                if 0 <= i < rows and 0 <= j < cols:
                    self.grid[i][j] = 1

    def print_grid(self):
        os.system("cls" if os.name == "nt" else "clear")
        for row in self.grid:
            print(" ".join("🟩" if cell else "⬛" for cell in row))
        print("\n")

    def count_neighbors(self, x, y):
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        count = 0
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                count += self.grid[nx][ny]
        return count

    def update(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                live_neighbors = self.count_neighbors(i, j)

                if self.grid[i][j] == 1:
                    if live_neighbors in [2, 3]:
                        new_grid[i][j] = 1
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = 1

        self.grid = new_grid

    def run(self, generations=10, delay=0.5):
        for _ in range(generations):
            self.print_grid()
            self.update()
            time.sleep(delay)

blinker = [(2, 1), (2, 2), (2, 3)]
glider = [(1, 2), (2, 2), (2, 3), (3, 1), (3, 2)]

game = GameOfLife(rows=10, cols=10, initial_state=glider)
game.run(generations=20, delay=0.1)