import streamlit as st
import time


def start_timer(page_num: int):
    st.session_state[f"page_{page_num}_timer"] = time.time()
