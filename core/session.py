import streamlit as st

def init_session():

    defaults = {
        "account": 10000.0,
        "wins": 0,
        "losses": 0,
        "trades": []
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
