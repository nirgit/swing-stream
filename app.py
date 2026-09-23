import streamlit as st
if "account" not in st.session_state: st.session_state.account=10000.0
if "wins" not in st.session_state: st.session_state.wins=0
if "losses" not in st.session_state: st.session_state.losses=0
if "trades" not in st.session_state: st.session_state.trades=[]
st.set_page_config(layout="wide")
st.title("Swing Trading Trainer MVP V2")
st.metric("Account", f"${st.session_state.account:,.0f}")
