import streamlit as st
st.set_page_config(page_title='Tic Tac Toe', page_icon='📈', layout="wide", initial_sidebar_state="collapsed")
st.logo('images/logo.png', icon_image='images/neww.png')
st.sidebar.title("Hi There!")
def create_board():
    return [["__" for _ in range(3)] for _ in range(3)]

# def print_board(board):
#     for row in board:
#         st.write(" | ".join(row))
#         st.write("-" * 9)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Row 1
        [board[1][0], board[1][1], board[1][2]],  # Row 2
        [board[2][0], board[2][1], board[2][2]],  # Row 3
        [board[0][0], board[1][0], board[2][0]],  # Column 1
        [board[0][1], board[1][1], board[2][1]],  # Column 2
        [board[0][2], board[1][2], board[2][2]],  # Column 3
        [board[0][0], board[1][1], board[2][2]],  # Diagonal 1
        [board[0][2], board[1][1], board[2][0]]   # Diagonal 2
    ]
    return [player, player, player] in win_conditions

def check_tie(board):
    return all(cell != "__" for row in board for cell in row)

def reset_game():
    st.session_state.board = create_board()
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

def tic_tac_toe():
    if 'board' not in st.session_state:
        reset_game()

    st.title("Tic Tac Toe")

    # Display the board
#     print_board(st.session_state.board)

    if st.session_state.game_over:
        if st.session_state.winner:
            st.write(f"Player {st.session_state.winner} wins!")
        else:
            st.write("It's a tie!")
        if st.button("Play Again"):
            reset_game()
            st.rerun()
    else:
        st.write(f"Player {st.session_state.current_player}'s turn")

        # Grid of buttons for player moves
        cols = st.columns(3)
        for i in range(3):
            for j in range(3):
                with cols[j]:
                    if st.button(f"{st.session_state.board[i][j]}", key=f"btn_{i}_{j}", disabled=st.session_state.board[i][j] != "__"):
                        if not st.session_state.game_over:
                            st.session_state.board[i][j] = st.session_state.current_player
                            if check_win(st.session_state.board, st.session_state.current_player):
                                st.session_state.game_over = True
                                st.session_state.winner = st.session_state.current_player
                            elif check_tie(st.session_state.board):
                                st.session_state.game_over = True
                            else:
                                st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                        st.rerun()

if __name__ == "__main__":
    tic_tac_toe()
