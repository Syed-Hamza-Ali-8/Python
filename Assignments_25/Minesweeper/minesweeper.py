import streamlit as st
import random

def initialize_board(size, num_mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    numbers = [[0 for _ in range(size)] for _ in range(size)]
    mine_positions = set()

    while len(mine_positions) < num_mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        mine_positions.add((row, col))

    for (r, c) in mine_positions:
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if 0 <= i < size and 0 <= j < size and (i, j) not in mine_positions:
                    numbers[i][j] += 1

    return board, numbers, mine_positions

if 'board' not in st.session_state:
    st.session_state.board = []
    st.session_state.numbers = []
    st.session_state.mine_positions = set()
    st.session_state.revealed = set()
    st.session_state.size = 5
    st.session_state.num_mines = 5
    st.session_state.game_over = False
    st.session_state.restart = False 

st.sidebar.title("Minesweeper Settings")
st.session_state.size = st.sidebar.slider("Board Size", 3, 10, st.session_state.size)
st.session_state.num_mines = st.sidebar.slider("Number of Mines", 1, st.session_state.size**2 - 1, st.session_state.num_mines)

if st.sidebar.button("Start New Game"):
    st.session_state.board, st.session_state.numbers, st.session_state.mine_positions = initialize_board(
        st.session_state.size, st.session_state.num_mines)
    st.session_state.revealed = set()
    st.session_state.game_over = False
    st.session_state.restart = True
    st.rerun()

st.title("💣 Minesweeper")

if not st.session_state.board:
    st.session_state.board, st.session_state.numbers, st.session_state.mine_positions = initialize_board(
        st.session_state.size, st.session_state.num_mines)

for i in range(st.session_state.size):
    cols = st.columns(st.session_state.size)
    for j in range(st.session_state.size):
        key = f"{i}_{j}"
        if (i, j) in st.session_state.revealed:
            if (i, j) in st.session_state.mine_positions:
                cols[j].button("💥", disabled=True, key=key)
            else:
                num = st.session_state.numbers[i][j]
                cols[j].button(f"{num if num != 0 else ''}", disabled=True, key=key)
        else:
            if cols[j].button("■", key=key):
                if st.session_state.game_over:
                    continue
                if (i, j) in st.session_state.mine_positions:
                    st.session_state.revealed.update(st.session_state.mine_positions)
                    st.session_state.game_over = True
                else:
                    def flood_fill(row, col):
                        if (row, col) in st.session_state.revealed or not (0 <= row < st.session_state.size and 0 <= col < st.session_state.size):
                            return
                        st.session_state.revealed.add((row, col))
                        if st.session_state.numbers[row][col] == 0:
                            for x in range(row-1, row+2):
                                for y in range(col-1, col+2):
                                    flood_fill(x, y)
                    flood_fill(i, j)
                st.rerun() 

if st.session_state.game_over:
    st.error("💥 BOOM! You hit a mine. Game Over!")
elif st.session_state.size ** 2 - len(st.session_state.revealed) == st.session_state.num_mines:
    st.success("🎉 Congratulations! You cleared the minefield!")
