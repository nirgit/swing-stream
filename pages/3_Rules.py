import streamlit as st
from core.session import init_session

init_session()

st.title('Rules')
st.write('Risk 1% per trade. Seek 2:1 reward/risk minimum.')
