# Import necessary libraries
import streamlit as st
import math

# Page configuration
st.set_page_config(page_title="Stock Futures Pricing App", page_icon="📈")

# Title
st.title("Stock Futures Pricing App")

# A python function that calculates the value of a futures contract

def FuturePrice(spotPrice, benefit, cost, r, t):
    return (spotPrice - benefit + cost)*math.pow(1 + r, t);

# Sidebar for user input

st.dataframe(df.style.format(subset=['Position', 'Marks'], formatter="{:.2f}"


symbol = st.sidebar.text_input("Enter Stock Symbol", "GARAN")
benefit = st.sidebar.number_input("Dividend", value=0.0)
miscCharges = st.sidebar.number_input("Cost", value=0.0);
t = st.sidebar.number_input("Vadeye Kalan Gün Sayısı", value=0.0)
r = st.sidebar.number_input("Vadeye Kalan Gün Sayısı", value=0.40);
spotPrice = st.sidebar.number_input("Enter Stock Price", value=0.0)
ratePerday      = r/365;

contractPrice   = FuturePrice(spotPrice, benefit, miscCharges, ratePerday, t);

# Display results
st.write(f"Stock Price: ${spotPrice}")
st.write(f"Futures Price: ${contractPrice}")
