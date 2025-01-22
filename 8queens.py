# Check if it's safe to place a queen
def is_safe(board, row, col):
    # Check the same column above
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check the top-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the top-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

# Print the board
def print_board(board):
    for row in board:
        print("  ".join(row))
    print()

# Try to place queens
def solve_n_queens(board, row):
    # If all queens are placed, print the solution
    if row == len(board):
        print_board(board)
        return

    # Try placing a queen in each column of the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 'Q'
            # Recur to place the next queen
            solve_n_queens(board, row + 1)
            # Backtrack: Remove the queen
            board[row][col] = '_'

# Input the number of queens and solve
N = int(input("Enter the number of Queens: "))
board = [['_' for _ in range(N)] for _ in range(N)]
solve_n_queens(board, 0)
