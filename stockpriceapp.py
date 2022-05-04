import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""""
# Stock Price App

Shown below are the stock **closing price** and ***volume*** of Tesla!

""")

tickersymbol = 'TSLA'

tickerData = yf.Ticker(tickersymbol)

tickerDf = tickerData.history(period= '1d', start='2010-5-03', end='2022-5-03')

st.write("""

### Closing Price

""")
st.line_chart(tickerDf.Close)
st.write("""

### Volume

""")
st.line_chart(tickerDf.Volume)

