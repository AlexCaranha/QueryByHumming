import streamlit as st

def render():
    st.write("You are in About page")

    st.subheader("Pitch Detection")
    st.info(
        "A pitch detection algorithm (PDA) is an algorithm designed to estimate the pitch or fundamental frequency of a quasiperiodic or oscillating signal, usually a digital recording of speech or a musical note or tone. This can be done in the time domain, the frequency domain, or both. [Wikipedia](https://en.wikipedia.org/wiki/Pitch_detection_algorithm)"
    )

    st.subheader("Onset Detection")
    st.info(
        "Onset Detection is a way to identify the begining of notes."
    )

    st.subheader("Melody Matching")
    st.info(
        "Algorithms to match melodies."
    )