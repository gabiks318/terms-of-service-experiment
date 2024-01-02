import time
import streamlit as st


def stop_timer(page_num: int):
    time_taken = time.time() - st.session_state[f"page_{page_num}_timer"]
    st.session_state[f"page_{page_num}_time_taken"] = time_taken
    print(f"Page {page_num} took {time_taken} seconds")


def next_page(page_num: int):
    stop_timer(page_num)
    st.session_state.page_num = page_num + 1
