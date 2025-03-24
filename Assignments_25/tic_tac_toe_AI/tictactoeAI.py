import streamlit as st
import numpy as np

st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="🎮")
st.title("🎮 Tic-Tac-Toe Game AI Version")

board = np.zeros((3, 3), dtype=int)  # 0-empty, 1-human, -1-AI

if "board_state" not in st.session_state:
    st.session_state.board_state = board
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.last_move = None 

def check_winner(board):
    for i in range(3):
        if abs(sum(board[i])) == 3:
            return np.sign(sum(board[i]))
        if abs(sum(board[:, i])) == 3:
            return np.sign(sum(board[:, i]))
    diag1 = sum([board[i, i] for i in range(3)])
    diag2 = sum([board[i, 2 - i] for i in range(3)])
    if abs(diag1) == 3:
        return np.sign(diag1)
    if abs(diag2) == 3:
        return np.sign(diag2)
    if not np.any(board == 0):
        return 0  # Draw
    return None

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == -1:
        return 1
    elif winner == 1:
        return -1
    elif winner == 0:
        return 0

    if is_max:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    board[i, j] = -1
                    score = minimax(board, False)
                    board[i, j] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    board[i, j] = 1
                    score = minimax(board, True)
                    board[i, j] = 0
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if st.session_state.board_state[i, j] == 0:
                st.session_state.board_state[i, j] = -1
                score = minimax(st.session_state.board_state, False)
                st.session_state.board_state[i, j] = 0
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        st.session_state.board_state[move] = -1

def reset_game():
    st.session_state.board_state = np.zeros((3, 3), dtype=int)
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.last_move = None

st.button("🔄 Restart Game", on_click=reset_game)
st.write("You are **X** | AI is **O**")

cols = st.columns(3)
for i in range(3):
    for j in range(3):
        symbol = ""
        if st.session_state.board_state[i, j] == 1:
            symbol = "❌"
        elif st.session_state.board_state[i, j] == -1:
            symbol = "⭕"

        if not st.session_state.game_over:
            if cols[j].button(symbol or " ", key=f"{i}{j}"):
                if st.session_state.board_state[i, j] == 0:
                    st.session_state.last_move = (i, j)
        else:
            cols[j].button(symbol or " ", key=f"{i}{j}", disabled=True)

if st.session_state.last_move:
    i, j = st.session_state.last_move
    if st.session_state.board_state[i, j] == 0:
        st.session_state.board_state[i, j] = 1
        winner = check_winner(st.session_state.board_state)
        if winner is None:
            ai_move()
            winner = check_winner(st.session_state.board_state)
        if winner is not None:
            st.session_state.game_over = True
            st.session_state.winner = winner
    st.session_state.last_move = None  # Reset after processing

if st.session_state.winner is not None:
    if st.session_state.winner == 1:
        st.success("🎉 You Win!")
    elif st.session_state.winner == -1:
        st.error("😎 AI Wins!")
    else:
        st.info("🤝 It's a Draw!")
