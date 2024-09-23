import streamlit as st
import time
st.set_page_config(page_title='Tic Tac Toe', page_icon='📈', layout="wide", initial_sidebar_state="collapsed")
st.logo('images/logo.png', icon_image='images/neww.png')
st.sidebar.title("Hi There!")

welcome_message = """
**Welcome to the Ultimate Tic-Tac-Toe Showdown! ❌⭕**

Get ready to immerse yourself in this classic game of strategy and wits. Whether you're Team X or Team O, it’s time to put your skills to the test and claim victory on the grid. Make your move wisely, and let’s see who can align three in a row first. Will it be you or your opponent? The game is on!
"""

def stream_data():
    time.sleep(2)
    for word in welcome_message.split(" "):
        yield word + " "
        time.sleep(0.02)
    st.image("images/x-o.png", caption="Sunrise Of AI",use_column_width ='always')

st.write_stream(stream_data)
