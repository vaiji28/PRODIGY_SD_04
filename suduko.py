def print_grid(grid):
    """Prints the Sudoku grid in a readable format."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    """Checks if it's valid to place num in grid[row][col]."""
    # Check if num is not in the current row
    if num in grid[row]:
        return False

    # Check if num is not in the current column
    for r in range(9):
        if grid[r][col] == num:
            return False

    # Check if num is not in the current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try possible numbers
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num  # Place num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack
                return False  # If no number is valid, return False
    return True  # Puzzle solved

def main():
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Puzzle:")
    print_grid(puzzle)
    
    if solve_sudoku(puzzle):
        print("\nSolved Sudoku Puzzle:")
        print_grid(puzzle)
    else:
        print("No solution exists.")

if _name_ == "_main_":
    main()
