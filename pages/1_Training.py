import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from core.data import scenario

def chart(df):
 fig=go.Figure(data=[go.Candlestick(x=df.index,open=df.Open,high=df.High,low=df.Low,close=df.Close)])
 fig.update_layout(xaxis_rangeslider_visible=False,height=600)
 return fig

if "loaded" not in st.session_state:
 t,v,f=scenario(); st.session_state.t=t; st.session_state.v=v; st.session_state.f=f; st.session_state.loaded=True

st.title("Training Round")
st.info("Ticker hidden. Decide based on chart only.")
st.plotly_chart(chart(st.session_state.v),use_container_width=True)
choice=st.radio("Decision",["BUY","PASS"])
support=st.number_input("Support",value=0.0)
stop=st.number_input("Stop Loss",value=0.0)
target=st.number_input("Target",value=0.0)
if st.button("Reveal Future"):
 full=pd.concat([st.session_state.v,st.session_state.f])
 st.plotly_chart(chart(full),use_container_width=True)
 st.write(f"Hidden ticker was: {st.session_state.t}")
 rr=(target-max(stop,0.01)) if target>0 else 0
 st.success(f"Decision recorded: {choice}")
if st.button("Next Scenario"):
 del st.session_state.loaded
 st.rerun()