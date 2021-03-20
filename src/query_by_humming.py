
import streamlit as st

import search_a_song_page
import database_page
import about_page
import configuration_page

st.set_page_config(
    page_title="Query by Humming",
    page_icon="images/microphone.png",
    layout="wide",
    initial_sidebar_state="auto",
)

st.sidebar.title("Query by humming")
st.sidebar.image("images/image_medium.png")

option = st.sidebar.radio(
    'Select an option:',
     ["Search a song", "Database", "Configuration", "About"])

if option == "Search a song":
    st.title("Query by humming - " + option)
    search_a_song_page.render()

if option == "Database":
    st.title("Query by humming - " + option)
    database_page.render()

if option == "Configuration":
    st.title("Query by humming - " + option)
    configuration_page.render()

if option == "About":
    st.title("Query by humming - " + option)
    about_page.render()
