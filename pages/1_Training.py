import streamlit as st,pandas as pd,plotly.graph_objects as go
from core.data import scenario

def chart(df):
 fig=go.Figure(data=[go.Candlestick(x=df.index,open=df["Open"],high=df["High"],low=df["Low"],close=df["Close"])])
 fig.update_layout(height=600,xaxis_rangeslider_visible=False)
 return fig

if "loaded" not in st.session_state:
 t,v,f=scenario(); st.session_state.t=t; st.session_state.v=v; st.session_state.f=f; st.session_state.loaded=True

st.subheader("Hidden Historical Scenario")
st.metric("Portfolio",f"${st.session_state.account:,.0f}")
st.plotly_chart(chart(st.session_state.v),use_container_width=True)
entry=st.number_input("Entry Price",min_value=0.0)
stop=st.number_input("Stop Loss",min_value=0.0)
target=st.number_input("Target",min_value=0.0)
choice=st.radio("Decision",["BUY","PASS"])
if entry>0 and stop>0 and stop<entry:
 risk_share=entry-stop
 acct_risk=st.session_state.account*0.01
 shares=int(acct_risk/risk_share)
 st.info(f"1% Risk=${acct_risk:.2f} | Risk/Share=${risk_share:.2f} | Shares={shares}")
if st.button("Reveal & Score"):
 full=pd.concat([st.session_state.v,st.session_state.f])
 st.plotly_chart(chart(full),use_container_width=True)
 future=st.session_state.f
 result='PASS'
 pnl=0
 if choice=='BUY' and entry>0 and stop>0 and target>entry:
   hit_target=(future['High']>=target).any()
   hit_stop=(future['Low']<=stop).any()
   risk=st.session_state.account*0.01
   if hit_target and not hit_stop: pnl=risk*2; st.session_state.wins+=1; result='WIN +2R'
   elif hit_stop: pnl=-risk; st.session_state.losses+=1; result='LOSS -1R'
   else: result='OPEN / NO HIT'
   st.session_state.account+=pnl
   st.session_state.trades.append(st.session_state.account)
 st.success(result)
 st.write('Ticker:',st.session_state.t)
if st.button('Next Scenario'):
 st.session_state.loaded=False
 st.rerun()
