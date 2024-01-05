import sys

class SudokuSolver:
    def __init__(self, filename):
        self.matrix = self.read_file(filename)
        self.number_of_calls = 0

    def read_file(self, textfile):
        with open(textfile, 'r') as file:
            file.readline()  # Skip the first line
            return [[int(c) for c in file.readline().strip()] for _ in range(9)]

    def is_valid(self, row, col, num):
        # Check row, column, and 3x3 square
        return all([
            all(num != self.matrix[row][i] for i in range(9)),
            all(num != self.matrix[i][col] for i in range(9)),
            all(num != self.matrix[row - row % 3 + i][col - col % 3 + j] for i in range(3) for j in range(3))
        ])

    def find_least_constrained_cell(self):
        min_options = 10  # More than the maximum possible options (1-9)
        min_cell = None
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] == 0:
                    options = sum(self.is_valid(i, j, num) for num in range(1, 10))
                    if options < min_options:
                        min_options, min_cell = options, (i, j)
        return min_cell

    def solve(self):
        self.number_of_calls += 1
        cell = self.find_least_constrained_cell()
        if not cell:
            self.display_solution()
            return True

        row, col = cell
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.matrix[row][col] = num
                if self.solve():
                    return True
                self.matrix[row][col] = 0
        return False

    def display_solution(self):
        print("Smart Backtracking Algorithm MRV Solution:")
        for row in self.matrix:
            print(row)
        print("Amount of Recursions:", self.number_of_calls)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        solver = SudokuSolver(sys.argv[1])
        solver.solve()
    else:
        print("Usage: python sudoku_solver.py <filename>")