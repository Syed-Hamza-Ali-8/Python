import streamlit as st
import numpy as np

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")
st.title("🎮 Tic-Tac-Toe")

if 'board' not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
if 'current_player' not in st.session_state:
    st.session_state.current_player = 1
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'winner_cells' not in st.session_state:
    st.session_state.winner_cells = []

# Winner check function
def check_winner(board):
    for i in range(3):
        if abs(sum(board[i, :])) == 3:
            return np.sign(board[i, 0]), [(i, j) for j in range(3)]
        if abs(sum(board[:, i])) == 3:
            return np.sign(board[0, i]), [(j, i) for j in range(3)]
    if abs(sum(board.diagonal())) == 3:
        return np.sign(board[0, 0]), [(i, i) for i in range(3)]
    if abs(sum(np.fliplr(board).diagonal())) == 3:
        return np.sign(board[0, 2]), [(i, 2 - i) for i in range(3)]
    return 0, []

def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current_player = 1
    st.session_state.game_over = False
    st.session_state.winner_cells = []

button_style = """
    <style>
    div.stButton > button {
        height: 80px;
        width: 80px;
        font-size: 35px;
        border: 2px solid #555;
        background-color: #f0f0f0;
        color: black;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

for i in range(3):
    cols = st.columns(3, gap='large')
    for j in range(3):
        cell_value = st.session_state.board[i, j]
        key = f"{i}{j}"

        label = " "
        if cell_value == 1:
            label = "❌"
        elif cell_value == -1:
            label = "⭕"

        disabled = st.session_state.board[i, j] != 0 or st.session_state.game_over

        if cols[j].button(label, key=key, disabled=disabled):
            if not st.session_state.game_over and st.session_state.board[i, j] == 0:
                st.session_state.board[i, j] = st.session_state.current_player

                winner, cells = check_winner(st.session_state.board)
                if winner != 0:
                    st.session_state.game_over = True
                    st.session_state.winner_cells = cells
                    st.success(f"🏆 Player {'❌' if winner == 1 else '⭕'} wins!")
                elif np.all(st.session_state.board != 0):
                    st.session_state.game_over = True
                    st.info("🤝 It's a draw!")
                else:
                    st.session_state.current_player *= -1

for i, j in st.session_state.winner_cells:
    st.write(f"Winning Cell: Row {i+1}, Column {j+1}")

if st.button("🔄 Reset Game"):
    reset_game()
