import streamlit as st
import numpy as np

def is_valid(board, row, col, num):

    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    st.title("🧩 Sudoku Solver")
    st.write("Enter the Sudoku puzzle below (use 0 for empty cells):")

    grid = []
    for i in range(9):
        row = []
        cols = st.columns(9)
        for j in range(9):
            cell_value = cols[j].number_input("", min_value=0, max_value=9, step=1, key=f"{i}-{j}")
            row.append(cell_value)
        grid.append(row)

    grid = np.array(grid)

    if st.button("Solve"):
        temp_grid = grid.copy()
        if solve_sudoku(temp_grid):
            st.success("✅ Sudoku Solved!")
            st.table(temp_grid)
        else:
            st.error("❌ No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
