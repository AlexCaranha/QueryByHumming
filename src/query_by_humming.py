
import streamlit as st
# import numpy as np
# import pandas as pd

def create_buttons_in_sidebar(buttons_names):
    for button_name in buttons_names:
        if st.sidebar.button(button_name):
            st.markdown(f"## {button_name}")

st.set_page_config(
    page_title="Query by Humming",
    page_icon="images/microphone.png",
    layout="wide",
    initial_sidebar_state="auto",
)

st.title("Query by humming")
st.sidebar.title("Query by humming")

create_buttons_in_sidebar(["Search a song", "Database", "Configuration", "About"])
