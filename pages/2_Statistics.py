import streamlit as st,pandas as pd
from core.session import init_session

init_session()

st.title('Statistics')
tr=len(st.session_state.get('trades',[]))
w=st.session_state.get('wins',0)
l=st.session_state.get('losses',0)
st.metric('Account',f"${st.session_state.get('account',10000):,.0f}")
st.metric('Trades',tr)
wr=(w/(w+l)*100) if (w+l)>0 else 0
st.metric('Win Rate',f"{wr:.1f}%")
if tr>0: st.line_chart(pd.Series(st.session_state['trades']))
